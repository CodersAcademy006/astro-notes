(function(){
'use strict';
var KEY='astroNotesRead';
function readSet(){try{return new Set(JSON.parse(localStorage.getItem(KEY)||'[]'))}catch(e){return new Set()}}
function writeSet(s){try{localStorage.setItem(KEY,JSON.stringify(Array.from(s)))}catch(e){}}

var style=document.createElement('style');
style.textContent=
'.readBtn,.readToggle{font:inherit;font-size:.72rem;font-weight:600;cursor:pointer;border-radius:999px;padding:3px 10px;border:1px solid var(--line);background:var(--bg);color:var(--mute)}'+
'.readBtn[aria-pressed="true"],.readToggle[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}'+
'.readBtn:active,.readToggle:active{transform:scale(.95)}'+
'a.card{position:relative;padding-right:92px}'+
'a.card .readBtn{position:absolute;top:14px;right:14px}'+
'a.card.is-read{opacity:.55}'+
'.controls{flex-wrap:wrap}'+
'.controls input[type=search]{font:inherit;font-size:.85rem;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 12px;flex:1;min-width:140px}'+
'.count{color:var(--mute);font-size:.8rem;white-space:nowrap}'+
'.readToggle{flex-shrink:0;margin-left:auto}'+
'.pageSearch{display:flex;align-items:center;gap:10px;margin:0 0 22px}'+
'.pageSearch input[type=search]{font:inherit;font-size:.9rem;color:var(--fg);background:var(--card);border:1px solid var(--line);border-radius:8px;padding:7px 12px;flex:1;min-width:0}'+
'.pageSearch .status{color:var(--mute);font-size:.8rem;white-space:nowrap}'+
'mark.hit{background:color-mix(in srgb,var(--accent) 25%,transparent);color:inherit;border-radius:3px;padding:0 1px}'+
'mark.hit.current{background:var(--accent);color:#fff}';
document.head.appendChild(style);

function setupPageSearch(main){
  var sub=main.querySelector('.sub');
  var bar=document.createElement('div');
  bar.className='pageSearch';
  bar.innerHTML='<input type="search" placeholder="Search this page" aria-label="Search this page"><span class="status"></span>';
  if(sub)sub.insertAdjacentElement('afterend',bar);else main.insertBefore(bar,main.firstChild);
  var input=bar.querySelector('input'),status=bar.querySelector('.status');
  var reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var marks=[],current=-1;

  function clearMarks(){
    main.querySelectorAll('mark.hit').forEach(function(m){m.replaceWith(document.createTextNode(m.textContent))});
    main.normalize();marks=[];current=-1;
  }
  function wrapMatches(q){
    var found=[];
    var walker=document.createTreeWalker(main,NodeFilter.SHOW_TEXT,{acceptNode:function(node){
      var p=node.parentNode;
      if(!p||p.nodeName==='SCRIPT'||p.nodeName==='STYLE'||p.closest('.pageSearch'))return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }});
    var nodes=[],n;
    while(n=walker.nextNode())nodes.push(n);
    var ql=q.toLowerCase();
    nodes.forEach(function(node){
      var text=node.nodeValue,lower=text.toLowerCase(),idx=lower.indexOf(ql);
      if(idx===-1)return;
      var frag=document.createDocumentFragment(),last=0;
      while(idx!==-1){
        frag.appendChild(document.createTextNode(text.slice(last,idx)));
        var mark=document.createElement('mark');
        mark.className='hit';mark.textContent=text.slice(idx,idx+q.length);
        frag.appendChild(mark);found.push(mark);
        last=idx+q.length;idx=lower.indexOf(ql,last);
      }
      frag.appendChild(document.createTextNode(text.slice(last)));
      node.parentNode.replaceChild(frag,node);
    });
    return found;
  }
  function goTo(i){
    if(!marks.length)return;
    if(current>=0)marks[current].classList.remove('current');
    current=(i+marks.length)%marks.length;
    marks[current].classList.add('current');
    marks[current].scrollIntoView({block:'center',behavior:reduceMotion?'auto':'smooth'});
    status.textContent=(current+1)+' of '+marks.length;
  }
  input.addEventListener('input',function(){
    clearMarks();
    var q=input.value.trim();
    if(!q){status.textContent='';return}
    marks=wrapMatches(q);
    if(!marks.length){status.textContent='No matches';return}
    goTo(0);
  });
  input.addEventListener('keydown',function(e){
    if(e.key==='Enter'){e.preventDefault();goTo(current+(e.shiftKey?-1:1))}
    else if(e.key==='Escape'){input.value='';clearMarks();status.textContent='';input.blur()}
  });
}

var cards=document.getElementById('cards');
if(cards){
  // index page: search filter + per-card read toggle
  var read=readSet();
  var list=Array.from(cards.children);
  var count=document.getElementById('readCount');

  function keyOf(a){return a.getAttribute('href')}
  function paint(a){
    var isRead=read.has(keyOf(a));
    a.classList.toggle('is-read',isRead);
    var btn=a.querySelector('.readBtn');
    btn.setAttribute('aria-pressed',String(isRead));
    btn.textContent=isRead?'Read':'Mark read';
  }
  function updateCount(){if(count)count.textContent=read.size+' of '+list.length+' read'}

  list.forEach(function(a){
    var btn=document.createElement('button');
    btn.type='button';btn.className='readBtn';
    btn.addEventListener('click',function(e){
      e.preventDefault();e.stopPropagation();
      var k=keyOf(a);
      if(read.has(k))read.delete(k);else read.add(k);
      writeSet(read);paint(a);updateCount();
    });
    a.appendChild(btn);
    paint(a);
  });
  updateCount();

  var search=document.getElementById('search');
  if(search)search.addEventListener('input',function(){
    var q=search.value.trim().toLowerCase();
    list.forEach(function(a){a.style.display=!q||a.textContent.toLowerCase().indexOf(q)>-1?'':'none'});
  });
} else {
  // note page: single read toggle, key derived from the page's own filename
  var host=document.querySelector('.bar > div')||document.querySelector('main');
  if(host){
    var k='notes/'+location.pathname.split('/').pop();
    var read=readSet();
    var btn=document.createElement('button');
    btn.type='button';btn.className='readToggle';
    function paint(){
      var isRead=read.has(k);
      btn.setAttribute('aria-pressed',String(isRead));
      btn.textContent=isRead?'Read ✓':'Mark as read';
    }
    btn.addEventListener('click',function(){
      if(read.has(k))read.delete(k);else read.add(k);
      writeSet(read);paint();
    });
    if(host.tagName==='MAIN')host.insertBefore(btn,host.firstChild);else host.appendChild(btn);
    paint();
  }
  var main=document.querySelector('main');
  if(main)setupPageSearch(main);
}
})();
