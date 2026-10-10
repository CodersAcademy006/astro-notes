from diagrams import box,arr,lab,fig
def d_cow():
    s=box(110,8,200,40,['Cow and lion in the marsh'],'b')
    s+=arr(160,48,105,72)+arr(260,48,315,72)
    s+=box(10,72,190,60,['Cow (Venus)','has a guru and owner','who comes looking'],'g')+box(220,72,190,60,['Lion (wrathful Jupiter)','"I need nobody"','no friend, no guru'],'r')
    s+=arr(105,132,105,156)+arr(315,132,315,156)
    s+=box(10,156,190,50,['Rope around the neck,','pulled out'],'g')+box(220,156,190,50,['Stuck, dies slowly','in the marsh'],'r')
    s+=box(30,224,360,50,['Gu = darkness, ru = light.','The guru takes you from the marsh to light'],'n')
    return fig(284,s,'The cow and lion story, as the speaker tells it.','Flow of the cow and lion story')
def d_belly():
    s=box(110,8,200,40,['Jupiter: belly below the navel'],'b')
    s+=arr(160,48,105,72)+arr(260,48,315,72)
    s+=box(10,72,190,70,['Jupiter works','Vacuum cleaner pulls','waste down and out','(apana air)'],'g')+box(220,72,190,70,['Jupiter disturbed','Food comes up:','sour belch, heartburn','vomiting, gas'],'r')
    s+=arr(105,142,105,166)+arr(315,142,315,166)
    s+=box(10,166,190,56,['Gut feeling is clear','Black dal digests','Head is light'],'g')+box(220,166,190,56,['Heavy head, headache','Decisions will not come','Black dal sits badly'],'r')
    s+=box(30,238,360,50,['Speaker\'s order: settle the belly,','then the brain works and decisions arrive'],'n')
    return fig(298,s,'Jupiter in the gut, per the speaker. These are his claims, not medical advice.','Flow of Jupiter working or disturbed in the belly')
def d_ne():
    s=''
    cells={(0,0):(['NW'],'e'),(1,0):(['NORTH','plants ok','only if needed'],'n'),(2,0):(['NORTH-EAST','JUPITER','open, empty,','clean, fragrant'],'g'),
           (0,1):(['WEST'],'e'),(1,1):(['HOUSE'],'e'),(2,1):(['EAST'],'e'),
           (0,2):(['SOUTH-WEST','keep sound,','no cracks'],'n'),(1,2):(['SOUTH'],'e'),(2,2):(['SOUTH-EAST'],'e')}
    for (cx,cy),(t,c) in cells.items():
        s+=box(5+cx*138,8+cy*100,130,92,t,c)
    s+=box(5,316,410,60,['North-east: no storage, kitchen, toilet,','red or yellow, thorny plants or home temple fire'],'b')
    return fig(386,s,'Where Jupiter lives in the house, per the speaker.','Compass grid with north-east for Jupiter')
def d_aspect():
    s=box(130,8,160,44,['Jupiter sits here','(houses 1 to 12)'],'b')
    s+=arr(150,52,80,84)+arr(210,52,210,84)+arr(270,52,340,84)
    s+=box(5,84,135,66,['5th from seat','full power','eats negatives'],'g')+box(150,84,120,66,['7th from seat','weaker, about 75','(his figure)'],'n')+box(280,84,135,66,['9th from seat','full power','eats negatives'],'g')
    s+=box(30,170,360,66,['In the seat itself he does not let','others run, and eats that house:','7th = marriage, 9th = father, 1st = self'],'r')
    s+=box(30,254,360,46,['He modifies what each planet there does','but always gives something'],'n')
    return fig(310,s,'Jupiter\'s glance in the triangle, as taught.','Diagram of Jupiter aspects on 5th, 7th and 9th')
def d_topaz():
    s=box(110,8,200,40,['Think of a topaz?'],'b')+arr(210,48,210,66)
    s+=box(40,66,340,44,['Read the full chart first','sign 9 is Jupiter\'s home'],'n')+arr(210,110,210,128)
    s+=box(40,128,340,44,['Do signs 10 or 11 fall in','an enemy house, the 8th, 2nd or 9th?'],'b')
    s+=arr(110,172,80,200)+arr(310,172,340,200)+lab(70,192,'yes','end')+lab(350,192,'no','start')
    s+=box(5,200,200,76,['Do not wear it','Speaker says: court cases,','eye risk, trouble in','the 8th house'],'r')+box(215,200,200,76,['May be worn','gold, Thursday morning','Pitambari if plain','topaz does not suit'],'g')
    s+=box(30,294,360,46,['Speaker\'s rule. Needs a trained reading.'],'n')
    return fig(350,s,'The speaker\'s topaz check, kept short.','Decision tree for wearing topaz')
D=dict(cow=d_cow(),belly=d_belly(),ne=d_ne(),aspect=d_aspect(),topaz=d_topaz())
