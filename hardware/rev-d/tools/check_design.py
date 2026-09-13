"""Check the exported schematic and independent Rev D interface requirements."""
import json,csv,xml.etree.ElementTree as ET
from collections import defaultdict
from design import ROOT
parts=json.loads((ROOT/'circuit.json').read_text());by={p['ref']:p for p in parts}
expected=defaultdict(set)
for p in parts:
 for pin,(_,net) in p['pins'].items():
  if net:expected[net].add((p['ref'],pin))
actual={}
for net in ET.parse(ROOT/'review/schematic.xml').getroot().find('nets'):
 name=net.attrib['name'].removeprefix('/')
 if name.startswith('unconnected-'):continue
 actual[name]={(n.attrib['ref'],n.attrib['pin']) for n in net.findall('node')}
assert actual==dict(expected),'Exported schematic differs from canonical pin assignments'
assert len(by)==len(parts)
assert {p['value'] for p in parts if p['ref'].startswith('U')}=={'TPS2042P','CD4050BE'}
assert {p['ref'] for p in parts if p['ref'].startswith('U')}=={'U1','U2'}
assert not any('PAD' in n or 'CHAIN' in n or 'RUN_ENABLE' in n or 'OUTPUT_DISABLE' in n for n in expected)
assert set(by['M1']['pins'])=={str(i) for i in range(1,24)}
assert sum(net is not None for name,net in by['M1']['pins'].values())==15 # 12 GPIO + 3 supply pins
for pin in [5,6,7,8,17,18,19,20]:assert by['M1']['pins'][str(pin)][1] is None
for i in range(2):
 n=i+1;j=by[f'J{n+1}'];u=by['U1']
 assert j['pins']['2'][1]==f'USB{n}_DM' and j['pins']['3'][1]==f'USB{n}_DP'
 assert u['pins'][str(3+i)][1]=='GND' and u['value']=='TPS2042P'
 for k,suffix in [(0,'DP'),(1,'DM')]:
  assert any(p['value']=='22R' and {v[1] for v in p['pins'].values()}=={f'GP{2*i+k}',f'USB{n}_{suffix}'} for p in parts)
  assert any(p['value']=='15k' and {v[1] for v in p['pins'].values()}=={'GND',f'USB{n}_{suffix}'} for p in parts)
assert by['U1']['pins']['2'][1]=='5V_BOARD' and by['U1']['pins']['1'][1]=='GND'
for pin,net in [(7,'USB1_5V'),(6,'USB2_5V'),(8,'USB1_FAULT'),(5,'USB2_FAULT')]:assert by['U1']['pins'][str(pin)][1]==net
for i,(prefix,kind,inp,outp) in enumerate([('KBD','DATA',3,2),('KBD','CLOCK',5,4),('MOUSE','DATA',7,6),('MOUSE','CLOCK',9,10)]):
 line=f'{prefix}_{kind}';q=by[f'Q{i+1}'];r=11+4*i
 assert q['pins']=={'1':['E','GND'],'2':['B',f'Q{i+1}_B'],'3':['C',line]}
 assert by['U2']['pins'][str(inp)][1]==line
 assert by['U2']['pins'][str(outp)][1]==f'GP{9+2*i}' # non-inverted; no HC14
 assert {v[1] for v in by[f'R{r}']['pins'].values()}=={f'GP{8+2*i}',f'Q{i+1}_B'}
 assert {v[1] for v in by[f'R{r+2}']['pins'].values()}=={line,prefix+'_5V'}
 assert {v[1] for v in by[f'R{r+3}']['pins'].values()}=={line,'GND'}
assert by['U2']['pins']['1'][1]=='3V3' and by['U2']['pins']['8'][1]=='GND'
for p in [11,14]:assert by['U2']['pins'][str(p)][1]=='GND'
for p in [12,13,15,16]:assert by['U2']['pins'][str(p)][1] is None
for ref,prefix in [('J4','KBD'),('J5','MOUSE')]:
 assert [by[ref]['pins'][str(k)][1] for k in range(1,5)]==[prefix+'_5V','GND',prefix+'_DATA',prefix+'_CLOCK']
 assert all(by[ref]['pins'][str(k)][1] is None for k in range(5,9))
 assert all(r.startswith(('J','R','TP')) for r,pin in expected[prefix+'_5V'])
tps={p['ref']:p['pins']['1'][1] for p in parts if p['ref'].startswith('TP')}
assert len(tps)==26 and list(tps.values()).count('GND')==4
assert set(tps.values())=={'GND','5V_INPUT','5V_BOARD','5V_MODULE','3V3','USB1_5V','USB2_5V','KBD_5V','MOUSE_5V','USB1_FAULT','USB2_FAULT','KBD_DATA','KBD_CLOCK','MOUSE_DATA','MOUSE_CLOCK',*[f'GP{i}' for i in range(8,16)]}
rows=list(csv.DictReader((ROOT/'breadboard-wiring.csv').open()))
assert len(rows)==sum(len(p["pins"]) for p in parts)
for row in rows:
 pin=by[row['Component']]['pins'][row['Physical pin']]
 assert row['Pin name']==pin[0] and row['Connect to net']==(pin[1] or 'NO CONNECTION')
probe_rows=list(csv.DictReader((ROOT/'test-points.csv').open()))
assert len(probe_rows)==30
for row in probe_rows:
 ref,pin=row['Probe location'].split('.')
 assert by[ref]['pins'][pin][1]==row['Net']
for ref,net in [('R3','USB1_DP'),('R4','USB1_DM'),('R8','USB2_DP'),('R9','USB2_DM')]:assert by[ref]['pins']['1'][1]==net and by[ref]['pins']['2'][1]=='GND'
assert sum(int(r['Quantity']) for r in csv.DictReader((ROOT/'bom-grouped.csv').open()))==len(parts)
report=f'''PASS: {len(parts)} components including mounting holes; {len(expected)} named nets; {len(rows)} physical pin assignments.
PASS: 26 through-hole test contacts cover power, PS/2, USB faults and four ground locations.
PASS: exported schematic netlist exactly matches the canonical circuit.
PASS: only two USB inputs, two PS/2 DIN outputs; no gamepad circuitry or nets.
PASS: two DIP chips; header-only RP2040 with 12 used GPIOs and 8 unused GPIOs.
PASS: dual TPS2042P outputs/faults and both active-low enables are correct.
PASS: four USB 22-ohm series paths and four 15-kilohm host pulldowns.
PASS: four low-only transistor outputs and four non-inverting CD4050 sense paths.
PASS: CD4050 supply/unused pins and target-reference power separation.
NOT TESTED: physical fit, electrical timing/thresholds, USB signal integrity,
firmware operation, USB receiver compatibility, or actual X16 operation.
This is a netlist/structural check, not an electrical simulation or full ERC.
'''
(ROOT/'review/design-checks.txt').write_text(report);print(report)
