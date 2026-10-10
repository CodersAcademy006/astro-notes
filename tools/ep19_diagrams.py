from diagrams import box,arr,lab,fig
def d_oneeye():
    s=box(110,8,200,40,['VENUS: one eye'],'r')
    for x in (50,150,270,370): s+=arr(210,48,x,72)
    s+=box(5,72,90,76,['No two-sided','view, no','judging'],'n')+box(105,72,90,76,['Very slow','243 day spin,','re-checks'],'n')+box(205,72,130,76,['Moves backwards','upside-down talk','that proves right'],'n')+box(345,72,70,76,['One idea','sticks'],'n')
    s+=box(30,166,360,50,['Saturn gives the second eye','Respect workers and Saturn helps Venus'],'g')
    s+=arr(210,148,210,166)
    s+=box(30,232,360,50,['Test: you explain, they do the opposite','Venus is afflicted, remedies needed'],'r')
    return fig(292,s,'The one-eyed god and what it looks like in a person.','Diagram of Venus traits')
def d_signs():
    s=box(110,8,200,36,['Venus in the sign of...'],'b')
    for x in (70,210,350): s+=arr(210,44,x,66)
    s+=box(5,66,130,130,['Best','','12 Ketu: best','2 own sign: party','10, 11 Saturn:','excellent'],'g')
    s+=box(145,66,130,130,['Mixed','','7: wealth, wilful','8: "I am emperor"','9 Jupiter:','well-mannered'],'n')
    s+=box(285,66,130,130,['Bad','','3 Mercury: empty','4 Moon: breaks','5 Sun: veiled','6 Rahu: ruin'],'r')
    s+=box(30,214,360,50,['Fix a bad sign: Ketu help (dog, cow),','white topaz, and the Venus remedies'],'b')
    s+=arr(350,196,350,214)
    return fig(274,s,'Venus by sign, as the speaker rates it.','Chart of Venus in different signs')
def d_chain():
    names=['Food','Rasa','Blood','Flesh','Fat','Bone','Marrow','Shukra']
    s=''
    for i,n in enumerate(names):
        c=i%4 if i<4 else 3-(i%4)
        x=5+c*104; y=8 if i<4 else 90
        s+=box(x,y,92,44,[n],'g' if n=='Shukra' else 'n')
        if i<3: s+=arr(x+92,y+22,x+104,y+22)
        elif i==3: s+=arr(x+46,y+44,x+46,90)
        elif i<7: s+=arr(x,y+22,x-12,y+22)
    s+=box(30,164,360,64,['If food does not become dhatu:','semen loss, menstrual trouble, dryness,','weak aura, early ageing'],'r')
    s+=arr(51,134,51,164)
    return fig(238,s,'The body chain the speaker gives, read left to right then back. Venus rules the last step.','Body tissue chain ending in shukra')
def d_fix():
    rows=[('Sun','Bow to fire and elders'),('Moon','Do not tell mother everything'),('Mars','Stay close to a brother'),('Mercury','Green fodder to the cow'),('Jupiter','No ego fights at home'),('Saturn','Fresh food to workers'),('Rahu','Do not fight mother-in-law or boss'),('Ketu','Serve dog, clean bedroom')]
    s=''
    for i,(p,r) in enumerate(rows):
        y=8+i*44
        s+=box(5,y,100,36,[p],'n')+arr(105,y+18,135,y+18)+box(135,y,280,36,[r],'g')
    return fig(366,s,'If Venus hurts this planet, do this. A starting guide, check the chart.','List of fixes by planet')
def d_topaz():
    s=box(110,8,200,40,['White topaz','longest finger'],'b')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Any other planet at fault?'],'b')
    s+=arr(110,106,60,134)+arr(210,106,210,134)+arr(310,106,360,134)
    s+=box(5,134,110,60,['Saturn:','add a blue','shade'],'n')+box(155,134,110,60,['Jupiter:','add a yellow','shade'],'n')+box(305,134,110,60,['None:','pure white'],'g')
    s+=box(30,214,360,60,['Silver (Friday morning), or white gold, platinum','Natural stone only. Heat-treated is no use.'],'b')
    s+=arr(210,194,210,214)
    return fig(284,s,'Choosing the white topaz, as the speaker describes it.','Decision tree for white topaz')
D=dict(oneeye=d_oneeye(),signs=d_signs(),chain=d_chain(),fix=d_fix(),topaz=d_topaz())
