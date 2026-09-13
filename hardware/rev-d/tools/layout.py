"""Place Rev D, preserving the checked circuit. Replaces PCB with unrouted board."""
import json,os,math,shutil,uuid
from pathlib import Path
import pcbnew as p
from design import ROOT,PARTS
CAD=ROOT/'kicad';LIB=CAD/'LinkCommander.pretty'
def v(x,y):return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
by={a['ref']:a for a in PARTS}
def at(ref,x,y,rot=0):by[ref].update(x=x,y=y,rotation=rot)
# Two receiver sockets, a socketed module, and external 5 V input.
for i,x in enumerate([29,60]):
 at('J'+str(2+i),x,21,180)
 at('D'+str(1+i),x+11,50)
 at('R'+str(3+5*i),x-10,49);at('R'+str(4+5*i),x-10,54);at('R'+str(5+5*i),x+4,54)
at('U1',23,36);at('C4',34,36);at('C5',40,29);at('C6',40,39)
at('C7',67,29);at('C8',68,41)
at('M1',76,15)
for ref,yy in [('R1',18),('R2',23),('R6',28),('R7',33)]:at(ref,99,yy)
at('J1',138,17);at('F1',119,27);at('JP1',128,37);at('C1',141,43)
at('U2',100,37);at('C3',113,37);at('C2',88,50)
for i in range(4):
 x=17+32*i
 for k in range(4):at('R'+str(11+4*i+k),x+(k%2)*13,61+(k//2)*5)
 at('Q'+str(i+1),x+27,67,90)
at('J4',40,86,180);at('J5',111,86,180)
for ref,x,y in [('H1',15,35),('H2',115,15),('H3',15,85),('H4',145,85)]:at(ref,x,y)
b=p.BOARD();b.SetCopperLayerCount(2)
nets=sorted({x[1] for a in PARTS for x in a['pins'].values() if x[1]})
ns={}
for i,n in enumerate(nets,1):ns[n]=p.NETINFO_ITEM(b,n,i);b.Add(ns[n])
for a in PARTS:
 fp=p.FootprintLoad(str(LIB),a['footprint'].split(':')[1]);fp.SetReference(a['ref']);fp.SetValue(a['value']);fp.SetFPID(p.LIB_ID('LinkCommander',a['footprint'].split(':')[1]));fp.SetPosition(v(a['x'],a['y']));fp.SetOrientationDegrees(a['rotation'])
 path=p.KIID_PATH();path.push_back(p.KIID(str(uuid.uuid5(uuid.NAMESPACE_URL,'linkcommander/revd/root'))));path.push_back(p.KIID(str(uuid.uuid5(uuid.NAMESPACE_URL,'linkcommander/revd/'+a['ref']+'1'))));fp.SetPath(path)
 fp.Reference().SetTextSize(v(.85,.85));fp.Reference().SetTextThickness(p.FromMM(.13));fp.Value().SetVisible(False)
 if a['ref'].startswith('R') and not a['ref'].startswith('RN'):fp.Reference().SetPosition(v(a['x']+5.08,a['y']-2.15))
 if a['ref'].startswith('R') and not a['ref'].startswith('RN') and 1<=int(a['ref'][1:])<=26:fp.Reference().SetPosition(v(a['x']+5.08,a['y']))
 if a['ref'] in ['Q1','Q2','Q3','Q4']:fp.Reference().SetTextAngle(p.EDA_ANGLE(0,p.DEGREES_T));fp.Reference().SetPosition(v(a['x']+2.5,a['y']+4.5))
 if a['ref'].startswith('TP'):fp.Reference().SetTextSize(v(.8,.8));fp.Reference().SetTextThickness(p.FromMM(.12))
 if a['ref'] in ['TP13','TP14','TP17','TP18']:fp.Reference().SetPosition(v(a['x'],a['y']+1.7))
 if a['ref'].startswith('U'):fp.Reference().SetPosition(v(a['x']+3.81,a['y']+4));fp.Reference().SetTextSize(v(1,1))
 if a['ref']=='J1':fp.Reference().SetPosition(v(145,13))
 if a['ref'] in ['J2','J3']:fp.Reference().SetVisible(False)
 if a['ref'] in ['J4','J5']:fp.Reference().SetPosition(v(a['x'],83))
 for pad in fp.Pads():
  n=pad.GetNumber()
  if n and a['pins'][n][1]:pad.SetNet(ns[a['pins'][n][1]])
 b.Add(fp)
# Rounded 140 x 80 mm outline, R4 corners. Four straight edges and four arcs.
for a,z in [((14,10),(146,10)),((150,14),(150,86)),((146,90),(14,90)),((10,86),(10,14))]:
 e=p.PCB_SHAPE();e.SetShape(p.SHAPE_T_SEGMENT);e.SetStart(v(*a));e.SetEnd(v(*z));e.SetLayer(p.Edge_Cuts);e.SetWidth(p.FromMM(.05));b.Add(e)
for cx,cy,ang in [(146,14,-90),(146,86,0),(14,86,90),(14,14,180)]:
 pts=[v(cx+4*math.cos(math.radians(ang+t)),cy+4*math.sin(math.radians(ang+t))) for t in [0,45,90]]
 e=p.PCB_SHAPE();e.SetShape(p.SHAPE_T_ARC);e.SetArcGeometry(*pts);e.SetLayer(p.Edge_Cuts);e.SetWidth(p.FromMM(.05));b.Add(e)
def text(s,x,y,size=1):
 t=p.PCB_TEXT(b);t.SetText(s);t.SetPosition(v(x,y));t.SetLayer(p.F_SilkS);t.SetTextSize(v(size,size));t.SetTextThickness(p.FromMM(.15));b.Add(t)
for a in PARTS:
 if a['ref'].startswith('TP') and a['value']=='GND':text('GND',a['x'],a['y']+2,.8)
text('LINK COMMANDER',124,12,1.1)
text('REV D',135,57,.9)
text('USB1 D+',19,46.8,.8);text('USB1 D-',19,51.8,.8)
text('USB2 D+',50,46.8,.8);text('USB2 D-',50,51.8,.8)
text('JP1 OFF\nFOR PC USB',126,44,.8)
text('5V IN',138,12.5,.8)
text('+',138,22,.8);text('-',140.54,22,.8)
text('J2 USB KEYBOARD',25.5,25,.8);text('J3 USB MOUSE',56.5,25,.8)
text('KEYBOARD',40,80,1.1);text('MOUSE',111,80,1.1)
for name,x,y in [('2042',26.81,43),('CD4050',103.81,47)]:text(name,x,y,.8)
stock=Path(os.environ['KICAD_FOOTPRINT_DIR'])/'Symbol.pretty'
for ref,name,x,y in [('LOGO1','KiCad-Logo2_8mm_SilkScreen',77,81),('LOGO2','OSHW-Logo2_7.3x6mm_SilkScreen',132,80)]:
 shutil.copy2(stock/(name+'.kicad_mod'),LIB/(name+'.kicad_mod'))
 fp=p.FootprintLoad(str(LIB),name);fp.SetReference(ref);fp.SetFPID(p.LIB_ID('LinkCommander',name));fp.SetPosition(v(x,y));fp.Reference().SetVisible(False);fp.Value().SetVisible(False);b.Add(fp)
ds=b.GetDesignSettings();ds.m_MinClearance=p.FromMM(.20);ds.m_TrackMinWidth=p.FromMM(.25);ds.m_ViasMinSize=p.FromMM(.65);ds.m_MinThroughDrill=p.FromMM(.3)
p.SaveBoard(str(CAD/'link-commander.kicad_pcb'),b)
shutil.copy2(ROOT/'tools/project-template.json',CAD/'link-commander.kicad_pro')
(ROOT/'circuit.json').write_text(json.dumps(PARTS,indent=2)+'\n')
print('Placed 140 x 80 mm, R4 outline; module headers, all THT, two silk logos.')
