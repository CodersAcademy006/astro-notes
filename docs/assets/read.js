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
'.readToggle{flex-shrink:0;margin-left:auto}';
document.head.appendChild(style);

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
}
})();
