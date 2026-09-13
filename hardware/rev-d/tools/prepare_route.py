from pathlib import Path
import pcbnew as p
from design import ROOT
CAD=ROOT/'kicad';REV=ROOT/'review';b=p.LoadBoard(str(CAD/'link-commander.kicad_pcb'))
p.WriteDRCReport(b,str(REV/'placement-drc.txt'),p.EDA_UNITS_MILLIMETRES,False)
p.ExportSpecctraDSN(b,str(REV/'link-commander.dsn'))
f=REV/'link-commander.dsn';text=f.read_text()
settings='(autoroute_settings (fanout off) (autoroute on) (postroute on) (vias on) (via_costs 50) (plane_via_costs 5) (start_ripup_costs 100) (start_pass_no 1) '
for name,direction in [('F.Cu','horizontal'),('B.Cu','vertical')]:settings+=f'(layer_rule {name} (active on) (preferred_direction {direction}) (preferred_direction_trace_costs 1) (against_preferred_direction_trace_costs 2)) '
text=text.replace('(boundary',settings+')\n    (boundary',1);f.write_text(text)
print('Exported two-layer router input with project net widths.')
