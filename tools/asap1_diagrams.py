from diagrams import box, arr, lab, fig

def d_knowledge():
    s=box(110,8,200,40,['Knowledge (books)','vs Wisdom (within)'],'b')+arr(210,48,210,66)
    s+=box(70,66,280,40,['A guru is a guide to the','next stretch, not an end point'],'n')+arr(210,106,210,124)
    s+=box(100,124,220,36,['Where do you stop?'],'b')
    s+=arr(160,160,105,188)+arr(260,160,315,188)
    s+=box(10,188,190,52,['Stuck on guru, temple,','idol or spouse'],'r')+box(220,188,190,52,['Keep moving past','each stopping point'],'g')
    s+=arr(105,240,105,262)+arr(315,240,315,262)
    s+=box(10,262,190,44,['Same grief (klesh)','keeps repeating'],'r')+box(220,262,190,44,['Wisdom keeps','growing, no ceiling'],'g')
    return fig(320,s,'The speaker\'s opening frame: knowledge has a ceiling, wisdom does not, and a guru is a guide, not a destination.','Flowchart contrasting stopping at a guru versus moving past each stopping point')

def d_balance():
    s='<line x1="40" y1="110" x2="380" y2="110" class="ln" stroke-width="3"/><path d="M210,112 L190,150 L230,150 Z" class="n"/>'
    s+=box(10,20,180,70,['MERCURY','empty space','checks the balance'],'n')+box(230,20,180,70,['VENUS','enjoyment,','beauty, luxury'],'n')
    s+=arr(100,90,100,106)+arr(320,90,320,106)
    s+=box(60,162,300,52,['Level: a workable mix of','good and bad in daily life'],'b')
    s+=box(60,228,300,56,['Tipped: life swings between','extremes with no evening-out'],'r')
    return fig(298,s,'Mercury and Venus as a seesaw. A level pair means an ordinary mix of luck; a tipped pair means life lurches between extremes.','Seesaw diagram of Mercury and Venus balance')

def d_rahuketu():
    s=box(100,6,220,36,['Someone speaks to you'],'n')
    s+=arr(140,42,90,70)+arr(280,42,330,70)+lab(100,62,'listen','end')+lab(320,62,"don't listen",'start')
    s+=box(5,70,190,58,['Rahu stays witness:','knowledge keeps building'],'g')+box(225,70,190,58,['Rahu negative:','cannot act on its own'],'r')
    s+=arr(100,128,100,150)+arr(320,128,320,150)
    s+=box(5,150,190,40,['Settled, able to act'],'g')+box(225,150,190,40,['Helplessness','(bebasi)'],'r')
    s+=box(60,206,300,34,['Ketu: a body with no head'],'b')+arr(210,240,210,258)
    s+=box(30,258,360,40,['Follows whoever or whatever','leads it, like a dog on a leash'],'n')+arr(210,298,210,316)
    s+=box(30,316,360,52,['Feed the dog, a saint, a guest:','Ketu settles, the body can enjoy'],'g')
    return fig(382,s,'Rahu cannot act without listening first; Ketu cannot judge, only follow. Each has its own simple fix.','Flowchart of Rahu listening versus Ketu following')

def d_stone():
    s=box(110,6,200,40,['A chart dosha','is present'],'r')
    s+=arr(150,46,100,74)+arr(270,46,320,74)
    s+=box(5,74,190,54,['Fix through discipline,','routine, consciousness'],'b')+box(225,74,190,54,['Wear the matching','gemstone'],'b')
    s+=arr(100,128,210,160)+arr(320,128,210,160)
    s+=box(60,160,300,44,['Either path limits downside','("damage control")'],'g')+arr(210,204,210,226)
    s+=box(30,226,360,56,['The stone never creates success','that was not otherwise due'],'n')
    return fig(300,s,'His claim about gemstones: they cap the downside of a dosha; they do not manufacture success on their own.','Decision flow showing a gemstone and discipline both as damage control, not a source of success')

def d_triad():
    s=box(140,6,140,34,['Grace and luck'],'b')
    s+=arr(170,40,70,70)+arr(210,40,210,70)+arr(250,40,350,70)
    s+=box(5,70,130,110,['INDRA','Enjoyment','blocked by','clutter'],'r')
    s+=box(145,70,130,110,['NEPTUNE','No grace:','nothing','helps'],'r')
    s+=box(285,70,130,110,['PLUTO','Chronic','illness and','fear of death'],'r')
    s+=arr(70,180,70,202)+arr(210,180,210,202)+arr(350,180,350,202)
    s+=box(5,202,130,90,['Spend on','comfort you','can afford;','clear closets'],'g')
    s+=box(145,202,130,90,['Generous,','"party mode";','stop counting','small costs'],'g')
    s+=box(285,202,130,90,['A simple','daily bow or','lamp toward','the south'],'g')
    s+=arr(210,292,210,314)
    s+=box(30,314,360,44,['Devotion, kirtan and chanting','keep all three steady'],'b')
    return fig(364,s,'Three more figures in the speaker\'s own framework: Indra for enjoyment, Neptune for grace, Pluto for chronic illness and fear.','Triad diagram of Indra, Neptune and Pluto with their remedies')

D=dict(knowledge=d_knowledge(),balance=d_balance(),rahuketu=d_rahuketu(),stone=d_stone(),triad=d_triad())
