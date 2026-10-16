from diagrams import box,arr,lab,fig

def d_studyhouses():
    s=box(90,8,240,40,['The 4th and 5th houses','carry a study reading'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Is Mercury or Jupiter','combust ("ast") or retrograde?'],'n')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'yes','end')+lab(310,126,'no','start')
    s+=box(10,134,180,64,['Sharp at 10 to 16,','then marks fall:','silly mistakes'],'r')
    s+=box(230,134,180,64,['Jupiter and Mercury','protect the marks','through the years'],'g')
    s+=box(30,222,360,58,['Mars can still rescue a score','with very little effort.','Saturn can shift the stream.'],'n')
    return fig(292,s,'The speaker\'s model for why a bright child\'s marks can fall after age ten.','Flowchart of Mercury and Jupiter affecting a child\'s study marks')

def d_vastugrid():
    cells={(0,0):(['NW','mind, thyroid'],'r'),(1,0):(['NORTH','ancestor help'],'g'),(2,0):(['NE','Brahma, navel'],'b'),
           (0,1):(['WEST','a guardian'],'n'),(1,1):(['HOUSE'],'e'),(2,1):(['EAST','entry, talk'],'n'),
           (0,2):(['SW','pitru-sthan'],'g'),(1,2):(['SOUTH'],'e'),(2,2):(['SE','fire, no smoke'],'r')}
    s=''
    for (cx,cy),(l,c) in cells.items():
        s+=box(5+cx*138,6+cy*98,134,90,l,c)
    return fig(306,s,'A simplified sketch of the vastu zones the speaker names; the full 32-deity grid is not reconstructed here.','Simplified compass grid of a few named vastu zones')

def d_failgood():
    s=box(90,8,240,40,['A child keeps failing,','or loses an admission'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Punish and force it through,','or let the planet take its due?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'force','end')+lab(310,126,'allow','start')
    s+=box(10,134,180,64,['A fee or a year lost','then health or the','body pays instead'],'r')
    s+=box(230,134,180,64,['Money or a year','is the full payment','body stays safe'],'g')
    s+=box(30,222,360,50,['His rule: pay in money or time,','it costs less than paying in health.'],'n')
    return fig(282,s,'The speaker\'s "sacrifice" framing for a failed exam or a lost admission fee.','Flowchart of letting a planet take its due through money or time, not health')

def d_examcolor():
    s=box(70,8,280,36,['Sign ruling the study house'],'b')
    rows=[('Mars debilitated','avoid red and black'),
          ('Saturn involved','avoid black, or wear it, by case'),
          ('Rahu involved','drink black tea or coffee, no milk'),
          ('Moon debilitated','avoid rice, milk and plain water'),
          ('Sun debilitated','avoid salty food and orange')]
    y=52
    for a,b in rows:
        s+=box(5,y,410,46,[a,b],'n')
        y+=54
    s+=box(5,y+4,410,40,['A full reading needs the exact chart;','this is only his worked-example pattern.'],'r')
    return fig(y+54,s,'A sample, not a full table, of the speaker\'s exam-day colour and food cautions.','Sample grid of exam-day colour cautions by afflicted planet')

def d_multichart():
    s=box(130,8,160,36,['One birth moment'],'b')
    labels=['Rashi','Chalit','Navamsa','KP']
    xs=[5,110,215,320]
    for i,nm in enumerate(labels):
        s+=box(xs[i],70,90,56,[nm,'chart'],'n')
        s+=arr(210,44,xs[i]+45,70)
    s+=box(30,150,360,56,['The same planet can land in a','different house on each chart'],'n')
    s+=arr(210,206,210,224)
    s+=box(30,224,360,50,['Read all of them together before','trusting any single placement.'],'b')
    return fig(284,s,'The speaker\'s point: no single chart is read alone near a sign\'s edge.','Diagram of one birth moment producing several charts to cross-check')

D=dict(studyhouses=d_studyhouses(),vastugrid=d_vastugrid(),failgood=d_failgood(),examcolor=d_examcolor(),multichart=d_multichart())
