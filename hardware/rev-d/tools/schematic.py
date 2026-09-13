"""Single-sheet wired schematic, functional gate units and explicit package pins."""
from pathlib import Path
import json,uuid,math,re
from collections import defaultdict
from design import ROOT,PARTS
CAD=ROOT/'kicad';BY={p['ref']:p for p in PARTS};defs=defaultdict(list);nodes={};items=[];placed=set();used=set();wireids=set();directions={};wirelabels=defaultdict(list);wires=[];labels=set();label_records={};junction_points=set()
def uid(k):return str(uuid.uuid5(uuid.NAMESPACE_URL,'linkcommander/revd/'+k))
def q(s):return json.dumps(str(s),ensure_ascii=False)
def fx(size=1.3,extra=''):return f'(effects (font (size {size} {size})) {extra})'
def text(s,x,y,size=1.7):items.append(f'(text {q(s)} (at {x} {y} 0) {fx(size,"(justify left)")} (uuid {uid("text"+s+str(x)+str(y))}))')
def line(a,b,graphic=False):
 if a==b:return
 k=str(a)+str(b)+str(graphic)
 if k in wireids:return
 wireids.add(k)
 if not graphic:
  wires.append((a,b));return
 tag='polyline'
 items.append(f'({tag} (pts (xy {a[0]} {a[1]}) (xy {b[0]} {b[1]})) (stroke (width {0.3 if graphic else 0}) (type default))'+(' (fill (type none))' if graphic else '')+f' (uuid {uid(k)}))')
def section(title,x,y,w,h,note=''):
 for a,b in [((x,y),(x+w,y)),((x+w,y),(x+w,y+h)),((x+w,y+h),(x,y+h)),((x,y+h),(x,y))]:line(a,b,True)
 text(title,x+5,y+7,2.4)
 if note:text(note,x+5,y+14,1.4)
def label(net,xy,angle=0):
 if (net,xy) in labels:return
 labels.add((net,xy))
 label_records[(net,xy)]=f'(label {q(net)} (at {xy[0]} {xy[1]} {angle}) {fx(1.25,"(justify right bottom)" if angle==180 else "(justify left bottom)")} (uuid {uid("label"+net+str(xy))}))'
def key(ref,pin):return (ref,str(pin))
def W(a,b,*via):
 if isinstance(a,tuple) and isinstance(a[0],str):
  used.add(a);net=BY[a[0]]['pins'][a[1]][1];aa=nodes[a]
 else:aa=a;net=None
 if isinstance(b,tuple) and isinstance(b[0],str):
  used.add(b);bb=nodes[b];nb=BY[b[0]]['pins'][b[1]][1]
  if net:assert net==nb,(a,b,net,nb)
  net=nb
 else:bb=b
 for x,z in zip([aa,*via,bb],[*via,bb]):line(x,z)
 if net:
  seg=[(abs(end[0]-start[0]),min(start[0],end[0]),start[1]) for start,end in zip([aa,*via,bb],[*via,bb]) if start[1]==end[1]]
  if seg:
   length,xx,yy=max(seg);label(net,(round(xx+max(0,(length-len(net)*.7)/2),4),yy))
  else:label(net,aa)

def L(ref,pin,dx=-10,dy=0):
 a=key(ref,pin);used.add(a);pt=nodes[a];net=BY[ref]['pins'][str(pin)][1]
 if net is None:items.append(f'(no_connect (at {pt[0]} {pt[1]}) (uuid {uid("nc"+str(a))}))');return
 end=(pt[0]+dx,pt[1]+dy);line(pt,end);label(net,end,180 if dx<0 else 0)
def stroke():return '(stroke (width 0.25) (type default))'
def poly(pts):return '(polyline (pts '+''.join(f'(xy {x} {-y}) ' for x,y in pts)+') '+stroke()+' (fill (type none)))'
def rect(x0,y0,x1,y1):return f'(rectangle (start {x0} {-y0}) (end {x1} {-y1}) {stroke()} (fill (type background)))'
def circle(x,y,r):return f'(circle (center {x} {-y}) (radius {r}) {stroke()} (fill (type none)))'
def place(ref,x,y,kind='box',left=None,right=None,unit=1,rot=0,pitch=4,width=30,pins=None,caption=None):
 p=BY[ref];shape='';loc={}
 if kind in ('R','C','D','F','JP'):
  loc={'1':(-7.5,0,0),'2':(7.5,0,180)}
  if kind in ['R','F','JP']:shape=rect(-3,-1.3,3,1.3)+poly([(-7.5,0),(-3,0)])+poly([(3,0),(7.5,0)])
  elif kind=='C':shape=poly([(-.7,-3),(-.7,3)])+poly([(.7,-3),(.7,3)])+poly([(-7.5,0),(-.7,0)])+poly([(.7,0),(7.5,0)])
  else:shape=poly([(-2,-2),(-2,2)])+poly([(-2,0),(2,-2),(2,2),(-2,0)])+poly([(-7.5,0),(-2,0)])+poly([(2,0),(7.5,0)])+poly([(0,-3),(2,-5),(1,-5)])+poly([(3,-3),(5,-5),(4,-5)])
  if kind=='C' and 'uF' in p['value']:shape+=f'(text "+" (at -3 4 0) {fx(1.3)})'
  h=5
 elif kind=='Q':
  loc={'1':(0,7.5,90),'2':(-7.5,0,0),'3':(0,-7.5,270)}
  shape=poly([(-7.5,0),(-2,0)])+poly([(-2,-3),(-2,3)])+poly([(-2,-1.5),(0,-4),(0,-7.5)])+poly([(-2,1.5),(0,4),(0,7.5)])+poly([(-.2,2.3),(0,4),(-1.6,3.5)]);h=9
 elif kind in ['buffer','inv','and']:
  if kind=='and':
   a,b,c=pins;loc={str(a):(-8,-2.5,0),str(b):(-8,2.5,0),str(c):(8,0,180)}
   shape=rect(-4,-5,4,5)+f'(text "&" (at 0 0 0) {fx(2.5)})'+poly([(-8,-2.5),(-4,-2.5)])+poly([(-8,2.5),(-4,2.5)])+poly([(4,0),(8,0)])
  else:
   a,b=pins;loc={str(a):(-8,0,0),str(b):(8,0,180)}
   shape=poly([(-4,-4),(-4,4),(4,0),(-4,-4)])+poly([(-8,0),(-4,0)])+poly([(5.5 if kind=='inv' else 4,0),(8,0)])
   if kind=='inv':shape+=circle(4.7,0,.75)+poly([(-2,1),(-1,1),(-1,-1),(1,-1)])
  h=10
 else:
  left=left or [];right=right or [];h=max(len(left),len(right))*pitch+4;shape=rect(-width/2,-h/2,width/2,h/2)
  for side,seq in [(-1,left),(1,right)]:
   for i,n in enumerate(seq):loc[str(n)]=(side*(width/2+5),(i-(len(seq)-1)/2)*pitch,0 if side==-1 else 180)
  if ref.startswith('RN'):
   ys=[loc[str(n)][1] for n in range(2,10)]
   shape+=poly([(-width/2,0),(-8,0)])+poly([(-8,min(ys)),(-8,max(ys))])
   for yy in ys:shape+=poly([(-8,yy),(-4,yy)])+rect(-4,yy-.7,4,yy+.7)+poly([(4,yy),(width/2,yy)])
  # Label the body function instead of depending on cryptic part markings.
  if caption:shape+=f'(text {q(caption)} (at 0 0 0) {fx(1.2)})'
 def rotate(xx,yy):
  r=math.radians(rot);return (round(x+xx*math.cos(r)-yy*math.sin(r),4),round(y+xx*math.sin(r)+yy*math.cos(r),4))
 libpins=''
 for n,(xx,yy,ang) in loc.items():
  assert n in p['pins'],(ref,n)
  nm,net=p['pins'][n];length=5 if kind=='box' else 0
  libpins+=f'(pin passive line (at {xx} {-yy} {ang}) (length {length}) (name {q(nm)} {fx(1)}) (number {q(n)} {fx(1)}))'
  nodes[key(ref,n)]=rotate(xx,yy);directions[key(ref,n)]=-1 if xx<0 else 1
 defs[ref].append(f'(symbol "LC_{ref}_{unit}_1" {shape} {libpins})')
 sid=uid(ref+str(unit));display=ref+(chr(64+unit) if ref=='U2' else '')
 showval=p['value'];hidevalue=ref=='U2' and unit!=7
 if kind in ['R','C','D','F','JP']:
  tx,ty=(x,y-4) if rot==0 else(x+4,y-2);vx,vy=(x,y+4) if rot==0 else(x+4,y+2)
 elif kind=='Q':tx,ty=x+8,y-3;vx,vy=x+10,y+2
 else:tx,ty=x,y-h/2-3;vx,vy=x,y+h/2+3
 items.append(f'(symbol (lib_id "LC_{ref}") (at {x} {y} {-rot}) (unit {unit}) (in_bom yes) (on_board yes) (dnp no) (uuid {sid}) '+
 f'(property "Reference" {q(ref)} (at {tx} {ty} {rot}) {fx(1.7)}) '+
 f'(property "Value" {q(showval)} (at {vx} {vy} {rot}) {fx(1.5,"hide" if hidevalue else "")}) '+
 f'(property "Footprint" {q(p["footprint"])} (at {x} {y} 0) {fx(1,"hide")}) '+
 ''.join(f'(pin "{n}" (uuid {uid(ref+str(unit)+"pin"+n)}))' for n in loc)+
 f'(instances (project "link-commander" (path "/{uid("root")}" (reference "{ref}") (unit {unit})))))')
 placed.add(ref)
 return {n:nodes[key(ref,n)] for n in loc}
def R(ref,x,y,vertical=False):return place(ref,x,y,ref[0] if not ref.startswith('JP') else 'JP',rot=90 if vertical else 0)
def gate(ref,unit,x,y,kind,pins):place(ref,x,y,kind,unit=unit,pins=pins)
text('LINK COMMANDER / REV D / USB KEYBOARD + MOUSE TO PS/2',15,18,3.8)
text('USB receiver -> RP2040 firmware -> PS/2 lines -> custom DIN cable -> Commander X16',15,29,2)
section('1 / POWER',10,40,185,110,'Regulated 5 V only. Remove JP1 before connecting PC USB.')
place('J1',38,84,right=[1,2],width=15);R('F1',85,74);R('JP1',148,74)
W(key('J1',1),key('F1',1),(57,82),(57,74));W(key('F1',2),key('JP1',1));L('J1',2,0,8);L('JP1',2,18)
R('C1',112,110,True);W(key('F1',2),key('C1',1),(112,74));L('C1',2,0,8)
text('J1: 5 V / 2 A supply\nF1: 1.5 A fast fuse\nUSB ports turn on with external power.\nX16 +5 V is used only for PS/2 pullups.',20,131,1.6)
section('2 / REMOVABLE RP2040-ZERO',205,40,185,110,'Plug-in module. No wires to underside pads.')
place('M1',305,101,left=[23,22,21,17,18,19,20],right=list(range(1,17)),width=35,pitch=4)
text('GP0/1: USB keyboard D+/D-\nGP2/3: USB mouse D+/D-\nGP8-15: PS/2 drive and sense',215,133,1.6)
section('3 / 3.3 V LOGIC POWER',400,40,190,110,'U2A-F are six buffers inside ONE CD4050BE chip.')
place('U2',441,81,left=[1,8],right=[13,16],unit=7,width=22)
R('C3',436,118,True);R('C2',480,118,True)
W(key('U2',1),key('C3',1),(420,79),(420,104),(436,104))
W(key('U2',8),key('C3',2),(415,83),(415,130),(436,130))
W(key('C3',1),key('C2',1));W(key('C3',2),key('C2',2))
gate('U2',5,548,87,'buffer',(11,12));gate('U2',6,548,121,'buffer',(14,15))
text('Unused inputs go to GND.\nUnused outputs stay open.',510,141,1.5)
for i in range(2):
 x=10+300*i;n=i+1;r=1+5*i;u='U1';j='J'+str(n+1)
 section(f'{4+i} / USB '+['KEYBOARD','MOUSE'][i],x,160,280,110,'Use a supported USB device or its own 2.4 GHz USB receiver.')
 if i==0:place(u,x+48,207,left=[2,3,4,1],right=[7,8,6,5],width=24,pitch=5)
 else:text('Power from U1 pin 6\nFault from U1 pin 5\nBoth channels are inside U1.',x+22,198,1.6)
 place(j,x+248,224,left=[1,2,3,4,5],width=20,pitch=8)
 R('R'+str(r),x+135,224);R('R'+str(r+1),x+135,210)
 W(key('R'+str(r),2),key(j,3));W(key('R'+str(r+1),2),key(j,2),(x+156,210),(x+156,216))
 for rr,xx,pin in [(r+2,x+177,3),(r+3,x+206,2)]:
  R('R'+str(rr),xx,247,True);W(key(j,pin),key('R'+str(rr),1),(xx,nodes[key(j,pin)][1]));L('R'+str(rr),2,0,6)
 if i==0:W(key(u,7),key(j,1),(x+81,199.5),(x+227,199.5),(x+227,208))
 R('D'+str(n),x+90,225);R('R'+str(r+4),x+90,235)
 L('D'+str(n),1,-12)
 W(key('D'+str(n),2),key('R'+str(r+4),2),(x+106,225),(x+106,235))
 if i==0:R('C4',x+25,251,True)
 cap1='C5' if i==0 else 'C7';cap2='C6' if i==0 else 'C8'
 R(cap1,x+58,251,True);R(cap2,x+130,251,True)
 # Caps on the receiver supply share a visible 5 V/GND pair.
 W(key(cap1,1),key(cap2,1),(x+58,242),(x+130,242))
 W(key(cap1,2),key(cap2,2),(x+58,264),(x+130,264))
for k,prefix in enumerate(['KBD','MOUSE']):
 x=10+300*k;j='J'+str(4+k)
 section(f'{6+k} / '+['KEYBOARD','MOUSE'][k]+' PS/2 OUTPUT',x,280,280,132,'Read = cable level. Drive HIGH pulls the line LOW.')
 place(j,x+249,355,left=[1,2,3,4],right=[5,6,7,8],width=22,pitch=6)
 for ch in range(2):
  i=2*k+ch;r=11+4*i;y=330+50*ch;qref='Q'+str(i+1);cp=[(3,2),(5,4),(7,6),(9,10)][i]
  place(qref,x+65,y,'Q');R('R'+str(r),x+30,y);R('R'+str(r+1),x+47,y+12,True)
  R('R'+str(r+2),x+105,y-26,True);R('R'+str(r+3),x+120,y+10,True)
  gate('U2',i+1,x+158,y-7.5,'buffer',cp)
  W(key('R'+str(r),2),key(qref,2));W(key(qref,2),key('R'+str(r+1),1),(x+47,y))
  W(key(qref,3),key('U2',cp[0]))
  W(key('R'+str(r+2),2),(x+105,y-7.5));W(key('R'+str(r+3),1),(x+120,y-7.5))
  L('R'+str(r+2),1,0,-4);L('R'+str(r+3),2,0,3);L(qref,1,0,13);L('R'+str(r+1),2,0,3);L('R'+str(r),1,-10);L('U2',cp[1],15)
  # Physically wire each cable line to the DIN socket, bypassing the sense buffer.
  if ch==0:W(key(qref,3),key(j,3),(x+65,y-7.5),(x+115,y-7.5),(x+115,y-18),(x+211,y-18),(x+211,358))
  else:W(key(qref,3),key(j,4),(x+65,y-7.5),(x+115,y-7.5),(x+115,406),(x+221,406),(x+221,364))
  text(['DATA','CLOCK'][ch],x+184,y-15,1.8)
text('HOW TO READ: dots join wires; crossing wires without dots do not join. Equal net names are connected.',15,424,1.8)
text('Q = transistor. R = resistor. C = capacitor. U = chip. M1 pin numbers are carrier numbers; use GP labels on the module.',15,433,1.6)
text('Prototype: firmware and bench tests are required before use with the X16. Cable wiring is in breadboard.md.',15,441,1.6)
# Label remaining boundary connections. Long internal signal paths are wires above.
for ref in sorted(placed):
 for pin,(_,net) in BY[ref]['pins'].items():
  a=key(ref,pin)
  assert a in nodes,('pin not drawn',a)
  if a not in used:
   # Short unobtrusive labels: pins on left/right package edges face away.
   xy=nodes[a]
   L(ref,pin,8*directions[a])
assert placed=={p['ref'] for p in PARTS if p['pins']},set(BY)-placed
# Split electrical wires at tees, pin ends and label anchors so KiCad's
# stored topology is identical to the drawn circuit, including visible dots.
points=junction_points|set(nodes.values())|{xy for net,xy in labels}|{pt for ab in wires for pt in ab}
parent={pt:pt for pt in points};drawn_segments=set();adj=defaultdict(set)
def find(a):
 while parent[a]!=a:
  parent[a]=parent[parent[a]];a=parent[a]
 return a
for a,b in wires:
 dx,dy=b[0]-a[0],b[1]-a[1]
 on=[pt for pt in points if abs((pt[0]-a[0])*dy-(pt[1]-a[1])*dx)<1e-5 and min(a[0],b[0])-1e-5<=pt[0]<=max(a[0],b[0])+1e-5 and min(a[1],b[1])-1e-5<=pt[1]<=max(a[1],b[1])+1e-5]
 on.sort(key=lambda pt:(pt[0]-a[0])*dx+(pt[1]-a[1])*dy)
 for aa,bb in zip(on,on[1:]):
  if aa!=bb:
   parent[find(aa)]=find(bb);adj[aa].add(bb);adj[bb].add(aa)
   seg=tuple(sorted([aa,bb]))
   if seg in drawn_segments:continue
   drawn_segments.add(seg)
   items.append(f'(wire (pts (xy {aa[0]} {aa[1]}) (xy {bb[0]} {bb[1]})) (stroke (width 0) (type default)) (uuid {uid("split"+str(aa)+str(bb))}))')
for pt,neighbors in adj.items():
 if len(neighbors)>=3:items.append(f'(junction (at {pt[0]} {pt[1]}) (diameter 0.8) (color 0 0 0 0) (uuid {uid("junction"+str(pt))}))')
# Keep one readable net name per physically wired island. Repeated names
# remain on disconnected section boundaries, where they are necessary.
chosen={}
for (net,xy),record in label_records.items():
 group=(net,find(xy));score=min(math.hypot(xy[0]-pt[0],xy[1]-pt[1]) for pt in nodes.values())
 if group not in chosen or score>chosen[group][0]:chosen[group]=(score,record)
items.extend(record for score,record in chosen.values())
lib=''
for ref,units in defs.items():
 hide=' hide' if not (ref.startswith('U') or ref=='M1' or ref.startswith('J')) else ''
 lib+=f'(symbol "LC_{ref}" (pin_names (offset 0.8){hide}) (in_bom yes) (on_board yes) (property "Reference" "{ref}" (at 0 0 0) {fx()}) (property "Value" {q(BY[ref]["value"])} (at 0 0 0) {fx()}) '+''.join(units)+')\n'
s=f'(kicad_sch (version 20230121) (generator eeschema) (uuid {uid("root")}) (paper "User" 620 455) (title_block (title "LINK COMMANDER — Rev D keyboard and mouse") (date "2026-09-13") (rev "D / PROTOTYPE") (company "RODDY")) (lib_symbols {lib}) '+''.join(items)+' (sheet_instances (path "/" (page "1"))))\n'
s=re.sub(r'\(property "(Reference|Value|Footprint)" ("(?:\\.|[^"\\])*")',lambda m:m[0]+f' (id {dict(Reference=0,Value=1,Footprint=2)[m[1]]})',s).replace(' -90)', ' 270)')
(CAD/'link-commander.kicad_sch').write_text(s)
print(f'One page: {len(placed)} components; {len(nodes)} physical pins; {len(wireids)} wire/section segments.')
