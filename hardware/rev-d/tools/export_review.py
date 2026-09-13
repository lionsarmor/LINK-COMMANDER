from pathlib import Path
import pcbnew as p
from design import ROOT
CAD=ROOT/'kicad';REV=ROOT/'review'
b=p.LoadBoard(str(CAD/'link-commander.kicad_pcb'))
# Plot useful review layers. SVG output is scalable and keeps exact dimensions.
plot=p.PLOT_CONTROLLER(b);opt=plot.GetPlotOptions();opt.SetOutputDirectory(str(REV));opt.SetPlotFrameRef(False);opt.SetAutoScale(False);opt.SetScale(1);opt.SetMirror(False);opt.SetPlotReference(True);opt.SetPlotValue(False)
for layer,name in [(p.F_Cu,'front-copper'),(p.B_Cu,'back-copper'),(p.F_SilkS,'assembly'),(p.Edge_Cuts,'outline')]:
 plot.SetLayer(layer);plot.OpenPlotfile(name,p.PLOT_FORMAT_SVG,name);plot.PlotLayer();plot.ClosePlot()
print('Exported review layers from the saved board without modifying it.')
