from diagrams import box,arr,lab,fig
def d_chakras():
    labels=['7 Crown','6 Third eye','5 Throat','4 Heart','3 NAVEL: Hanuman seat','2 Sacral','1 Root: Saturn, dark']
    s=''
    for i,l in enumerate(labels):
        c='g' if 'NAVEL' in l else ('r' if 'Root' in l else 'n')
        s+=box(60,8+i*44,300,36,[l],c)
        if i<len(labels)-1: s+=arr(210,44+i*44,210,52+i*44)
    return fig(8+7*44,s,'The speaker\'s chakra ladder. He treats the navel, third from the bottom, as the seat of Hanuman consciousness.','Stacked diagram of seven chakras with the navel marked as the Hanuman seat')
def d_navel():
    s=box(140,150,140,50,['NAVEL','(Hanuman)'],'g')
    targets=[('Breath settles',40,30),('Confidence, work',300,30),('Digestion, health',40,270),('Relationships, love',300,270)]
    for lbl,x,y in targets:
        s+=arr(210,175,x+40,y+20) if y<150 else arr(210,200,x+40,y)
        s+=box(x,y,160,44,[lbl],'n')
    return fig(330,s,'The speaker\'s claim: a settled navel is read out through the body as calm breath, confidence, health and better relationships.','Radiating diagram of the navel affecting breath, confidence, health and relationships')
def d_allegory():
    s=box(130,8,160,40,['RAM','supreme consciousness'],'b')+arr(210,48,210,66)
    s+=box(110,66,200,40,['SITA','your individual self'],'n')+arr(210,106,210,124)
    s+=box(90,124,240,40,['LAKSHMAN (buddhi)','crosses its own line'],'n')+arr(210,164,210,182)
    s+=box(90,182,240,46,['RAVANA (ego)','seizes Sita'],'r')+arr(210,228,210,246)
    s+=box(60,246,300,46,['HANUMAN (prana)','crosses the ocean, lights the fire'],'g')+arr(210,292,210,310)
    s+=box(90,310,240,40,['Ego burns; Sita','is freed, reunites with Ram'],'g')
    return fig(360,s,'The speaker\'s reading of the Ramayana as one person\'s inner story: the self loses its boundary, ego takes hold, and life-breath (Hanuman) burns it away.','Flowchart of the Ramayana read as an inner allegory')
def d_marspower():
    s=box(90,8,240,40,['Mars circles through all 12 signs'],'n')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Reaches the 10th sign, Capricorn'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,46,['Exalted here (uchcha):','its strongest classical placement'],'g')+arr(210,170,210,188)
    s+=box(30,188,360,46,['Capricorn sits at the root chakra,','Saturn\'s usually dark domain'],'n')+arr(210,234,210,252)
    s+=box(60,252,300,46,['Light enters the dark;','Shani steps aside for Hanuman'],'g')
    return fig(312,s,'The speaker\'s astronomy for "Hanuman at full power": Mars exalted in Capricorn, lighting up the root chakra.','Flowchart of Mars reaching exaltation in Capricorn at the root chakra')
def d_mangal():
    s=box(90,8,240,40,['Mars in house 1, 4, 7, 8 or 12'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Mangal dosha: named in the chart'],'n')
    for x in (60,215,350): s+=arr(210,106,x,138)
    s+=box(5,138,140,70,['Household conflict','Feed jaggery to a','red/brown cow'],'g')
    s+=box(150,138,140,70,['Venus feels blocked','7 cowries, red cloth,','kept in a locker'],'g')
    s+=box(295,138,140,70,['Vastu feels off','2 monkey figures','in the south'],'g')
    s+=box(30,222,360,40,['Saturn sitting with Mars in the same house','is said to cancel the dosha'],'n')
    return fig(282,s,'The speaker\'s remedies for mangal dosha, by the problem it is blamed for.','Flowchart of mangal dosha and its three named remedies')
D=dict(chakras=d_chakras(),navel=d_navel(),allegory=d_allegory(),marspower=d_marspower(),mangal=d_mangal())
