from diagrams import box,arr,lab,fig
def d_layers():
    s=box(60,8,300,50,['SUN: one thought, strong aura','Light reaches every planet'],'b')+arr(210,58,210,76)
    s+=box(60,76,300,50,['JUPITER: guru, the filter','Light comes down clean'],'g')+arr(210,126,210,144)
    s+=box(30,144,360,76,['BELOW JUPITER: Ketu, Saturn, Uranus,','Neptune, Pluto','Lust, anger, greed, fear. Nobody listens.'],'r')
    return fig(232,s,'Where the Sun\'s light fades, as the speaker draws it.','Layers from Sun to dark planets')
def d_heart():
    s=box(110,8,200,40,['Heart is broken'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['The Sun is hit that day'],'n')+arr(210,106,210,124)
    s+=box(30,124,360,40,['Result lands in the house the Sun sits in'],'b')
    for i,(a,b) in enumerate([('2nd','money'),('4th','home'),('5th','children'),('7th','marriage'),('10th','work')]):
        s+=box(5+i*83,182,78,50,[a,b],'n')
    s+=arr(210,164,210,182)+box(30,250,360,50,['Fix: forgive, let go, take blessings'],'g')
    return fig(312,s,'How a broken heart is said to land in the chart.','Heartbreak to house result')
def d_signs():
    rows=[(['Sign 1 and 8','Best'],'g'),(['Sign 3 and 6','Very good'],'g'),(['Sign 4','OK'],'n'),(['Sign 2 and 7','Worst'],'r'),(['Sign 9 to 12','Churning'],'b')]
    s=''
    for i,(t,c) in enumerate(rows):
        s+=box(5+(i%2)*212,8+(i//2)*66,202,56,t,c)
    s+=box(30,208,360,60,['Signs 1 and 8 sit next to 2 and 7.','A small slip in the chalit chart','swings best to worst.'],'b')
    return fig(278,s,'The Sun by sign, in the speaker\'s ranking.','Sun sign ranking')
def d_serve():
    s=box(110,8,200,40,['Sun fault shows'],'r')+arr(210,48,210,66)
    s+=box(30,66,360,40,['Help a stranger who did not ask'],'n')+arr(210,106,210,124)
    s+=box(30,124,360,40,['Give quietly, ask nothing, tell no one'],'g')
    s+=arr(210,164,210,182)+box(5,182,200,66,['Sun heals','Bones, heart,','enemies ease'],'g')+box(215,182,200,66,['You boast of it','"I gave 100 kg"','Sun spoils'],'r')
    return fig(258,s,'Why secret giving is the Sun\'s main remedy.','Flowchart of giving to strangers')
def d_ruby():
    s=box(110,8,200,40,['Sun trouble'],'r')+arr(210,48,210,66)
    s+=box(30,66,360,50,['First: serve strangers, wheat donation,','less table salt, cow on Sundays'],'n')+arr(210,116,210,134)
    s+=box(30,134,360,40,['Still stuck? Sun in a bad house?'],'b')+arr(210,174,210,192)
    s+=box(30,192,360,60,['Ruby: ring finger, 5 to 7 ratti,','gold or copper, Sunday morning','Wakes the house owner. Does not add power.'],'g')
    return fig(262,s,'The order of Sun remedies in the class.','Ladder from small remedies to ruby')
D=dict(layers=d_layers(),heart=d_heart(),signs=d_signs(),serve=d_serve(),ruby=d_ruby())
