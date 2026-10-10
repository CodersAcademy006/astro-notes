from diagrams import box,arr,lab,fig
def d_feet():
    s=box(110,8,200,40,['Feet: Pluto\'s place'],'b')+arr(150,48,95,76)+arr(270,48,325,76)
    s+=box(5,76,200,76,['Care for them','Touch and press your own','Press elders\' feet'],'g')+box(215,76,200,76,['No cracks','Ghee or oil on soles','Or petroleum jelly'],'g')
    s+=box(30,176,360,44,['Speaker\'s remedies, not medical advice'],'n')
    return fig(232,s,'The speaker\'s map of the feet and how to look after them.','Feet as Pluto place with care steps')
def d_chain():
    s=box(60,8,300,40,['Heavy weight in the mind'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Pain in the body, strained relations'],'r')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Take the Yamraj out of the mind'],'b')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Forgive, drop the grudge, let go'],'g')
    s+=box(30,240,360,44,['His teaching. See a doctor for pain.'],'n')
    return fig(296,s,'The speaker\'s chain from mind to body and the remedy he gives.','Flowchart from mental weight to forgiveness')
def d_graces():
    s=box(110,8,200,40,['What can hold Yamraj'],'b')
    items=[('Sun','Light, life'),('Moon','Water, Shiva'),('Mars','Hanuman, breath'),('Rahu','The observer')]
    for i,(p,t) in enumerate(items):
        s+=box(5+(i%2)*209,60+(i//2)*70,206,60,[p,t],'g')
    s+=box(30,204,360,44,['Observed, Yamraj goes straight on one line'],'n')
    return fig(260,s,'Graces the speaker names against Yamraj.','Sun, Moon, Mars and Rahu')
def d_signs():
    rows=[('Sign 1','Mars','Courage bent, villain'),('Sign 2','Venus','Wealth, voice, ends'),('Sign 3','Mercury','Talk, gifts, gadgets'),('Sign 4','Moon','Home, diet change'),('Sign 5','Sun','Royalty, lineage')]
    s=''
    for i,(a,b,c) in enumerate(rows):
        y=8+i*52
        s+=box(5,y,80,44,[a],'b')+box(92,y,90,44,[b],'n')+box(189,y,226,44,[c],'g')
    return fig(272,s,'Pluto in signs 1 to 5, as the speaker reads them.','Five signs with ruler and effect')
def d_balance():
    s=box(5,8,200,50,['Heaven (Uranus)','Hell (Neptune)'],'n')+box(215,8,200,50,['Yamlok (Pluto)','Keeps the balance'],'b')
    s+=arr(210,58,210,76)+box(60,76,300,40,['Plus always equals minus'],'r')+arr(210,116,210,134)
    s+=box(60,134,300,52,['Water what you want','Attention feeds what grows'],'g')
    s+=box(30,204,360,44,['His teaching, with illustrative numbers'],'n')
    return fig(260,s,'The speaker\'s balance of joy and sorrow.','Plus equals minus flow')
D=dict(feet=d_feet(),chain=d_chain(),graces=d_graces(),signs=d_signs(),balance=d_balance())
