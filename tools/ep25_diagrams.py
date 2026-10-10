from diagrams import box,arr,lab,fig
def d_sea():
    s=box(110,8,200,40,['Neptune (Varuna)'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['The sea: unlimited, hidden, gives all'],'n')
    s+=arr(110,106,75,140)+arr(310,106,345,140)
    s+=box(5,140,200,70,['Water (Moon)','and salt (Sun)','sea = body fluids'],'g')+box(215,140,200,70,['Wishes, sleep,','intuition, grace','west direction'],'g')
    s+=box(30,226,360,44,['Too much gives drink, drugs, illusion'],'r')
    return fig(280,s,'What the speaker places inside Neptune.','Diagram of Neptune as the sea')
def d_elem():
    s=box(5,8,200,66,['Water signs 4, 8, 12','Best: positive result'],'g')+box(215,8,200,66,['Earth signs 2, 6, 10','Friendly: firm principles'],'g')
    s+=box(5,86,200,66,['Air signs 3, 7, 11','Little match with water'],'n')+box(215,86,200,66,['Fire signs 1, 5, 9','Most negative: quarrels'],'r')
    s+=box(30,168,360,50,['Fire plus water: false, drama,','actors. Negative: deceit'],'b')
    return fig(228,s,'Neptune by element of the sign, as the speaker reads it.','Grid of Neptune by sign element')
def d_conj():
    items=[('Sun','name, fame'),('Moon','fame, intuition'),('Mars','performer'),('Mercury','soft talk'),('Jupiter','belief, ego'),('Venus','artist, music'),('Saturn','luck, loans'),('Pluto','Dharmaraj'),('Ketu','healer, cult')]
    s=''
    for i,(n,p) in enumerate(items):
        s+=box(5+(i%3)*140,8+(i//3)*66,132,54,['With '+n,p],'g' if n in('Moon','Jupiter','Pluto','Ketu') else 'n')
    s+=box(30,214,360,44,['Negative signs turn each into harm'],'r')
    return fig(268,s,'Neptune with each planet, in brief.','Grid of Neptune conjunctions')
def d_thread():
    s=box(110,8,200,40,['Choose the colour'],'n')+arr(210,48,210,66)
    s+=arr(110,48,70,76)+arr(310,48,350,76)
    s+=box(5,76,130,70,['Light blue','Neptune','soft fix'],'g')+box(145,76,130,70,['Ink blue','Rahu','crushes'],'r')+box(285,76,130,70,['Red or purple','Mars','dilute with blue'],'b')
    s+=box(30,168,360,44,['Yellow (Jupiter) for work, then change'],'n')
    s+=box(30,226,360,44,['Side effects always exist, check chart'],'r')
    return fig(280,s,'The thread and ink colours named in the class.','Diagram of thread colours')
def d_west():
    s=box(110,8,200,40,['West of the home'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['W4, W5, W6: Varuna, asuras, grace'],'n')+arr(210,106,210,124)
    s+=box(60,124,300,40,['No door, keep clean'],'g')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Place the ishta image in W5'],'g')+arr(210,222,210,240)
    s+=box(60,240,300,40,['Sleep, release the wish, forget it'],'n')
    return fig(290,s,'The west direction steps in the speaker\'s account.','Flowchart of the west area')
D=dict(sea=d_sea(),elem=d_elem(),conj=d_conj(),thread=d_thread(),west=d_west())
