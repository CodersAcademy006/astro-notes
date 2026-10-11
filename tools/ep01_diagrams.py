from diagrams import box,arr,lab,fig
def d_fate():
    s=box(10,8,190,50,['Past-life karma'],'n')+box(220,8,190,50,['This life: your','commands, reactions'],'n')
    s+=arr(105,58,105,86)+arr(315,58,315,86)
    s+=box(10,86,190,64,['Prarabdha (fixed)','about 12 percent','debts and balance'],'r')+box(220,86,190,64,['Karma you add','reacting adds more','not reacting adds none'],'g')
    s+=arr(105,150,180,184)+arr(315,150,240,184)
    s+=box(110,184,200,44,['Your life as it plays out'],'b')+arr(210,228,210,250)
    s+=box(60,250,300,52,['Remedy and grace: the bone bruises,','it does not break'],'g')
    return fig(312,s,'Fixed prarabdha plus the karma you add. A remedy softens, it does not delete.','Flowchart of prarabdha, new karma and remedy')
def d_signs():
    items=[('1 Aries','Mars'),('2 Taurus','Venus'),('3 Gemini','Mercury'),('4 Cancer','Moon'),('5 Leo','Sun'),('6 Virgo','Rahu'),('7 Libra','Neptune'),('8 Scorpio','Uranus'),('9 Sagittarius','Jupiter'),('10 Capricorn','Saturn'),('11 Aquarius','Pluto'),('12 Pisces','Ketu')]
    s=''
    for i,(n,p) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*66
        c='r' if p in('Rahu','Ketu') else ('b' if p in('Neptune','Uranus','Pluto') else 'n')
        s+=box(x,y,96,54,[n,p],c)
    s+=box(30,214,360,50,['Seven classical planets, plus','five more rulers in this class'],'g')
    return fig(274,s,'The twelve signs and their rulers, as the speaker assigns them.','Grid of twelve signs and rulers')
def d_body():
    rows=[('Crown: thoughts arrive','n'),('Third eye (ajna): control centre','b'),('Mercury, Venus: throat to heart','n'),('Mars: navel, fire','r'),('Jupiter: water chakra, liver','n'),('Saturn: pelvic girdle, bones','n'),('Uranus, Neptune, Pluto: below','b')]
    s=''
    for i,(t,c) in enumerate(rows):
        y=8+i*44
        s+=box(60,y,300,34,[t],c)
        if i<len(rows)-1: s+=arr(210,y+34,210,y+44)
    return fig(318,s,'Where the speaker places the planetary portals, top to bottom.','Vertical map of planets along the body')
def d_elements():
    segs=[(288,'b'),(48,'n'),(16,'r'),(24,'g'),(24,'n')]
    s='';x=10
    for w,c in segs:
        s+=f'<rect x="{x}" y="10" width="{w}" height="36" class="{c}"/>'; x+=w
    rows=[('Water 72: Varuna, dreams, the body','b'),('Earth 12: fixed, prarabdha, base chakra','n'),('Fire 4: runs by itself, the navel','r'),('Air 6: breath and knowledge','g'),('Space 6: grace, the unseen','n')]
    for i,(t,c) in enumerate(rows): s+=box(10,60+i*40,400,32,[t],c)
    return fig(268,s,'The five elements in the body, as the speaker gives the shares.','Bar of five elements with shares')
def d_journey():
    cells={(0,0):(['NORTH-WEST','Support','for others'],'n'),(1,0):(['NORTH','Money and','chances'],'g'),(2,0):(['NORTH-EAST','Clarity,','then fun'],'g'),
           (0,1):(['WEST','Prayer, God','WNW: detox'],'b'),(1,1):(['Starts north-','north-west,','goes clockwise'],'e'),(2,1):(['EAST','Friends,','talking'],'n'),
           (0,2):(['SOUTH-WEST','Ancestors,','children'],'b'),(1,2):(['SOUTH','Discipline,','sleep, brand'],'n'),(2,2):(['SOUTH-EAST','Earning,','confidence'],'g')}
    s=''
    for (cx,cy),(l,c) in cells.items(): s+=box(5+cx*138,6+cy*86,134,76,l,c)
    s+=box(30,270,360,50,['Birth, money, health, clarity, fun, friends,','earning, rest, children, prayer'],'n')
    return fig(330,s,'The zones of the home follow the stages of a life, per the speaker.','Compass of home zones as life stages')
D=dict(fate=d_fate(),signs=d_signs(),body=d_body(),elements=d_elements(),journey=d_journey())
