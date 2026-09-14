"""Generate the BOM and breadboard tables from the same circuit as the CAD."""
import csv
from collections import defaultdict
from design import ROOT,PARTS
with (ROOT/'bom.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Reference','Part / value','Through-hole footprint','Function','Assembly notes'])
 for p in PARTS:w.writerow([p['ref'],p['value'],p['footprint'].split(':')[1],p['group'],p['notes']])
groups=defaultdict(list);nets=defaultdict(list)
for p in PARTS:
 groups[p['value'],p['footprint'].split(':')[1]].append(p['ref'])
 for pin,(_,net) in p['pins'].items():
  if net:nets[net].append(f"{p['ref']}.{pin}")
with (ROOT/'bom-grouped.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Quantity','Part / value','Through-hole footprint','References'])
 for (value,fp),refs in groups.items():w.writerow([len(refs),value,fp,' '.join(refs)])
with (ROOT/'breadboard-wiring.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Component','Value','Physical pin','Pin name','Connect to net','Section'])
 for p in PARTS:
  for pin,(name,net) in sorted(p['pins'].items(),key=lambda x:int(x[0])):w.writerow([p['ref'],p['value'],pin,name,net or 'NO CONNECTION',p['group']])
with (ROOT/'net-connections.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Net','Connect these component pins together'])
 for net,refs in sorted(nets.items()):w.writerow([net,'; '.join(refs)])
with (ROOT/'placement.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Reference','Part','X mm','Y mm','Rotation degrees'])
 for p in PARTS:w.writerow([p['ref'],p['value'],p['x'],p['y'],p['rotation']])
print('Wrote BOM, per-pin wiring, per-net wiring and placement tables.')

# Test contacts include dedicated THT holes and existing USB resistor pads.
with (ROOT/'test-points.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['Probe location','Net','Access type'])
 for p in PARTS:
  if p['ref'].startswith('TP'):w.writerow([p['ref']+'.1',p['pins']['1'][1],'Dedicated plated through-hole; optional pin'])
 for ref in ['R3','R4','R8','R9']:
  p=next(p for p in PARTS if p['ref']==ref);w.writerow([ref+'.1',p['pins']['1'][1],'Existing USB data resistor pad; no added stub'])

# Root breadboard attachments, derived from the active Rev D parts.
PROJECT=ROOT.parent.parent
keyboard={'M1','J1','F1','JP1','U1','U2','J2','D1','Q1','Q2','J4',
 *[f'C{i}' for i in range(1,7)],*[f'R{i}' for i in range(1,6)],*[f'R{i}' for i in range(11,19)]}
electrical=[p for p in PARTS if not p['ref'].startswith(('H','TP'))]
assert keyboard <= {p['ref'] for p in electrical}
category=defaultdict(list)
for p in electrical:category[p['value'],p['footprint'].split(':')[1]].append(p)
header=['Keyboard first qty','Add mouse qty','Full qty','Part / value','References','Package / footprint','Breadboard description']
def description(value):
 names={'5V INPUT / GND':'Two-contact 5 V power connection','1.5A fast 5x20':'1.5 A fast fuse, 5×20 mm','REMOVE FOR PC USB':'Removable module-power jumper','RP2040-Zero SOCKETS':'RP2040-Zero module on headers','USB 1':'USB-A receptacle, keyboard','USB 2':'USB-A receptacle, mouse','KBD SDS-70J':'7-pin DIN socket, keyboard (SDS-70J for PCB)','MOUSE SDS-70J':'7-pin DIN socket, mouse (SDS-70J for PCB)','TPS2042P':'TPS2042P dual power switch, DIP-8','CD4050BE':'CD4050BE buffer, DIP-16','2N3904':'2N3904 transistor, TO-92','RED FAULT':'Red LED, 3 mm','100nF':'100 nF leaded ceramic capacitor'}
 if value in names:return names[value]
 if value.endswith('R'):return value[:-1]+' Ω resistor'
 if value.endswith('k'):return value[:-1]+' kΩ resistor'
 if 'uF' in value:return value.replace('uF',' µF /').replace('10V','10 V')+' electrolytic capacitor'
 return value
rootrows=[]
for (value,footprint),objs in category.items():
 initial=sum(p['ref'] in keyboard for p in objs)
 rootrows.append([initial,len(objs)-initial,len(objs),value,' '.join(p['ref'] for p in objs),footprint,description(value)])
with (PROJECT/'BREADBOARD-PARTS.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(header);w.writerows(rootrows)
(PROJECT/'BREADBOARD-WIRING.csv').write_bytes((ROOT/'breadboard-wiring.csv').read_bytes())
guide=PROJECT/'BREADBOARD.md'
if guide.exists():
 s=guide.read_text();a='<!-- BEGIN GENERATED BREADBOARD PARTS -->';z='<!-- END GENERATED BREADBOARD PARTS -->'
 before,tail=s.split(a);_,after=tail.split(z)
 table='| Keyboard first | Add mouse | Full total | Part / value | References |\n|---:|---:|---:|---|---|\n'
 for row in rootrows:table+='| '+' | '.join(str(v) for v in [*row[:3],row[6],row[4]])+' |\n'
 guide.write_text(before+a+'\n'+table+z+after)
print('Updated root breadboard parts, full wiring CSV and inline quantities.')
