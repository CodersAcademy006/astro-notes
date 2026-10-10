from diagrams import box,arr,lab,fig
def d_seesaw():
    s='<line x1="40" y1="100" x2="380" y2="100" class="ln" stroke-width="3"/><path d="M210,102 L190,140 L230,140 Z" class="n"/>'
    s+=box(10,16,180,64,['RAHU high','only the head runs','body does not'],'r')+box(230,16,180,64,['KETU dead','skin, money, body','suffer'],'r')
    s+=box(30,158,360,50,['Jupiter (Vishnu) cut the pair','and keeps the seesaw sane'],'b')
    s+=box(30,224,360,56,['Rahu spoils Jupiter, then Ketu.','Fix Rahu, and Jupiter sets right'],'g')
    return fig(290,s,'Rahu and Ketu as a seesaw, with Jupiter in charge, per the speaker.','Seesaw of Rahu and Ketu with Jupiter')
def d_houses():
    items=[('1','Mars'),('2','Venus'),('3','Mercury'),('4','Moon'),('5','Sun'),('6','Rahu'),('7','Uranus'),('8','Indra'),('9','Jupiter'),('10','Saturn'),('11','Yamraj'),('12','Ketu')]
    s=''
    for i,(n,p) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*66
        c='g' if p=='Jupiter' else ('r' if p in('Rahu','Ketu') else 'n')
        s+=box(x,y,96,54,['House '+n,p],c)
    s+=box(30,214,360,50,['Check the sign in a house before','any remedy for that house'],'b')
    return fig(274,s,'Who owns each place, as the speaker lists it.','Grid of twelve houses and owners')
def d_guru():
    s=box(110,8,200,40,['Rahu and Ketu need a guru'],'b')
    for x in (60,160,260,360): s+=arr(210,48,x,76)
    s+=box(5,76,100,70,['Mother','mental guru','Moon better'],'n')+box(110,76,100,70,['Father','mental guru','Sun better'],'n')
    s+=box(215,76,100,70,['Guru in','person','Jupiter better'],'g')+box(320,76,95,70,['Stone guru','Mars better'],'n')
    s+=box(30,170,360,50,['Improve Jupiter by your own karma,','and Rahu and Ketu set'],'g')
    return fig(230,s,'Kinds of guru and the planet each improves, per the speaker.','Types of guru and planets')
def d_thread():
    s=box(110,8,200,40,['Rahu troubles a house'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,44,['Is sign 5 at that spot?'],'b')+arr(130,110,90,138)+arr(290,110,330,138)+lab(100,130,'no','end')+lab(320,130,'yes','start')
    s+=box(10,138,190,66,['Yellow thread','on the right wrist','(Jupiter sets Rahu)'],'g')+box(220,138,190,66,['Gold or yellow on the','right wrist would ruin 11','Use a red tattoo, left arm'],'r')
    s+=box(30,224,360,50,['Check the navamsa first: a blue thread','is cancelled if Rahu is debilitated there'],'n')
    return fig(284,s,'Rahu and Jupiter threads, as taught. Chart conditions come first.','Decision tree for threads on the wrist')
def d_check():
    s=box(110,8,200,40,['Any Jupiter remedy'],'b')+arr(210,48,210,66)
    s+=box(40,66,340,44,['Which sign sits in that house?'],'n')+arr(210,110,210,128)
    s+=box(40,128,340,44,['Do signs 10 or 11 hit it,','or is it the 6th, 8th or 12th?'],'b')
    s+=arr(110,172,80,200)+arr(310,172,340,200)+lab(70,192,'yes','end')+lab(350,192,'no','start')
    s+=box(5,200,200,66,['Do not do it','The remedy backfires','Wake no vice houses'],'r')+box(215,200,200,66,['Go ahead','Give yellow, topaz,','thread as taught'],'g')
    return fig(276,s,'The speaker\'s check before a Jupiter remedy.','Decision tree before a Jupiter remedy')
D=dict(seesaw=d_seesaw(),houses=d_houses(),guru=d_guru(),thread=d_thread(),check=d_check())
