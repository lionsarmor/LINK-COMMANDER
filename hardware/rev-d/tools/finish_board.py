from pathlib import Path
import re,json
import pcbnew as p
from design import ROOT
CAD=ROOT/'kicad';REV=ROOT/'review'
b=p.LoadBoard(str(CAD/'link-commander.kicad_pcb'))
# KiCad 7's session importer requires an open GUI board. Parse the limited
# Specctra route output directly, validating coordinates/layers/via geometry.
def parse_sexp(text):
 stack=[];result=None
 for token in re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',text):
  if token=='(':stack.append([])
  elif token==')':
   done=stack.pop()
   if stack:stack[-1].append(done)
   else:result=done
  else:stack[-1].append(json.loads(token) if token.startswith('"') else token)
 assert not stack
 return result
session=parse_sexp((REV/'link-commander.ses').read_text())
routes=next(x for x in session if isinstance(x,list) and x[0]=='routes')
assert ['resolution','um','10'] in routes
network=next(x for x in routes if isinstance(x,list) and x[0]=='network_out')
layer_ids={'F.Cu':p.F_Cu,'In1.Cu':p.In1_Cu,'In2.Cu':p.In2_Cu,'B.Cu':p.B_Cu}
def xy(x,y):return p.VECTOR2I(round(float(x)*100),round(-float(y)*100))
assert not list(b.GetTracks()), 'Run only against the unrouted board.'
for net in network[1:]:
 assert net[0]=='net';netobj=b.FindNet(net[1]);assert netobj is not None
 for item in net[2:]:
  if item[0]=='wire':
   path=item[1];assert path[0]=='path';assert path[1] in ['F.Cu','B.Cu'], 'Unexpected signal layer'
   width=round(float(path[2])*100);pts=[xy(path[k],path[k+1]) for k in range(3,len(path),2)]
   for a,z in zip(pts,pts[1:]):
    if a==z:continue
    t=p.PCB_TRACK(b);t.SetStart(a);t.SetEnd(z);t.SetWidth(width);t.SetLayer(layer_ids[path[1]]);t.SetNet(netobj);b.Add(t)
  elif item[0]=='via':
   assert item[1]=='Via[0-1]_650:300_um',item[1]
   t=p.PCB_VIA(b);t.SetPosition(xy(item[2],item[3]));t.SetWidth(p.FromMM(.65));t.SetDrill(p.FromMM(.3));t.SetViaType(p.VIATYPE_THROUGH);t.SetLayerPair(p.F_Cu,p.B_Cu);t.SetNet(netobj);b.Add(t)
  else:raise ValueError(item[0])
# A back-layer ground pour surrounds the two-layer routes.
def v(x,y):return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
if not len(b.Zones()):
 z=p.ZONE(b);z.SetLayer(p.B_Cu);z.SetNet(b.FindNet('GND'));z.SetLocalClearance(p.FromMM(.25));z.SetPadConnection(p.ZONE_CONNECTION_THERMAL);z.SetThermalReliefGap(p.FromMM(.3));z.SetThermalReliefSpokeWidth(p.FromMM(.4));z.SetMinThickness(p.FromMM(.2));o=z.Outline();o.NewOutline()
 for x,y in [(10.4,10.4),(149.6,10.4),(149.6,89.6),(10.4,89.6)]:o.Append(int(p.FromMM(x)),int(p.FromMM(y)))
 b.Add(z)
b.BuildConnectivity();p.ZONE_FILLER(b).Fill(b.Zones());p.SaveBoard(str(CAD/'link-commander.kicad_pcb'),b)
b=p.LoadBoard(str(CAD/'link-commander.kicad_pcb'))
p.WriteDRCReport(b,str(REV/'pcb-drc.txt'),p.EDA_UNITS_MILLIMETRES,False)
# Plot useful review layers. SVG output is scalable and keeps exact dimensions.
plot=p.PLOT_CONTROLLER(b);opt=plot.GetPlotOptions();opt.SetOutputDirectory(str(REV));opt.SetPlotFrameRef(False);opt.SetAutoScale(False);opt.SetScale(1);opt.SetMirror(False);opt.SetPlotReference(True);opt.SetPlotValue(False)
for layer,name in [(p.F_Cu,'front-copper'),(p.B_Cu,'back-copper'),(p.F_SilkS,'assembly'),(p.Edge_Cuts,'outline')]:
 plot.SetLayer(layer);plot.OpenPlotfile(name,p.PLOT_FORMAT_SVG,name);plot.PlotLayer();plot.ClosePlot()
print('Imported route, refilled ground plane, wrote DRC and SVG review layers.')
