from diagrams import box,arr,lab,fig
def d_bali():
    s=box(110,8,200,40,['Good luck or relief arrives'],'g')+arr(210,48,210,66)
    s+=box(60,66,300,40,['The planet now takes a sacrifice (bali)'],'r')+arr(210,106,210,124)
    s+=box(90,124,240,40,['Which currency do you pay in?'],'n')
    for x in (50,150,270,370): s+=arr(210,164,x,196)
    s+=box(5,196,90,66,['Time','lost minutes','or years'],'r')+box(105,196,90,66,['Body','illness,','a limb'],'r')+box(225,196,90,66,['Mind','stress,','fights'],'r')+box(325,196,90,66,['Money','best, can be','re-earned'],'g')
    s+=box(30,282,360,40,['His rule: pay early and quietly, in money'],'b')
    return fig(332,s,'The speaker\'s sacrifice model: the cost is paid in one currency or another.','Flowchart of the sacrifice a planet takes, paid in time, body, mind or money')
def d_modes():
    rows=[('Movable',['Signs 1, 4, 7, 10'],['Starts and keeps moving','construction, travel'],'n'),('Fixed',['Signs 2, 5, 8, 11'],['Settles and stays','wedding, Diwali puja,','child enters home'],'g'),('Dual',['Signs 3, 6, 9, 12'],['Goes and stops','in and out'],'r')]
    s=''
    for i,(a,b,c,k) in enumerate(rows):
        y=8+i*92
        s+=box(5,y,130,76,[a]+b,'b')+arr(135,y+38,150,y+38)+box(150,y,265,76,c,k)
    s+=box(30,292,360,40,['Pick the lagna type to match the job'],'b')
    return fig(342,s,'Three lagna types and the jobs he assigns them.','Diagram of movable, fixed and dual signs with their uses')
def d_family():
    items=[('Sun',['Father']),('Moon',['Mother']),('Mercury',['Daughter,','sister, aunt']),('Venus',['Wife']),('Mars',['Brother,','son, friend']),('Jupiter',['Guru,','husband']),('Saturn',['Servant']),('Rahu,','Ketu',['Indra, Varuna,','Yama'])]
    s=''
    k=0
    for p in items:
        if p[0]=='Rahu,':
            name=['Outer planets,','Rahu, Ketu'];role=['Indra, Varuna,','Yama']
        else:
            name=[p[0]];role=p[1]
        x=5+(k%3)*138; y=8+(k//3)*84
        s+=box(x,y,134,76,name+role,'r' if k==7 else 'n')
        k+=1
    s+=box(5,260,410,40,['Grace flows from the Sun at the top downward'],'b')
    return fig(310,s,'The household of planets as the speaker names it.','Grid of planets and the family roles he assigns')
def d_host():
    s=box(10,8,190,56,['Moon in sign 2','or sign 7'],'g')+box(220,8,190,56,['Moon in sign 1','or sign 8'],'r')
    s+=arr(105,64,105,84)+arr(315,64,315,84)
    s+=box(10,84,190,70,['Welcomed like a mother','mind and heart sync','sleep well'],'g')+box(220,84,190,70,['Son or Indra says','get out, mother','stomach, hyper-emotion'],'r')
    s+=box(10,172,190,56,['Sun in sign 1','Leader, strong eyes'],'g')+box(220,172,190,56,['Sun in the 7th house','friction in marriage'],'r')
    s+=box(30,246,360,40,['Result depends on who hosts the guest'],'b')
    return fig(296,s,'The host rule: a planet does best where its host welcomes it.','Diagram of the host rule for the Moon and the Sun')
def d_cord():
    steps=[['1. Sit insulated,','calm, eyes shut'],['2. Imagine a small','room, golden light'],['3. Two chairs:','you and the relative'],['4. See a cord, navel','to navel (blood kin)'],['5. Cut it, roll it,','blue bag into space'],['6. Bow, return both to','own bodies, thank']]
    s=''
    for i,t in enumerate(steps):
        y=8+i*60
        s+=box(60,y,300,46,t,'g' if i in(0,5) else 'n')
        if i<5: s+=arr(210,y+46,210,y+60)
    s+=box(30,372,360,40,['Do it only when calm, or the cord multiplies'],'r')
    return fig(422,s,'The cord cutting exercise as he teaches it, a visualisation only.','Flowchart of the six steps of cord cutting')
D=dict(bali=d_bali(),modes=d_modes(),family=d_family(),host=d_host(),cord=d_cord())
