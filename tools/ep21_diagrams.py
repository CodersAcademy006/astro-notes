from diagrams import box,arr,lab,fig
def d_letgo():
    s=box(110,8,200,40,['Something is dying','(job, love, money)'],'r')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Do you hold on?'],'b')
    s+=arr(130,106,95,134)+arr(290,106,325,134)
    s+=box(10,134,190,64,['Cry for years','Mind stays trapped','Pluto presses on'],'r')+box(220,134,190,64,['Let go in one jerk','Habit stops all at once'],'g')
    s+=arr(105,198,105,222)+arr(315,198,315,222)
    s+=box(10,222,190,64,['Death in instalments','Cycle repeats at 20','then 40, then 60'],'r')+box(220,222,190,64,['New garment, new','job or house, and','Pluto settles'],'g')
    return fig(296,s,'Hold on or let go, the speaker\'s core rule for Pluto.','Flowchart of holding on versus letting go')
def d_cycles():
    items=[('Moon','72 hours'),('Sun','1 month'),('Mercury','about 22 days'),('Venus, Mars','1 to 1.5 months'),('Jupiter','1 year'),('Saturn','2.5 years'),('Uranus','7, 14, 21 years'),('Pluto','20 to 21 years')]
    s=''
    for i,(p,t) in enumerate(items):
        x=5+(i%2)*208; y=8+(i//2)*62
        s+=box(x,y,200,52,[p,t],'r' if p=='Pluto' else 'n')
    s+=box(30,262,360,44,['A small issue clears fast, a big one takes','a long cycle. Let go or the next cycle starts.'],'b')
    return fig(316,s,'How long each planet takes to clear an issue, per the speaker.','Table of planet time scales')
def d_signs():
    items=[('1','Mars'),('2','Venus'),('3','Mercury'),('4','Moon'),('5','Sun'),('6','Rahu'),('7','Varuna'),('8','Death place'),('9','Jupiter'),('10','Saturn'),('11','Own sign'),('12','Ketu')]
    s=''
    for i,(n,p) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*66
        c='r' if n in('1','4','5','8') else ('g' if n in('2','6','9','10','11') else 'n')
        s+=box(x,y,96,54,['Sign '+n,p],c)
    s+=box(30,214,360,50,['Pluto in a sign. Red: hard, green: easier.','The speaker calls this a rough guide only.'],'b')
    return fig(274,s,'The sign Pluto sits in and the planet that owns it.','Grid of Pluto in signs 1 to 12')
def d_tail():
    s=box(110,8,200,40,['Pluto troubles grow'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Ketu is the cloud that covers'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Serve animals with tails'],'g')
    for x in (60,160,260,360): s+=arr(210,164,x,196)
    s+=box(5,196,100,52,['Cow','Dog'],'g')+box(110,196,100,52,['Fish','Buffalo'],'g')+box(215,196,100,52,['Pigeon','Crow'],'g')+box(320,196,95,52,['Do not','eat them'],'r')
    s+=box(30,264,360,44,['Then death finds no room, he says.','Treat a sick pet at the vet.'],'b')
    return fig(318,s,'The tailed animal remedy as the speaker describes it.','Flowchart of serving animals with tails')
def d_threads():
    items=[('1','Red, foot'),('2','Black, foot'),('3','Blue, foot'),('4, 5','Yellow, feet'),('6','Green-blue'),('7, 8','Black, foot')]
    s=''
    for i,(n,t) in enumerate(items):
        x=5+(i%3)*139; y=8+(i//3)*66
        s+=box(x,y,132,54,['Pluto in '+n,t],'n')
    s+=box(30,148,360,64,['Thread colour by sign, as he lists it.','Foot or wrist depends on the chart.','Read the chart first.'],'b')
    return fig(222,s,'Thread colours the speaker names for Pluto by sign.','Grid of thread colours by sign')
D=dict(letgo=d_letgo(),cycles=d_cycles(),signs=d_signs(),tail=d_tail(),threads=d_threads())
