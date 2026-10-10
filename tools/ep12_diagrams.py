from diagrams import box,arr,lab,fig
def d_pull():
    s=box(110,8,200,40,['SUN','pulls everything in'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['JUPITER pulls back','keeps Earth from falling in'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['SATURN holds Jupiter','with Indra, Varuna, Yama'],'n')+arr(210,164,210,182)
    s+=box(30,182,360,52,['Life is the rope in the middle','Saturn sits behind Jupiter: in the dark'],'g')
    return fig(244,s,'The speaker\'s tug of war: Sun, Jupiter and Saturn.','Flowchart of the Sun Jupiter Saturn tug of war')
def d_court():
    s=box(110,8,200,52,['SATURN: the judge','gives the verdict'],'r')
    s+=arr(150,60,95,86)+arr(270,60,325,86)
    s+=box(5,86,200,64,['RAHU: the summons','punisher, covers','the Sun'],'n')
    s+=box(215,86,200,64,['KETU: the lawyer','explains, protects,','also punishes'],'n')
    s+=box(30,170,360,52,['Boast about luck: Saturn rules against you','Stay quiet: it rules for you'],'b')
    s+=arr(105,150,105,170)+arr(315,150,315,170)
    return fig(232,s,'Saturn as judge, with Rahu and Ketu as his agents.','Court picture of Saturn Rahu Ketu')
def d_letgo():
    s=box(110,8,200,40,['An area Saturn looks at'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['You push, count, ask, plan'],'r')+arr(210,106,210,124)
    s+=box(60,124,300,40,['It fails, drags or turns against you'],'r')
    s+=arr(210,164,210,182)+box(60,182,300,40,['Instead: leave it to a guru','or deity, ask once'],'g')
    s+=arr(210,222,210,240)+box(60,240,300,40,['It comes as luck, by surprise'],'g')
    return fig(290,s,'Where Saturn sits or looks, the speaker says do not poke.','Flowchart of letting go in a Saturn area')
def d_stone():
    s=box(110,8,200,40,['Saturn needs a stone?'],'b')+arr(210,48,210,66)
    s+=box(30,66,360,40,['Is sign 10 or house 8 a problem?'],'b')
    s+=arr(110,106,80,130)+arr(310,106,340,130)+lab(90,124,'no','end')+lab(330,124,'yes','start')
    s+=box(10,130,190,64,['Blue sapphire','right shade, 5 to 7 ratti','silver'],'g')
    s+=box(220,130,190,64,['Not pure sapphire','blue-shade topaz','with another planet'],'r')
    s+=box(10,210,400,50,['A stone corrects like glasses, it does not strengthen.','The whole chart decides, not one placement.'],'n')
    return fig(270,s,'The speaker\'s checks before the Saturn stone. Not advice to buy one.','Decision tree for the Saturn stone')
def d_sade():
    s=box(110,8,200,40,['Find your Moon sign'],'b')+arr(210,48,210,66)
    for i,(t,x,c) in enumerate([(['Saturn in','sign before','Moon sign','2.5 years'],5,'n'),(['Saturn on','Moon sign','2.5 years','dark mind'],113,'r'),(['Saturn in','next sign','2.5 years','going dhaiya'],221,'n')]):
        s+=box(x,66,100,84,t,c)
    s+=box(329,66,86,84,['Total','7.5 years'],'b')
    s+=box(30,170,360,64,['Outcome depends on the whole birth chart:','Rama and Ravana, Krishna and Kansa','had it together, results opposite'],'n')
    s+=box(30,250,360,50,['Have a guru, carry the Sun (confidence),','keep matters secret'],'g')
    return fig(310,s,'Sade sati as the speaker describes it.','Timeline of sade sati')
D=dict(pull=d_pull(),court=d_court(),letgo=d_letgo(),stone=d_stone(),sade=d_sade())
