from diagrams import box,arr,lab,fig
def d_karma():
    s=box(90,8,240,40,['Wish or do harm to someone'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,46,['The debt is logged,','not forgiven just because it is forgotten'],'b')+arr(210,112,210,130)
    s+=box(40,130,340,46,['Returns in a later birth,','often with the roles reversed'],'n')+arr(210,176,210,194)
    s+=box(10,194,185,56,['Victim becomes the "son"','illness collects the debt in full'],'g')+box(225,194,185,56,['Wrongdoer becomes the parent','pays by grieving, not by dying'],'r')
    return fig(264,s,'How the opening story frames suffering: karma as an account that always closes, often across lifetimes.','Flowchart of the karma story: wished harm returns later with reversed roles')
def d_ishta_grid():
    cells=[(['1 Mars','Hanuman'],'g'),(['2 Venus','Lakshmi'],'g'),(['3 Mercury','Durga /','Saraswati'],'b'),(['4 Moon','Shiva'],'b'),
           (['5 Sun','Vishnu'],'g'),(['6 Rahu','Durga'],'b'),(['7 Varuna','Varuna /','Lakshmi'],'b'),(['8 Mars co.','Hanuman or','Rama'],'n'),
           (['9 Jupiter','Guru photo'],'g'),(['10 Saturn','Shani'],'n'),(['11 Pluto co.','Hanuman'],'g'),(['12 Ketu','Ganesh'],'g')]
    s=''
    for i,(l,c) in enumerate(cells):
        col=i%4; row=i//4
        s+=box(5+col*103,6+row*96,98,88,l,c)
    return fig(298,s,"A quick-reference grid: which sign in the 9th house points to which planet and deity, the speaker's simplified starting table.",'Grid of sign number to planet and suggested Ishta deity')
def d_swayam():
    s=box(90,8,240,40,['Your own karaka planet sits','exalted in a house'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['That quality is already strong,','natively, inside you'],'n')
    s+=arr(150,106,90,134)+arr(270,106,330,134)+lab(100,126,'aware','end')+lab(330,126,'unaware','start')
    s+=box(10,134,180,64,['You recognise it:','"aham brahmasmi",','you become your own Ishta'],'g')
    s+=box(230,134,180,64,['You keep searching outside,','chasing the world,','and never notice it'],'r')
    return fig(214,s,'The "swayam Ishta" idea: an exalted planet in the right house can mean you already are what you would pray to, if you notice it.','Flowchart of becoming your own Ishta through an exalted planet')
def d_mangal():
    s=box(90,8,240,36,['Mars sits in house 1, 4, 7, 8 or 12'],'r')+arr(210,44,210,66)
    s+=box(60,66,300,40,['This chart is "manglik"'],'b')
    s+=arr(150,106,90,134)+arr(270,106,330,134)+lab(100,126,'Shani also there','end')+lab(330,126,'Shani not there','start')
    s+=box(5,134,190,56,['Dosha cancelled.','Marry manglik or not,','equally safe.'],'g')
    s+=box(225,134,190,56,['Dosha active.','Fire pheras will "ignite"','it at the wedding.'],'n')
    s+=arr(320,190,320,212)
    s+=box(220,212,195,56,['No-fire marriage (court,','Anand Karaj) carries no','dosha at all.'],'g')
    return fig(282,s,'Checking for a manglik placement and the two remedies offered: cancel it with Saturn, or skip the fire that activates it.','Decision tree for the manglik Mars placement')
def d_vakri():
    s=box(20,8,180,36,['MERCURY retrograde'],'b')+box(220,8,180,36,['JUPITER retrograde'],'b')
    s+=arr(110,44,110,66)+arr(310,44,310,66)
    s+=box(10,66,200,76,['Cannot stay quiet.','Argues, repeats,','over-explains.','Needs a stone just','to feel settled.'],'r')
    s+=box(210,66,200,76,["Studies collapse,",'especially at 15-16.',"\"I know, don't",'teach me.\" Ego','inflates fast.'],'r')
    s+=arr(110,142,110,164)+arr(310,142,310,164)
    s+=box(10,164,200,56,['Green items to the','person or their sister:','saunf, bangle, sweet.'],'g')+box(210,164,200,56,['Awareness of the ego,','plus general guru-','and-spouse service.'],'g')
    return fig(234,s,"Two retrograde planets covered as live examples, before the full retrograde class promised next time.",'Side by side comparison of Mercury retrograde and Jupiter retrograde')
def d_fate():
    s=box(110,8,200,36,['Change a fate not yet written'],'b')
    for x in (70,210,350): s+=arr(210,44,x,66)
    s+=box(5,66,130,64,['Pure effort.','Flies alone,','dies before arriving.'],'r')+box(145,66,130,64,['Pure prayer.','Begs and waits,','life wasted.'],'r')+box(285,66,130,76,["Rides in a guru's",'pocket. Grace carries','it there effortlessly.'],'g')
    s+=arr(350,142,350,164)
    s+=box(230,164,185,50,['Best route: proximity','to where grace already flows.'],'g')
    return fig(224,s,"The mosquito story, the class's answer to changing a destiny that is not already fixed.",'Flowchart of three ways to change an undestined fate: effort, prayer, or proximity to grace')
D=dict(karma=d_karma(),grid=d_ishta_grid(),swayam=d_swayam(),mangal=d_mangal(),vakri=d_vakri(),fate=d_fate())
