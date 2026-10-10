from diagrams import box,arr,lab,fig
def d_pair():
    s=box(110,8,200,40,['One snake, one pair'],'b')+arr(150,48,95,72)+arr(270,48,325,72)
    s+=box(5,72,200,150,['RAHU: the head','Sun side, ultraviolet','Mind, eyes, ears, nose','Compares, watches, plans','Fault: head jams'],'n')
    s+=box(215,72,200,150,['KETU: the body','Moon side, infrared','Skin, bed, hands, healing','Does, makes, feels','Fault: body fails'],'n')
    s+=box(30,240,360,50,['Manifestation happens between the two:','Rahu thinks rightly, Ketu makes it'],'g')
    s+=arr(105,222,105,240)+arr(315,222,315,240)
    return fig(300,s,'Rahu and Ketu are one pair, the head and the body.','Rahu and Ketu head and body')
def d_seesaw():
    s='<line x1="60" y1="90" x2="360" y2="90" stroke="currentColor" stroke-width="3"/>'
    s+='<polygon points="210,90 190,130 230,130" fill="currentColor" opacity="0.4"/>'
    s+=box(30,20,120,50,['Level','Both balanced'],'g')+box(270,20,120,50,['Level','Manifestation'],'g')
    s+=box(5,150,130,64,['Rahu too high','Ketu low:','body, home suffer'],'r')+box(285,150,130,64,['Ketu too high','Rahu low:','servant, depressed'],'r')
    s+=box(140,150,140,64,['Seesaw rule','up here,','down there'],'n')
    s+=box(30,232,360,50,['Fix: witness mind (Rahu) and service (Ketu),','a little of each, never zero or too much'],'b')
    return fig(292,s,'The Rahu-Ketu seesaw, as the speaker draws it.','Seesaw diagram of Rahu and Ketu')
def d_flow():
    s=box(110,8,200,40,['Serve and give','(Ketu up)'],'g')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Witness mind comes on','(Rahu level)'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['No ego, no madness, no fights','Ketu makes what you wish'],'g')
    s+=box(30,186,175,76,['Too much serving','you become a slave,','depressed, blind and deaf'],'r')+box(215,186,175,76,['Stealing at the temple','or abusing workers','Ketu falls, Rahu rises'],'r')
    s+=arr(150,164,117,186)+arr(270,164,302,186)
    return fig(272,s,'How service sets Rahu, and how it goes wrong.','Flowchart of service and witness mind')
def d_fixed():
    items=[('1','Mars'),('2','Venus'),('3','Mercury'),('4','Moon'),('5','Sun'),('6','Rahu'),('7','Varuna'),('8','Indra'),('9','Jupiter'),('10','Saturn'),('11','Yama'),('12','Ketu')]
    s=''
    for i,(n,p) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*66
        c='r' if p in('Rahu','Ketu') else 'n'
        s+=box(x,y,96,54,['Area '+n,p],c)
    s+=box(30,214,360,50,['The sign that lands on an area can differ.','Fix the sign first, planet second.'],'b')
    return fig(274,s,'The fixed areas, as the speaker lists them.','Grid of fixed areas and planets')
def d_signfirst():
    s=box(110,8,200,40,['A house has a bad planet'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Which sign sits in that house?'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Fix that sign lord first','(emerald if the sign is Mercury)'],'g')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Then the planet: pearl, cat\'s eye'],'n')+arr(210,222,210,240)
    s+=box(30,240,360,50,['Stone is a once-for-life fix, like glasses.','Sugar or heart cases still need medicine.'],'b')
    return fig(300,s,'Fix the sign before the planet, per the speaker.','Flowchart for sign before planet')
D=dict(pair=d_pair(),seesaw=d_seesaw(),flow=d_flow(),fixed=d_fixed(),signfirst=d_signfirst())
