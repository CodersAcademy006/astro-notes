from diagrams import box,arr,lab,fig

def d_tattva():
    items=[('Moon','water, slow,','content'),('Mars','fire, driven,','aggressive'),('Mercury','air, business,','fast talk'),
           ('Jupiter','space, wisdom,','discourse'),('Venus','indulgence,','perfume, ease'),('Saturn','shabby,','withdrawn'),
           ('Rahu','crooked,','restless talk'),('Ketu','silent,','mouth stuffed'),('Outer three','wandering,','on guard duty')]
    s=''
    for i,(p,l1,l2) in enumerate(items):
        x=5+(i%3)*138; y=8+(i//3)*84
        s+=box(x,y,130,74,[p,l1,l2],'n')
    s+=box(10,262,400,46,['Each planet, the speaker says, has its own','daily style. Catch yours before judging it.'],'b')
    return fig(318,s,'The speaker\'s rough style tag for each planet.','Grid of planets and their everyday behaviour style')

def d_aspect():
    s=box(70,8,280,44,['Which houses a planet\'s','aspect (drishti) reaches'],'b')
    rows=[('Sun, Moon, Mercury, Venus, Rahu','only the 7th house'),
          ('Mars','1st, 4th, 7th, 8th'),
          ('Jupiter','1st, 5th, 7th, 9th'),
          ('Saturn','1st, 3rd, 7th, 10th'),
          ('Varun (Neptune)','every house, he says')]
    y=56
    for p,h in rows:
        s+=box(5,y,410,46,[p,h],'n')
        y+=56
    return fig(y+10,s,'The speaker\'s list of which houses each planet\'s aspect (drishti) reaches.','List of planets and the houses their aspect reaches')

def d_reverse():
    s=box(90,8,240,40,['A planet sits exalted','by its sign'],'g')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Which house does it actually','sit in, friend or enemy?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'friendly house','end')+lab(310,126,'enemy house','start')
    s+=box(10,134,180,56,['Gives its full,','best result'],'g')
    s+=box(230,134,180,56,['Same exaltation,','opposite result'],'r')
    s+=box(30,210,360,54,['A strong sign can still act weak','once you check which house it rules.'],'n')
    return fig(284,s,'How an exalted planet can still give a reversed result, per the speaker\'s worked charts.','Flowchart of an exalted planet giving a reversed result by house')

def d_blind():
    s=box(90,8,240,40,['Trouble shows up','in your life'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['React, chase it, resent it,','or stay unaware?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'react','end')+lab(310,126,'let go','start')
    s+=box(10,134,180,56,['Saturn strikes','again, harder'],'r')
    s+=box(230,134,180,56,['Saturn quietly','arranges a fix'],'g')
    s+=arr(100,190,100,214)+arr(320,190,320,214)
    s+=box(10,214,180,46,['More struggle,','more loss'],'r')
    s+=box(230,214,180,46,['A "coincidence"','solves it'],'g')
    return fig(284,s,'The speaker\'s picture of Saturn: go unaware ("blind") rather than chase the trouble.','Flowchart of reacting to trouble versus letting Saturn quietly fix it')

def d_donate():
    items=[('Saturn','black dal'),('Jupiter','yellow dal'),('Venus','white chana'),('Mercury','moong dal'),
           ('Mars','red dal/lentil'),('Moon','rice'),('Sun','wheat')]
    s=''
    for i,(p,g) in enumerate(items):
        x=5+(i%2)*205; y=8+(i//2)*58
        s+=box(x,y,195,48,[p,g],'n')
    s+=box(10,246,400,46,['Give the grain of the sign in that house','at a school, before an exam or paper.'],'b')
    return fig(302,s,'The speaker\'s grain-by-planet donation list for exam-day remedies.','Grid pairing each planet with a grain to donate')

D=dict(tattva=d_tattva(),aspect=d_aspect(),reverse=d_reverse(),blind=d_blind(),donate=d_donate())
