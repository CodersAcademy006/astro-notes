from diagrams import box,arr,lab,fig
def d_account():
    s=box(110,8,200,40,['Every word and deed','is recorded'],'b')+arr(210,48,210,66)
    s+=box(30,66,360,40,['Curses, blessings, quarrels, service pile up'],'n')
    s+=arr(110,106,80,134)+arr(310,106,340,134)
    s+=box(10,134,190,52,['Blessings from many','people asking for you'],'g')+box(220,134,190,52,['Curses and grudges','from many people'],'r')
    s+=arr(105,186,105,208)+arr(315,186,315,208)
    s+=box(10,208,190,52,['Ketu builds and keeps','money, work, love'],'g')+box(220,208,190,52,['Fruit switches on','illness, loss'],'r')
    return fig(270,s,'The karma account as the speaker describes it: Ketu delivers what has piled up.','Karma account flowchart')
def d_heads():
    s=box(110,8,200,40,['KETU: body, no head'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['It acts as the head it is given'],'n')
    for i,(t,c) in enumerate([(['Moon','cools'],'g'),(['Sun','heats'],'r'),(['Rahu','obeys Rahu'],'n'),(['Neptune','never full'],'n'),(['Indra','any means'],'r'),(['Jupiter','no wrong deed'],'g')]):
        x=5+(i%3)*139; y=124+(i//3)*70
        s+=box(x,y,133,60,t,c)
    s+=arr(210,106,210,124)
    return fig(270,s,'Ketu in signs 4 to 9, according to the head it is fitted with.','Ketu and the head fitted on it')
def d_cloud():
    s=box(110,8,200,40,['KETU: cloud, smoke'],'b')
    rows=[('Mars, Venus','friends: fire gives smoke','g'),('Mercury','enemy: wind blows it away','r'),('Jupiter','a huge shape, rocket lift','g'),('Saturn','darkness hides the cloud','n'),('Indra','lightning empties the cloud','n'),('Neptune','the sea feeds the cloud','n')]
    for i,(a,b,c) in enumerate(rows):
        x=5+(i%2)*209; y=60+(i//2)*62
        s+=box(x,y,200,54,[a,b],c)
    s+=arr(210,48,210,60)
    return fig(256,s,'How the cloud picture of Ketu fits each planet.','Ketu and the planets')
def d_seesaw():
    s='<line x1="40" y1="110" x2="380" y2="110" class="ln" stroke-width="3"/><path d="M210,112 L190,150 L230,150 Z" class="n"/>'
    s+=box(10,22,180,70,['RAHU: the head','witness mind'],'b')+box(230,22,180,70,['KETU: the body','fun, parties, health'],'g')
    s+=arr(100,92,100,106)+arr(320,92,320,106)
    s+=box(10,162,200,64,['Rahu down, Ketu up','blind fun, no witness'],'r')+box(215,162,200,64,['Rahu up, Ketu down','body and fun fail'],'r')
    s+=box(30,240,360,52,['Level: enjoy and let go','"if it comes good, if not better"'],'g')
    return fig(302,s,'Keeping Rahu and Ketu level, as he describes it.','Rahu Ketu seesaw')
def d_start():
    s=box(110,8,200,40,['Things will not stay'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Whom are you asking? Who asks for you?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)
    s+=box(10,134,190,64,['Stop cursing and doubting','Earn blessings','Give quietly'],'g')
    s+=box(220,134,190,64,['Fit a good head on Ketu','guru, right deity','one Ganesha'],'g')
    s+=arr(100,198,100,220)+arr(315,198,315,220)
    s+=box(10,220,190,64,['Give to a stranger','cow, dog, crow'],'b')+box(220,220,190,64,['Leave ego with God','learn to bow'],'b')
    return fig(294,s,'A starting path from the class. Section 16 has the table with timestamps.','Flowchart for Ketu advice')
D=dict(account=d_account(),heads=d_heads(),cloud=d_cloud(),seesaw=d_seesaw(),start=d_start())
