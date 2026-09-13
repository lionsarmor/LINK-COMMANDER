import pcbnew as p,json
from design import ROOT
CAD=ROOT/'kicad';REV=ROOT/'review';b=p.LoadBoard(str(CAD/'link-commander.kicad_pcb'))
def v(x,y):return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
p.WriteDRCReport(b,str(REV/'pcb-drc.txt'),p.EDA_UNITS_MILLIMETRES,False)
# Check actual board pins against the circuit, not just the schematic.
parts=json.loads((ROOT/'circuit.json').read_text());byref={x['ref']:x for x in parts}
assert {fp.GetReference() for fp in b.GetFootprints() if not fp.GetReference().startswith('LOGO')}==set(byref)
for fp in b.GetFootprints():
 if fp.GetReference().startswith('LOGO'):
  assert not list(fp.Pads());continue
 obj=byref[fp.GetReference()]
 for pad in fp.Pads():
  assert pad.GetAttribute()!=p.PAD_ATTRIB_SMD,(fp.GetReference(),pad.GetNumber())
  if pad.GetNumber():assert pad.GetNetname()==(obj['pins'][pad.GetNumber()][1] or ''),(fp.GetReference(),pad.GetNumber())
assert b.GetCopperLayerCount()==2
assert all(t.GetLayer() in [p.F_Cu,p.B_Cu] for t in b.GetTracks())
assert len(b.Zones()) and all(z.GetLayer()==p.B_Cu and z.GetNetname()=='GND' for z in b.Zones())
print('PASS: every populated pad is through-hole and matches the canonical net assignment.')
print('PASS: two copper layers with a back-layer GND pour.')

report=(REV/'pcb-drc.txt').read_text()
assert 'Found 0 DRC violations' in report and 'Found 0 unconnected pads' in report and 'Found 0 Footprint errors' in report
print('PASS: saved board has zero DRC violations, zero unconnected pads and zero footprint errors.')
