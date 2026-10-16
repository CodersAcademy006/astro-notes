from diagrams import box, arr, lab, fig

def d_body():
    s=box(120,6,180,40,['Sun: right eye,','skull, confidence'],'n')+arr(210,46,210,64)
    s+=box(120,64,180,40,['Moon: left eye,','immunity'],'n')+arr(210,104,210,122)
    s+=box(90,122,240,40,['Mercury, Venus:','throat and chest'],'n')+arr(210,162,210,180)
    s+=box(110,180,200,40,['Mars: the navel,','the army'],'n')+arr(210,220,210,238)
    s+=box(90,238,240,40,['Jupiter: sacral chakra,','creation, the liver'],'n')+arr(210,278,210,296)
    s+=box(110,296,200,36,['Saturn: base of spine'],'n')+arr(210,332,210,350)
    s+=box(60,350,300,44,['Legs and feet: Uranus, Neptune,','Pluto, Indra, Varuna'],'b')
    return fig(410,s,'The speaker\'s head-to-foot body map: each planet governs one zone, from the skull down to the legs.','Vertical body map linking planets to body zones from head to feet')

def d_friend():
    s=box(90,6,240,44,['Space debris drifts','toward Earth'],'n')+arr(210,50,210,64)
    s+=box(60,64,300,44,["Jupiter's gravity catches","most of it, flings the rest"],'b')+arr(210,108,210,130)
    s+=box(90,130,240,40,['What still gets through'],'n')+arr(210,170,210,192)
    s+=box(40,192,340,48,['Mars absorbs the impact,','sits just in front of Earth'],'g')+arr(210,240,210,262)
    s+=box(90,262,240,36,['Earth stays safe'],'g')
    s+=box(30,312,360,56,['Hanuman silently took every hit in','Ram\'s story: this is why Mars is "friend"'],'n')
    return fig(380,s,'His asteroid-belt story for why Mars is Earth\'s closest friend: it quietly absorbs damage meant for Earth.','Flowchart of Jupiter and Mars protecting Earth from space debris')

def d_houses():
    s=box(150,6,120,34,['SUN'],'b')
    s+=arr(170,40,80,66)+arr(250,40,340,66)
    s+=box(5,66,160,36,['Friendlier houses'],'g')+box(255,66,160,36,['Harder houses'],'r')
    s+=box(5,110,160,44,["9th: Jupiter,","humble king"],'g')
    s+=box(5,162,160,44,['11th: Pluto,','good fortune'],'g')
    s+=box(5,214,160,44,['5th: own sign:','royal, generous'],'g')
    s+=box(255,110,160,44,['2nd: Venus drains','the king\'s energy'],'r')
    s+=box(255,162,160,44,['7th: Neptune hurts','marriage, vitality'],'r')
    s+=box(255,214,160,44,['10th: Saturn makes','a workaholic'],'r')
    return fig(274,s,'The Sun as a king visiting different deities\' houses: some placements help it rule well, others drain it.','Two-column diagram contrasting friendlier and harder Sun house placements')

def d_ishta():
    s=box(110,6,200,40,['Do you know your','protective deity?'],'b')
    s+=arr(150,46,90,74)+arr(270,46,330,74)+lab(100,66,'yes','end')+lab(320,66,'no','start')
    s+=box(5,74,190,54,['Connect directly,','use the exact method'],'g')
    s+=box(225,74,190,54,['Pick whatever practice','gives real peace'],'g')
    s+=arr(100,128,210,160)+arr(320,128,210,160)
    s+=box(60,160,300,44,['Protection runs automatically,','known or not'],'b')+arr(210,204,210,226)
    s+=box(30,226,360,56,['The one practical step: avoid the','opposing deity\'s domain or space'],'n')
    return fig(300,s,'His claim about Ishta: the protection is automatic either way; the only action needed is avoiding the opposing deity\'s space.','Decision flow for finding and using a personal protective deity')

def d_switch():
    s=box(130,6,160,34,['One cosmic "switch"'],'b')
    s+=arr(160,40,70,70)+arr(210,40,210,70)+arr(260,40,350,70)
    s+=box(5,70,130,60,['Chanting a','repeated name'],'n')
    s+=box(145,70,130,60,['A formless,','silent practice'],'n')
    s+=box(285,70,130,60,['A fixed ritual','or prayer'],'n')
    s+=arr(70,130,210,162)+arr(210,130,210,162)+arr(350,130,210,162)
    s+=box(40,162,340,50,['All are routes to the same place;','some are direct, some take longer'],'g')+arr(210,212,210,234)
    s+=box(60,234,300,40,['Neither route is "more spiritual"'],'n')
    return fig(284,s,'His "flip the switch" analogy: every tradition\'s practice is one more route to the same connection, not a competition.','Diagram of different ritual paths converging on one cosmic switch')

D=dict(body=d_body(),friend=d_friend(),houses=d_houses(),ishta=d_ishta(),switch=d_switch())
