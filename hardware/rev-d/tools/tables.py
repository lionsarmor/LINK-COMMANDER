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
