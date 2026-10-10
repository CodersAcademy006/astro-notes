from diagrams import box,arr,lab,fig
def d_fifty():
    s=box(110,8,200,40,['Two people, one chariot'],'b')+arr(150,48,95,76)+arr(270,48,325,76)
    s+=box(5,76,200,76,['Arjun: does his 50','Keeps balance, shoots','Does not disturb'],'g')+box(215,76,200,76,['Krishna: does the rest','Drives the chariot','The other half'],'g')
    s+=box(30,176,360,52,['Above 50 the fierce form (rudrata) comes:','you hurt yourself or the other'],'r')
    return fig(240,s,'The 50-50 rule that opens the class.','Arjun and Krishna sharing a chariot, 50 each')
def d_jvs():
    s=box(5,8,200,40,['JUPITER (purush)'],'b')+box(215,8,200,40,['VENUS (prakriti)'],'b')
    rows=[(['Fast spin, about 11 hours','Gas giant, big talk'],['Slow, about 243 days','Spins against the rest']),(['Gives advice (updesh)','"Follow behind me"'],['Gives orders (aadesh)','"I will drag you"']),(['Liver, cholesterol','Anger, then leaves'],['Heart, joy, love','Stays, "die, I revive you"'])]
    for i,(a,b) in enumerate(rows):
        y=64+i*70
        s+=box(5,y,200,60,a,'n')+box(215,y,200,60,b,'n')
    s+=box(30,278,360,44,['Both are Brahmin planets.','Seat them in balance.'],'g')
    return fig(334,s,'Jupiter and Venus side by side, as the speaker contrasts them.','Comparison of Jupiter and Venus')
def d_bp():
    s=box(110,8,200,40,['Constant complaining'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Venus heats up (about 470 C)'],'n')+arr(210,106,210,124)
    s+=box(60,124,300,40,['The speaker links: high blood pressure'],'r')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Then cursing: pancreas, sugar'],'r')
    s+=box(30,240,360,52,['His claims, not medical findings.','Stop complaining and see a doctor.'],'b')
    return fig(304,s,'The speaker\'s chain from complaining to the body. These are his claims.','Flowchart from complaining to blood pressure and sugar')
def d_pisces():
    s=box(110,8,200,40,['Venus visits a house'],'b')+arr(150,48,95,76)+arr(270,48,325,76)
    s+=box(5,76,200,90,['Sign 12, Ketu\'s home','Exalted, best welcome','Cow and elephant yoni','Lakshmi imagined here'],'g')
    s+=box(215,76,200,90,['Rahu\'s sign','Debilitated','Rahu is a head only','No body for fun'],'r')
    s+=box(30,188,360,52,['Clouds on Venus trap the light,','which the speaker calls Ketu'],'n')
    return fig(252,s,'Where Venus is exalted and debilitated, per the speaker.','Venus in Ketu sign and Rahu sign')
def d_family():
    items=[('Sun','Suryakant'),('Moon','Chandrakanta'),('Mercury','Budhika'),('Rahu','The worker'),('Venus','Wife or partner'),('Mars','Son, commander')]
    s=''
    for i,(p,t) in enumerate(items):
        x=5+(i%3)*139; y=8+(i//3)*70
        s+=box(x,y,132,60,[p,t],'g' if p=='Venus' else 'n')
    s+=box(30,156,360,52,['Venus meets each one differently:','Sun burns her, Neptune throws a party'],'b')
    return fig(220,s,'The speaker\'s royal family picture of the planets.','Planets as a family')
D=dict(fifty=d_fifty(),jvs=d_jvs(),bp=d_bp(),pisces=d_pisces(),family=d_family())
