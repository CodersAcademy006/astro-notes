from diagrams import box,arr,lab,fig
def d_sea():
    s=box(110,8,200,40,['NEPTUNE (Varuna)','the sea'],'b')+arr(150,48,95,72)+arr(270,48,325,72)
    s+=box(5,72,200,120,['GIVES','Intuition, grace','Treasure, oil, gems','Film, vitamins','Wide heart'],'g')
    s+=box(215,72,200,120,['TAKES','Storm, illusion','Drugs, alcohol','False promises','Long delays'],'r')
    s+=box(30,208,360,50,['Which side you get depends on','forgiving or hating (upper or lower sea)'],'n')
    s+=arr(105,192,105,208)+arr(315,192,315,208)
    return fig(268,s,'Neptune as the sea: it gives and it takes, and the speaker says your inner state decides which.','Neptune gives and takes')
def d_grace():
    s=box(110,8,200,40,['You want grace'],'n')+arr(150,48,95,72)+arr(270,48,325,72)
    s+=box(5,72,200,76,['Begging, trading','Forgive nothing','Pre-live results','Lower Neptune'],'r')
    s+=box(215,72,200,76,['Ask once and drop it','Forgive, forget','Accept bitter fruit','Upper Neptune'],'g')
    s+=arr(105,148,105,170)+arr(315,148,315,170)
    s+=box(5,170,200,64,['Quarrels for no reason','Wishes cancel'],'r')
    s+=box(215,170,200,64,['Grace, intuition','Help from strangers'],'g')
    return fig(244,s,'The two ways of asking, as the speaker contrasts them.','Comparison of begging and accepting')
def d_modes():
    s=box(5,8,130,50,['Movable','1 4 7 10'],'b')+box(145,8,130,50,['Fixed','2 5 8 11'],'b')+box(285,8,130,50,['Dual','3 6 9 12'],'b')
    s+=arr(70,58,70,80)+arr(210,58,210,80)+arr(350,58,350,80)
    s+=box(5,80,130,76,['Car is moving','Wedding departs','Storm in sign 4'],'n')
    s+=box(145,80,130,76,['Car is parked','Wedding, joining','a job, foundation','Sea blocked in 8'],'g')
    s+=box(285,80,130,76,['Moves and halts','Loans return,','items borrowed','Both sides in 12'],'r')
    s+=box(30,174,360,50,['Neptune stays about 14 years in one sign,','so no divorce or exit comes before that'],'b')
    return fig(234,s,'Movable, fixed and dual signs for timing and for Neptune in a water sign.','Three sign modes')
def d_houses():
    items=[('1','Low self-worth, addiction'),('2','Luxury, big ideas'),('3','Sibling trouble'),('4','Mother, damp home'),('5','Children differ'),('6','Enemies vanish'),('7','Live-in, own sign'),('8','Money not there'),('9','Guru, vices dropped'),('10','Confused work'),('11','Detached, social media'),('12','Spending, then money')]
    s=''
    for i,(n,t) in enumerate(items):
        x=5+(i%3)*139; y=8+(i//3)*70
        w=t.split(', ') if ', ' in t else [t]
        s+=box(x,y,133,62,['House '+n]+w,'n')
    return fig(294,s,'One line per house for Neptune, taken from the speaker\'s walk through the chart.','Neptune in each house')
def d_start():
    s=box(110,8,200,40,['Something is unclear'],'n')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Can you act on it? (Arjuna)'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(80,122,'yes','end')+lab(340,122,'no','start')
    s+=box(10,134,180,64,['Do the work with body','leave the head work','to God'],'g')
    s+=box(230,134,180,64,['Do not chase it','Leave it to the sea'],'g')
    s+=arr(100,198,100,222)+arr(320,198,320,222)
    s+=box(10,222,180,64,['Forgive and let go','Bokoju lesson'],'b')+box(230,222,180,64,['Aquamarine','details next class'],'n')
    return fig(296,s,'A starting path from the class. Section 13 has the full table with timestamps.','Flowchart for Neptune advice')
D=dict(sea=d_sea(),grace=d_grace(),modes=d_modes(),houses=d_houses(),start=d_start())
