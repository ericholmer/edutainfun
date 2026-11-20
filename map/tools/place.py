import re,json,math,sys
# Usage: python3 place.py index.html states.js   (needs: pip install shapely)
# For each state, finds the center of the largest sticker-shaped box inside its borders.
from shapely.geometry import Polygon, MultiPolygon, box, Point
from shapely.prepared import prep
src=open(sys.argv[1]).read()
line=re.search(r'const STATES = (\[.*?\]);\n',src)
D=json.loads(line.group(1))
A=3.8   # sticker width / height for a typical 9-letter name
out={}
for s in D:
    if s['co']>=0 or s['ab']=='HI': continue
    rings=[ [tuple(map(float,p.split(','))) for p in re.findall(r'-?[\d.]+,-?[\d.]+',seg)] for seg in s['d'].split('M') if seg.strip()]
    polys=[Polygon(r).buffer(0) for r in rings if len(r)>=3]
    g=max(MultiPolygon([q for p in polys for q in (p.geoms if hasattr(p,'geoms') else [p])]).geoms,key=lambda p:p.area)
    P=prep(g); minx,miny,maxx,maxy=g.bounds
    def fit(cx,cy):
        if not P.contains(Point(cx,cy)): return 0
        lo,hi=0,(maxy-miny)
        for _ in range(14):
            h=(lo+hi)/2
            if P.contains(box(cx-A*h/2,cy-h/2,cx+A*h/2,cy+h/2)): lo=h
            else: hi=h
        return lo
    step=max(1.0,(maxx-minx)/60)
    cands=[]
    y=miny
    while y<=maxy:
        x=minx
        while x<=maxx:
            h=fit(x,y)
            if h>0: cands.append((h,x,y))
            x+=step
        y+=step
    best=max(c[0] for c in cands)
    top=[c for c in cands if c[0]>=best*0.94]
    cx=sum(c[1] for c in top)/len(top); cy=sum(c[2] for c in top)/len(top)
    h=fit(cx,cy)
    if h<best*0.85: _,cx,cy=max(top)  ; h=fit(cx,cy) if fit(cx,cy) else best
    out[s['ab']]=dict(lx=round(cx,1),ly=round(cy,1),sw=round(A*h*0.86,1),old=(s['lx'],s['ly']))
for ab,v in sorted(out.items()): print(ab,v)
for s in D:
    if s['ab'] in out: s['lx'],s['ly'],s['sw']=out[s['ab']]['lx'],out[s['ab']]['ly'],out[s['ab']]['sw']
open(sys.argv[2],'w').write('const STATES = '+json.dumps(D,separators=(',',':'))+';')
