from diagrams import box,arr,lab,fig
def d_cloud():
    s=box(110,8,200,40,['Ketu in sign 4'],'r')+arr(210,48,210,66)
    s+=box(40,66,340,50,['Ketu is a cloud: the Moon','water is hidden inside'],'n')+arr(210,116,210,134)
    s+=box(5,134,130,70,['Dog','Ketu'],'n')+box(145,134,130,70,['Cow','Venus'],'n')+box(285,134,130,70,['Crow','Saturn'],'n')
    s+=box(30,222,360,56,['Serve them, and guests and saints.','The speaker says the Moon is released'],'g')
    return fig(290,s,'Serving what Ketu rules, per the speaker.','Ketu cloud and the animals to serve')
def d_chain():
    s=box(110,8,200,40,['Moon down, begging'],'b')+arr(210,48,210,64)
    rows=[('Anger inside','Sun and Mars'),('Not speaking','Mercury'),('Ego, no bowing','Jupiter'),('Not enjoying','Venus'),('Contempt','Saturn'),('Greed, envy','Indra, Varuna')]
    for i,(a,b) in enumerate(rows):
        x=5+(i%3)*140; y=64+(i//3)*70
        s+=box(x,y,130,60,[a,'spoils '+b],'r' if i%2==0 else 'n')
    s+=box(30,214,360,50,['His list of what a bad Moon','drags down, as he states it'],'g')
    return fig(274,s,'What he says a bad Moon spoils, planet by planet.','Chain of planets spoiled by a bad Moon')
def d_pearl():
    s=box(60,8,300,44,['Where is sign 4 in the chart?'],'b')+arr(210,52,210,70)
    s+=box(60,70,300,44,['Is sign 4 itself in 6, 8 or 12?'],'n')+arr(120,114,90,142)+arr(300,114,330,142)+lab(100,134,'no','end')+lab(320,134,'yes','start')
    s+=box(5,142,200,70,['Moon in 6, 8, 12?','A pearl wakes the lord','He says: wear it'],'g')+box(215,142,200,70,['A pearl lifts that house','and enemies, illness','He says: do not'],'r')
    s+=box(30,230,360,50,['Little finger, silver, Monday,','growing Moon, as he states it'],'n')
    return fig(290,s,'The pearl rule as the speaker gives it. A full chart reading is needed.','Decision tree for wearing a pearl')
def d_year():
    items=[('Chaitra','Navratri: fast, feed girls'),('Shravan','Shivling water'),('Ashwin','Tarpan for ancestors'),('Kartik','Karwa Chauth'),('Pausha','No weddings, per him'),('Ekadashi','No rice, Nirjala')]
    s=''
    for i,(a,b) in enumerate(items):
        x=5+(i%2)*208; y=8+(i//2)*72
        s+=box(x,y,202,62,[a,b],'g' if i<4 else 'n')
    s+=box(30,232,360,50,['Each rite cuts water or honours water,','which he ties to the Moon'],'b')
    return fig(292,s,'Moon rites through the year, per the speaker.','Calendar of Moon rites')
def d_thread():
    s=box(110,8,200,40,['Moon flawed in chart'],'r')+arr(210,48,210,66)
    s+=box(40,66,340,44,['First: which sign holds the Moon?'],'b')+arr(210,110,210,128)
    s+=box(5,128,130,78,['Sign 1','Red thread','right foot'],'n')+box(145,128,130,78,['Sign 4, 5, 7','Yellow thread','left foot'],'g')+box(285,128,130,78,['Sign 12','Pearl, set Ketu','or Jupiter'],'n')
    s+=box(30,224,360,56,['No orange (Sun). No black tattoo.','These are his claims, not advice'],'r')
    return fig(290,s,'Threads by Moon sign as the speaker gives them.','Thread choice by Moon sign')
D=dict(cloud=d_cloud(),chain=d_chain(),pearl=d_pearl(),year=d_year(),thread=d_thread())
