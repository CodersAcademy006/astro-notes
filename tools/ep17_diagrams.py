from diagrams import box,arr,lab,fig
def d_system():
    s=box(5,8,100,50,['Sun','pulls all in'],'b')+box(115,8,100,50,['Jupiter','cuts the light'],'n')+box(225,8,90,50,['Saturn','holds Jupiter'],'n')+box(325,8,90,50,['Uranus','holds Saturn'],'g')
    s+=arr(115,33,105,33)+arr(225,33,215,33)+arr(325,33,315,33)
    s+=box(30,84,360,50,['Like a rubber band: the outer planets pull back','so the Sun does not swallow Jupiter'],'n')
    s+=box(5,160,200,64,['Beyond Uranus','Neptune is Varuna','Pluto is Yama (death)'],'n')+box(215,160,200,64,['Arun pulls the Sun\'s chariot','Indra is the deity','Two separate entities'],'b')
    return fig(240,s,'The speaker\'s picture of why Uranus matters in the solar system.','Rubber band picture of Sun, Jupiter, Saturn and Uranus')
def d_navel():
    s=box(110,8,200,40,['The navel portal','(fire centre)'],'b')+arr(150,48,100,76)+arr(270,48,320,76)
    s+=box(5,76,200,104,['Sign 1: Mars, Hanuman','Wants nothing','Burns the ego (Lanka)','Eats anything','Pitfall: pride'],'g')
    s+=box(215,76,200,104,['Sign 8: Indra','Wants taste, comfort','Enjoys, protects heaven','Chilli, chutney, party','Pitfall: attachment'],'g')
    s+=box(30,200,360,56,['Same fire, turned two ways.','A strong navel: no fear, good digestion,','easy breath, good sleep'],'n')
    return fig(268,s,'Sign 1 and sign 8 share the navel portal, as the speaker explains.','Two columns comparing sign 1 and sign 8')
def d_spoil():
    s=box(90,8,240,40,['Life talk: "this is hell"','or double talk behind backs'],'r')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Indra is spoiled'],'r')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Indulgence, addictions, waste','Money flows out, food from outside'],'r')
    s+=box(30,190,360,40,['Opposite: "great, no problem"','Respect yourself, gift yourself'],'g')+arr(210,230,210,248)
    s+=box(60,248,300,40,['Indra is built, the lagna is strong'],'g')
    return fig(300,s,'How the speaker says Indra is spoiled and how he is built.','Flowchart of spoiled and built Indra')
def d_signs():
    items=[('1','Mars','Fast power'),('2','Venus','Inflamed'),('3','Mercury','Wish tree'),('4','Moon','Short circuit'),('5','Sun','Folded hands'),('6','Rahu','Elephant ride'),('7','Varuna','Storm'),('8','Indra','Own seat'),('9','Jupiter','Controlled'),('10','Saturn','Dark party'),('11','Yama','Welcomed'),('12','Ketu','Tears cloud')]
    s=''
    for i,(n,p,t) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*72
        c='r' if n in('2','4','7') else 'g' if n in('1','5','8','9','11') else 'n'
        s+=box(x,y,96,62,[n+'. '+p,t],c)
    s+=box(30,228,360,44,['The house where Uranus sits is where','heaven, or trouble, is felt'],'b')
    return fig(284,s,'Uranus by sign number, as the speaker lists them. Green is easy, red is hard.','Grid of twelve signs and Uranus results')
def d_fix():
    s=box(110,8,200,40,['Asking, nothing manifests'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Check the navel: fear, digestion,','breath'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Fix core strength, set Rahu and Ketu'],'g')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Then Jupiter: a guru, liver detox'],'g')+arr(210,222,210,240)
    s+=box(60,240,300,40,['Then the Sun: witness mind, Indra helps'],'g')
    return fig(292,s,'The order the speaker gives for fixing the body portal before asking.','Flowchart of navel, Jupiter and Sun')
D=dict(system=d_system(),navel=d_navel(),spoil=d_spoil(),signs=d_signs(),fix=d_fix())
