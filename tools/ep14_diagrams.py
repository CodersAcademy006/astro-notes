from diagrams import box,arr,lab,fig
def d_family():
    s=box(110,8,200,40,['SUN: the soul, the father'],'b')+arr(210,48,210,100)
    s+=box(5,100,125,60,['JUPITER','calm, the guru'],'g')+box(145,100,130,60,['MERCURY','the child mind'],'n')+box(290,100,125,60,['RAHU','wild, blue'],'r')
    s+=arr(130,130,145,130)+arr(290,130,275,130)
    s+=arr(210,160,210,185)+box(30,185,360,50,['Yellow plus blue makes green.','Set Jupiter and Rahu, and Mercury behaves.'],'g')
    return fig(250,s,'Mercury is the child of the Sun, steadied by Jupiter and shaken by Rahu.','Sun, Jupiter, Rahu and Mercury')
def d_company():
    s=box(145,8,130,40,['MERCURY','copies its company'],'n')
    for i,(a,b,c) in enumerate([('Saturn','dull,','heavy'),('Mars','bold,','commanding'),('Rahu','restless,','tricky'),('Jupiter','wise,','steady')]):
        x=5+i*104; s+=arr(210,48,x+48,90)+box(x,90,96,70,[a,b,c],'r' if a=='Rahu' else 'n')
    s+=box(30,185,360,50,['Mercury becomes the company it keeps.','Choose your company.'],'b')
    return fig(250,s,'Mercury takes the nature of whoever it sits with.','Mercury and company')
def d_ear():
    s=box(110,8,200,40,['Words said into the ear'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Ear is the sky element, always open'],'n')
    s+=arr(150,106,105,124)+arr(270,106,315,124)
    s+=box(5,124,200,76,['Calm and loving','Child sleeps, stays well','Exam goes well'],'g')+box(215,124,200,76,['Shouted or fearful','"What of my paper?"','Child falls ill'],'r')
    s+=box(30,218,360,50,['Same for you: whisper peace','into your own ear, alone'],'b')
    return fig(280,s,'What goes into the ear acts as an order.','Ear words become orders')
def d_twelfth():
    s=box(110,8,200,40,['Mercury in the 12th house'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Which sign is it in?'],'n')
    s+=arr(150,106,105,124)+arr(270,106,315,124)
    s+=box(5,124,200,66,['Sign 3, 9 or 12','Calmer, often fine'],'g')+box(215,124,200,66,['Any other sign','Highly negative'],'r')
    s+=arr(315,190,315,208)+box(30,208,360,50,['Pierce the nose centre for 100 hours,','silver stud. Emerald for a lasting fix.'],'b')
    return fig(270,s,'The speaker\'s test for a 12th-house Mercury.','Flowchart for Mercury in 12th')
def d_ladder():
    rows=[('1. Habits: hair tied, talk, clean north','n'),('2. Give: green moong, secret giving, elders','n'),('3. Alum gargle for 43 days if work is stuck','b'),('4. Emerald, once for life, if the chart suits','g')]
    s=''
    for i,(t,c) in enumerate(rows):
        y=8+i*54; s+=box(20,y,380,40,[t],c)
        if i<3: s+=arr(210,y+40,210,y+54)
    return fig(228,s,'From small daily fixes up to the lasting one.','Ladder of Mercury remedies')
D=dict(family=d_family(),company=d_company(),ear=d_ear(),twelfth=d_twelfth(),ladder=d_ladder())
