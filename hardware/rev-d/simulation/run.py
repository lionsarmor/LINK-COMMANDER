#!/usr/bin/env python3
"""Bounded PS/2 SPICE study, not a complete adapter or production qualification."""
import argparse,csv,hashlib,io,json,os,re,subprocess,tempfile,urllib.request,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
parser=argparse.ArgumentParser()
parser.add_argument('--ngspice',default='ngspice')
parser.add_argument('--cache',type=Path,default=Path.home()/'.cache/link-commander-simulation')
parser.add_argument('--code-model-dir',type=Path,help='For privately extracted ngspice; ordinary installations load these automatically')
args=parser.parse_args();args.cache.mkdir(parents=True,exist_ok=True)
models=[('2N3904.lib','https://www.onsemi.com/pub/Collateral/2N3904.LIB','5608c109b8d68d57798557991cee506661d031916f589325fad5ed10d82ccbf7',None),('CD4050B.lib','https://www.ti.com/lit/zip/schm018','e8266016c89735465990a1a26fd2811425e1d0e2a17c4db3e6c76f18e7c93712','CD4050B.lib')]
for filename,url,sha,member in models:
 f=args.cache/filename
 if not f.exists():
  blob=urllib.request.urlopen(url,timeout=30).read()
  if member:blob=zipfile.ZipFile(io.BytesIO(blob)).read(member)
  f.write_bytes(blob)
 assert hashlib.sha256(f.read_bytes()).hexdigest()==sha, f'Model changed: review {f} before updating its hash'
# Explicit local adaptations, not the inaccessible TI support attachment:
# 1. Datasheet-confirmed non-inverting function, correcting the published NAND bug.
# 2. Rename VT to avoid ngspice interpreting it as built-in thermal voltage.
s=(args.cache/'CD4050B.lib').read_text()
assert '.PARAM AND  = 0' in s and '.PARAM NAND = 1' in s
s=s.replace('.PARAM AND  = 0','.PARAM AND  = 1').replace('.PARAM NAND = 1','.PARAM NAND = 0')
s=re.sub(r'\bVT\b','LC_INPUT_VT',s)
(args.cache/'CD4050B-local.lib').write_text(s)
parts=json.loads((ROOT/'circuit.json').read_text());by={p['ref']:p for p in parts}
def resistance(ref):
 value=by[ref]['value'];return float(value.replace('k','e3').replace('R',''))
rows=[];first_wave=None
with tempfile.TemporaryDirectory(prefix='link-commander-spice-') as td:
 work=Path(td);init='set ngbehavior=ps\n'
 if args.code_model_dir:
  init+=''.join(f'codemodel {p.resolve()}\n' for p in sorted(args.code_model_dir.glob('*.cm')))
 (work/'.spiceinit').write_text(init)
 def run_netlist(netlist,name):
  (work/'case.cir').write_text(netlist)
  result=subprocess.run([args.ngspice,'-b','case.cir'],cwd=work,text=True,capture_output=True,timeout=60)
  log=result.stdout+'\n'+result.stderr
  if result.returncode or re.search(r'(?im)(error|fatal|timestep too small|.*simulation interrupted)',log):raise RuntimeError(name+'\n'+log[-4000:])
  return {k:float(v) for k,v in re.findall(r'^([a-z][a-z0-9_]*)\s*=\s*([-+\deE.]+)',log,re.M)}
 # Test the local compatibility correction independently of the transistor circuit.
 sanity=f'''CD4050 model function check
.include "{args.cache.resolve()/'CD4050B-local.lib'}"
Vcc vcc 0 3.3
Vin a 0 PULSE(0 5 10u 100n 100n 20u 100u)
Xbuf y a vcc 0 CD4050B
Cl y 0 10p
.control
tran 50n 40u
meas tran lo find v(y) at=5u
meas tran hi find v(y) at=20u
quit
.endc
.end
'''
 m=run_netlist(sanity,'sanity');assert abs(m['lo'])<.1 and m['hi']>3.2
 for channel,(prefix,kind,inp,outp) in enumerate([('KBD','DATA',3,2),('KBD','CLOCK',5,4),('MOUSE','DATA',7,6),('MOUSE','CLOCK',9,10)]):
  q=by[f'Q{channel+1}'];r=11+4*channel;net=f'{prefix}_{kind}'
  assert q['value']=='2N3904' and q['pins']['1'][1]=='GND' and q['pins']['3'][1]==net
  assert by['U2']['pins'][str(inp)][1]==net and by['U2']['pins'][str(outp)][1]==f'GP{9+2*channel}'
  for ref,nets in [(r,{f'GP{8+2*channel}',f'Q{channel+1}_B'}),(r+1,{f'Q{channel+1}_B','GND'}),(r+2,{net,prefix+'_5V'}),(r+3,{net,'GND'})]:assert {p[1] for p in by[f'R{ref}']['pins'].values()}==nets
  rb,rpd,rpu,rline=[resistance(f'R{i}') for i in range(r,r+4)]
  for target,vlogic in [(4.75,3.135),(5.0,3.3),(5.25,3.465)]:
   for capacitance in [100,500,1000]:
    ident=f'{net}_{target}_{capacitance}'
    hi=target*rline/(rline+rpu)
    netlist=f'''Rev D {ident}: nominal resistor values, 25 C. No actual firmware/host model.
.include "{args.cache.resolve()/'2N3904.lib'}"
.include "{args.cache.resolve()/'CD4050B-local.lib'}"
.temp 25
Vtarget target 0 {target}
Vlogic vcc 0 {vlogic}
* GPIO stimulus, 30 ohm assumed source resistance. Not an RP2040 transistor model.
Vdrive stimulus 0 PULSE(0 {vlogic} 10u 100n 100n 20u 100u)
Rgpio stimulus drive 30
Rb drive base {rb}
Rpd base 0 {rpd}
Qpull line base 0 Q2n3904
Rpu target line {rpu}
Rline line 0 {rline}
* Assumed external cable/connector/probe capacitance; CD4050 input capacitance is in its model.
Ccable line 0 {capacitance}p
Xbuf sense line vcc 0 CD4050B
Csense sense 0 10p
* Host is only an ideal low-side switch, 10 ohm on resistance, with no extra host pullup.
Vhost host 0 PULSE(0 3.3 55u 100n 100n 15u 100u)
Shost line 0 host 0 host_switch
.model host_switch SW(Ron=10 Roff=1e12 Vt=1.65 Vh=0)
.control
set wr_singlescale
set wr_vecnames
tran 50n 100u
meas tran idle_line find v(line) at=5u
meas tran driven_line find v(line) at=20u
meas tran host_line find v(line) at=60u
meas tran idle_sense find v(sense) at=5u
meas tran driven_sense find v(sense) at=20u
meas tran host_sense find v(sense) at=60u
meas tran release_10_90 trig v(line) val={.1*hi} rise=1 td=29u targ v(line) val={.9*hi} rise=1 td=29u
meas tran base_drive find v(base) at=20u
wrdata waveform.txt v(stimulus) v(host) v(line) v(sense)
quit
.endc
.end
'''
    m=run_netlist(netlist,ident)
    assert all(k in m for k in ['idle_line','driven_line','host_line','idle_sense','driven_sense','host_sense','release_10_90','base_drive']),ident
    # These are exploratory acceptance levels, not a full PS/2 compliance specification.
    assert m['idle_line']>4 and -.05<m['driven_line']<.4 and -.05<m['host_line']<.4,ident
    assert m['idle_sense']>vlogic-.1 and abs(m['driven_sense'])<.1 and abs(m['host_sense'])<.1,ident
    m['gpio_current_ma']=(vlogic-m['base_drive'])/(rb+30)*1000
    rows.append(dict(channel=net,target_v=target,logic_v=vlogic,external_cap_pf=capacitance,**m))
    if channel==0 and target==5 and capacitance==500:
     first_wave=(work/'waveform.txt').read_text()
     # Portable example for manual use: copy downloaded/local models beside this deck.
     portable=netlist.replace(str(args.cache.resolve())+'/', 'models/')
     (HERE/'ps2-example.cir').write_text(portable)
results={'ngspice':subprocess.check_output([args.ngspice,'--version'],text=True).splitlines()[1].strip(),'cases':rows,'model_sources':[dict(filename=f,url=u,sha256=h) for f,u,h,_ in models],'scope':'Exploratory PS/2 pull-down and nominal buffer model at 25 C. No full-system simulation.','local_cd4050_changes':['AND=1 and NAND=0 to correct known inversion bug','VT renamed LC_INPUT_VT for ngspice compatibility']}
(HERE/'results.json').write_text(json.dumps(results,indent=2)+'\n')
with (HERE/'results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(HERE/'waveform.txt').write_text('\n'.join(line.rstrip() for line in first_wave.splitlines())+'\n')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
wave=np.loadtxt(io.StringIO(first_wave),skiprows=1)
fig,axes=plt.subplots(3,1,figsize=(10,7),sharex=True,layout='constrained')
axes[0].plot(wave[:,0]*1e6,wave[:,1],label='RP2040 drive stimulus');axes[0].plot(wave[:,0]*1e6,wave[:,2],'--',label='Host pull-low stimulus');axes[0].legend(loc='upper right')
axes[1].plot(wave[:,0]*1e6,wave[:,3],color='#ab3e2a');axes[1].set_title('PS/2 cable voltage: 5 V reference, 500 pF assumed external capacitance')
axes[2].plot(wave[:,0]*1e6,wave[:,4],color='#176f50');axes[2].set_title('Sense voltage: locally corrected nominal CD4050 model at 3.3 V')
for a in axes:a.set_ylabel('Volts');a.grid(alpha=.25)
axes[-1].set_xlabel('Time (microseconds)')
fig.suptitle('Rev D exploratory SPICE study — not firmware or hardware validation')
fig.savefig(HERE/'ps2-waveform.png',dpi=160);plt.close(fig)
summary=f'''36 / 36 exploratory cases met the stated static voltage checks.
Highest simulated driven cable LOW (model artifact; see README): {max(r['driven_line'] for r in rows):.4f} V
Min released cable HIGH: {min(r['idle_line'] for r in rows):.4f} V
Max host-held cable LOW: {max(r['host_line'] for r in rows):.4f} V
GPIO drive current range: {min(r['gpio_current_ma'] for r in rows):.3f}–{max(r['gpio_current_ma'] for r in rows):.3f} mA
Cable 10–90% release rise time: {min(r['release_10_90'] for r in rows)*1e6:.3f}–{max(r['release_10_90'] for r in rows)*1e6:.3f} microseconds
Scope: four channels; three paired supplies; 100/500/1000 pF external capacitance; 25 C; nominal resistors.
No USB host, firmware, power startup/sequencing, chip temperature corners, PCB parasitic extraction or actual X16 simulation.
Model caveat: the 2N3904 model predicts a small negative driven LOW (~-14 to -15 mV); this is not a validated physical voltage.
CD4050 is a locally corrected behavioral model; its 3.3 V timing/drive strength is not qualified by this study.
'''
(HERE/'summary.txt').write_text(summary);print(summary)
