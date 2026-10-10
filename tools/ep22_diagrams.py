from diagrams import box,arr,lab,fig
def d_split():
    s=box(110,8,200,40,['Body is about 72% water'],'b')+arr(150,48,95,76)+arr(270,48,325,76)
    s+=box(10,76,190,86,['Body share: 72','On the Moon a 60 kg','person weighs 10 kg','one sixth of 72 is 12'],'n')
    s+=box(220,76,190,86,['Mind share: 12','Rules the whole life','Thoughts come from','nowhere, not chosen'],'g')
    s+=arr(105,162,105,182)+arr(315,162,315,182)
    s+=box(10,182,190,56,['Water dries with age','90, 80, 72, then 60'],'r')+box(220,182,190,56,['Pineal gland dries','common sense fades'],'r')
    s+=box(30,254,360,44,['Fix the Moon in the chart,','the mind and the water follow'],'b')
    return fig(308,s,'The speaker\'s water and mind split, as he explains it.','Diagram of 72 percent body water and 12 percent mind')
def d_grid():
    items=[('1','Clay pot'),('2','Spring'),('3','Sandy soil'),('4','Pure milk'),('5','Canal'),('6','Handpump'),('7','Field'),('8','Mud, grave'),('9','Sea'),('10','Mountain'),('11','Drain'),('12','Rain, dew')]
    s=''
    for i,(n,p) in enumerate(items):
        x=5+(i%4)*104; y=8+(i//4)*66
        c='g' if n in('1','2','4','9') else ('r' if n in('5','8','11') else 'n')
        s+=box(x,y,96,54,['House '+n,p],c)
    s+=box(30,214,360,50,['Green: good. Red: troubled. Plain: mixed.','Sign, degree and aspects change the result.'],'b')
    return fig(274,s,'The water the Moon is like in each house, per the speaker.','Grid of Moon water types by house')
def d_filter():
    s=box(110,8,200,40,['A thought arrives'],'n')+arr(210,48,210,66)
    s+=box(70,66,280,40,['Third eye filter (the Moon)'],'b')
    s+=arr(130,106,95,140)+arr(290,106,325,140)+lab(100,128,'clear','end')+lab(320,128,'blocked','start')
    s+=box(10,140,190,52,['Witness mind','lets it pass'],'g')+box(220,140,190,52,['Thought hits the','root chakra'],'r')
    s+=arr(105,192,105,214)+arr(315,192,315,214)
    s+=box(10,214,190,64,['Dropped into the','ground, it ends'],'g')+box(220,214,190,64,['Stored karma sprouts','into events in life'],'r')
    return fig(288,s,'The third eye as a filter for thoughts, in the speaker\'s account.','Flowchart of the third eye filter')
def d_tara():
    s=box(110,8,200,40,['Moon and Tara'],'n')+arr(210,48,210,66)
    s+=box(70,66,280,40,['Son born: Mercury (Budh)'],'b')+arr(210,106,210,124)
    s+=box(50,124,320,40,['Mercury fights the Moon','mother and daughter clash'],'r')+arr(210,164,210,182)
    s+=box(50,182,320,40,['Moon with Mercury in a girl\'s chart'],'b')
    s+=arr(110,222,70,246)+arr(210,222,210,246)+arr(310,222,350,246)
    s+=box(5,246,130,70,['Sandy water','in a glass','bottle'],'g')+box(145,246,130,70,['Give green','things, secretly','give notes'],'g')+box(285,246,130,70,['Stop arguing,','emerald if','Mercury weak'],'g')
    return fig(326,s,'Why Moon and Mercury clash and the remedies named for it.','Flowchart of Moon Mercury conflict and remedies')
def d_charge():
    s=box(110,8,200,40,['Feet off the earth'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Plain water in both hands','at the heart'],'n')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Breathe in, draw one wish','from the cosmos (peace)'],'n')+arr(210,164,210,182)
    s+=box(60,182,300,40,['Blow out gently, say the name'],'n')+arr(210,222,210,240)
    s+=box(60,240,300,40,['Person drinks the water'],'g')
    s+=box(10,298,400,52,['One fair reason, one request at a time.','A new request needs the first one cleared.'],'r')
    return fig(360,s,'The water charging steps, as the speaker describes them.','Flowchart of water charging steps')
D=dict(split=d_split(),grid=d_grid(),filter=d_filter(),tara=d_tara(),charge=d_charge())
