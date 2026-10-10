from diagrams import box,arr,lab,fig
def d_symbol():
    s=box(110,8,200,40,['KETU: a body with no head'],'r')
    for x in (55,155,265,365): s+=arr(210,48,x,72)
    s+=box(5,72,100,86,['Fish','floats, bound,','fast'],'n')+box(110,72,90,86,['Sword','a cut will','happen'],'n')+box(205,72,110,86,['Flag','"my way",','ego'],'n')+box(320,72,95,86,['Shield','blocks, no','thought'],'n')
    s+=box(30,176,360,50,['No head: someone else thinks for you','mother, father, society, a guru'],'b')
    s+=arr(210,158,210,176)
    s+=box(30,242,175,64,['Ketu good','tailed animals help,','people follow you'],'g')+box(215,242,175,64,['Ketu bad','tailed animals harm,','nobody listens'],'r')
    s+=arr(210,226,117,242)+arr(210,226,302,242)
    return fig(316,s,'The four Ketu symbols and what they show up as in a chart.','Diagram of Ketu symbols')
def d_wealth():
    s=box(110,8,200,40,['Give to a stranger','who did not ask'],'g')+arr(210,48,210,66)
    s+=box(110,66,200,40,['12th house gets strong','Ketu is pleased'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Ketu returns it multiplied','4, 6, 8 times, from unknown places'],'g')+arr(210,164,210,182)
    s+=box(60,182,300,52,['Also needed: respect for women (Venus)','and for your guru (Jupiter), or Ketu eats both'],'r')
    return fig(244,s,'Why the speaker says Ketu wealth grows by giving. Do not grab, serve.','Flow of giving to strangers and Ketu wealth')
def d_stone():
    s=box(110,8,200,40,['Cat\'s eye (lahsuniya)','5 to 7 ratti'],'b')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Is Jupiter well placed in your chart?'],'b')
    s+=arr(130,106,80,134)+arr(290,106,330,134)+lab(95,126,'yes','end')+lab(325,126,'no','start')
    s+=box(10,134,140,52,['Wear on the','index finger'],'g')+box(270,134,140,52,['Is Saturn','well placed?'],'b')
    s+=arr(310,186,260,214)+arr(350,186,360,214)+lab(285,206,'yes','end')+lab(358,206,'no','start')
    s+=box(150,214,140,52,['Wear on the','middle finger'],'g')+box(300,214,115,76,['Fix Jupiter and','Saturn first.','Dire case: Sun','finger (ring)'],'r')
    s+=box(10,306,400,50,['Hard, technical stone. A bracelet can activate bad aspects.','Gomed is easier to place. Take chart advice first.'],'n')
    return fig(366,s,'Finger choice for the cat\'s eye, as the speaker describes it.','Decision tree for cat\'s eye finger')
def d_elements():
    cols=[('FIRE','1, 5, 9',['works well,','dims the Sun','a little'],'g',['siblings,','father, guru']),('WATER','4, 8, 12',['full power,','binds the','Moon\'s water'],'r',['mother,','authority,','strangers']),('AIR','3, 7, 11',['wind blows','Ketu away,','3 is its fall'],'b',['sister,','daughter,','girls']),('EARTH','2, 6, 10',['follows the','lord of the','sign'],'n',['Venus,','Rahu,','Saturn'])]
    s=''
    for i,(n,sg,eff,c,a) in enumerate(cols):
        x=5+i*103
        s+=box(x,8,98,46,[n,sg],c)+arr(x+49,54,x+49,68)+box(x,68,98,76,eff,'n')+arr(x+49,144,x+49,158)+box(x,158,98,76,['Keep right:']+a,'n')
    return fig(244,s,'Ketu by element of the sign, and the relationships that matter in each.','Four columns of Ketu by element')
def d_start():
    s=box(110,8,200,36,['Which Ketu problem?'],'b')
    items=[(['Things are','half done'],['Silver kada','with a gap']),(['Urinary or','genital trouble'],['Pierce ear or nose,','wash with curd']),(['No children,','weak "tail"'],['Serve dog,','cow and crow']),(['Cuts, anger,','harm to others'],['Forgive. Mars:','meditate on navel']),(['Zeal and','drive are dead'],['Exercise, keep a','pet or toy dog'])]
    for i,(p,r) in enumerate(items):
        y=60+i*60
        s+=box(5,y,190,48,p,'n')+arr(195,y+24,225,y+24)+box(225,y,190,48,r,'g')
    s+=box(10,366,400,66,['Always: serve the dog, never hit it.','Respect women, guru, grandparents, maternal side.','Give to strangers who did not ask.'],'b')
    return fig(442,s,'A starting path for Ketu remedies. Section 20 has the full list with timestamps.','Flowchart for choosing a Ketu remedy')
D=dict(symbol=d_symbol(),wealth=d_wealth(),stone=d_stone(),elements=d_elements(),start=d_start())
