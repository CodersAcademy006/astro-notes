# usage: python3 tools/build.py <cfg.json>   cfg: vid,title,sub,desc,len,sections_dir,out,points[[bold,rest]],puts[[before_html,diagram_key]],diagrams_module
import re,sys,json,importlib.util,os
cfg=json.load(open(sys.argv[1])); here=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('dg',os.path.join(here,cfg['diagrams_module'])); dg=importlib.util.module_from_spec(spec); sys.path.insert(0,here); spec.loader.exec_module(dg)
D=dg.D; vid=cfg['vid']; sd=os.path.join(here,cfg['sections_dir'])
body=''.join(open(os.path.join(sd,f)).read() for f in sorted(os.listdir(sd)) if f.endswith('.html'))
for before,key in cfg['puts']:
    assert before in body,before; body=body.replace(before,D[key]+before,1)
def ts(m):
    h,mi,s=map(int,m.group(1).split(':')); return f'<a class="ts" href="https://www.youtube.com/watch?v={vid}&amp;t={h*3600+mi*60+s}s">{m.group(1)}</a>'
body=re.sub(r'\{\{t:(\d\d:\d\d:\d\d)\}\}',ts,body)
secs=re.findall(r'<section id="([^"]+)">\s*<h2>(.*?)</h2>',body,re.S)
toc=''.join(f'<div><a href="#{i}">{re.sub(r"<a.*?</a>","",t).strip()}</a></div>' for i,t in secs)
pts=''.join(f'<li><div><b>{b}</b> {r}</div></li>' for b,r in cfg['points'])
h=open(os.path.join(here,'template_head.html')).read()
for k,v in dict(TITLE=cfg['title'],SUB=cfg['sub'],DESC=cfg['desc'],VID=vid,LEN=cfg['len'],POINTS=pts,TOC=toc,BODY=body,END='').items(): h=h.replace(f'@@{k}@@',v)
open(cfg['out'],'w').write(h); print(len(secs),'sections',len(h),'bytes')
