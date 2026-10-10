import re,sys
d='/private/tmp/claude-501/-Users-srijanupadhyay/7ac12395-f8f2-4d1d-b7fa-d78ecdfc783b/scratchpad/'
vid='VNIwRnEEWrs'
body=''.join(open(d+f'p{i}.html').read() for i in range(1,7))
def ts(m):
    h,mi,s=map(int,m.group(1).split(':')); t=h*3600+mi*60+s
    return f'<a class="ts" href="https://www.youtube.com/watch?v={vid}&amp;t={t}s">{m.group(1)}</a>'
import sys as _s; _s.path.insert(0,d)
from diagrams import D
def put(before,key,after=False):
    global body
    assert before in body,before
    body=body.replace(before,(before+D[key]) if after else (D[key]+before),1)
put('<h3>The eclipse lesson','seesaw')
put('<h3>Rahu dasha: the 18 year loop','window')
put('<h3>Barley (jau) in water','daan')
put('<div class="box">\n<h4>How to tie it</h4>','thread')
put('</section>\n\n<section id="threadjob">','compass')
put('<div class="tablewrap"><table>\n<tr><th>Situation</th>','start')
body=re.sub(r'\{\{t:(\d\d:\d\d:\d\d)\}\}',ts,body)
secs=re.findall(r'<section id="([^"]+)">\s*<h2>(.*?)</h2>',body,re.S)
toc=''.join(f'<div><a href="#{i}">{re.sub(r"<a.*?</a>","",t).strip()}</a></div>' for i,t in secs)
h=open(d+'head.html').read().replace('@@TOC@@',toc).replace('@@BODY@@',body).replace('@@END@@','')
open(sys.argv[1],'w').write(h)
print(len(secs),'sections',len(h),'bytes')
