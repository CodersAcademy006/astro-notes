from diagrams import box,arr,lab,fig

def d_compare():
    s=box(110,8,200,40,['You see someone','ahead of you'],'n')+arr(210,48,210,66)
    s+=box(70,66,280,40,['Mind runs back into the past','(family, old hurts, old wins)'],'r')+arr(210,106,210,124)
    s+=box(90,124,240,40,['A natal retrograde planet','can now grab power'],'b')
    s+=arr(160,164,105,196)+arr(260,164,315,196)
    s+=box(10,196,190,50,['Catch yourself','no comparison'],'g')+box(220,196,190,50,['Keep comparing','keep chasing'],'r')
    s+=arr(105,246,105,268)+arr(315,246,315,268)
    s+=box(10,268,190,50,['Planet stays calm','life moves straight'],'g')+box(220,268,190,50,['Planet turns vakri','life pulled backward'],'r')
    return fig(338,s,'The speaker\'s rule: comparison is what switches on a retrograde planet\'s pull.','Flowchart: comparing with others can switch on a retrograde planet')

def d_mona():
    s=box(130,8,160,36,['Two people','walking in a park'],'b')
    s+=box(15,60,170,60,['MONA','runs ahead fast','(10 km/h)'],'g')
    s+=box(235,60,170,60,['MINAL','walks on, slower','(2 km/h)'],'n')
    s+=arr(100,120,100,150)+arr(320,120,320,150)
    s+=box(15,150,170,46,['Both move forward','the whole time'],'n')
    s+=box(235,150,170,46,['Both move forward','the whole time'],'n')
    s+=box(30,212,360,64,['From Mona\'s fast pace,','Minal looks like she is','falling behind'],'r')
    s+=box(30,292,360,40,['That look of "going backward"','is what a retrograde planet is'],'b')
    return fig(350,s,'The speaker\'s park analogy: a retrograde planet never truly reverses, it only looks that way next to a faster neighbour.','Diagram of two walkers at different speeds explaining retrograde motion')

def d_filter():
    s=box(110,8,200,36,['Rays from a planet'],'n')+arr(210,44,210,66)
    s+=box(70,66,280,40,['A clean, matched stone','filters, does not boost'],'b')
    s+=arr(130,106,90,138)+arr(290,106,330,138)+lab(100,128,'clean','end')+lab(300,128,'cracked','start')
    s+=box(10,138,190,56,['Full, even flow','through to the body'],'g')+box(220,138,190,56,['Patchy, uneven flow','some rays spill away'],'r')
    s+=arr(105,194,105,222)+arr(315,194,315,222)
    s+=box(10,222,190,50,['Dosha filtered','steady relief'],'g')+box(220,222,190,50,['Only partial relief','for a lifetime'],'r')
    s+=box(30,288,360,40,['A stone never raises or lowers power.','It only filters how much gets through.'],'n')
    return fig(338,s,'The speaker\'s tea-strainer picture of what a gemstone does.','Flowchart of a gemstone filtering a planet\'s rays, clean versus cracked stone')

def d_universal():
    s=box(90,8,240,40,['A planet is retrograde','at your birth'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Does it own a 3rd, 6th, 8th','or 12th house placement?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'yes','end')+lab(310,126,'no','start')
    s+=box(10,134,180,64,['Caution zone','can side-effect','like a steroid too'],'r')
    s+=box(230,134,180,64,['Safer to fit','its stone is the','main fix'],'g')
    s+=arr(100,198,100,222)+arr(320,198,320,222)
    s+=box(10,222,180,50,['Still often needed,','case by case'],'n')+box(230,222,180,50,['Wear the matching','stone, well fitted'],'n')
    s+=box(30,288,360,40,['His universal law: a retrograde planet','always needs its matching stone.'],'b')
    return fig(338,s,'The speaker\'s decision path for whether to fit a stone for a retrograde planet.','Flowchart for deciding on a gemstone for a retrograde planet')

def d_maturity():
    items=[('Moon','5'),('Sun','10'),('Jupiter','16'),('Venus','27'),('Mars','28'),('Mercury','32'),('Saturn','36'),('Rahu','42'),('Ketu','48')]
    s=''
    for i,(p,yr) in enumerate(items):
        x=5+(i%3)*138; y=8+(i//3)*76
        s+=box(x,y,130,64,[p,'age '+yr],'n')
    s+=box(10,246,400,46,['Before this age, still forming.','After it, dosha effects can bite.'],'b')
    return fig(302,s,'The speaker\'s ages at which each planet fully "matures" in a person.','Grid of ages at which each planet matures')

D=dict(compare=d_compare(),mona=d_mona(),filter=d_filter(),universal=d_universal(),maturity=d_maturity())
