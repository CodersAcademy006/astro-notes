from diagrams import box, arr, lab, fig

def d_pipe():
    s = box(110,8,200,36,['Your throat','where Mercury sits'],'b')
    s += arr(210,44,210,64)
    s += box(60,64,300,40,['A hollow pipe: carries anything','placed in it, keeps nothing'],'n')
    items=[(5,'Truth','g'),(108,'Lies','r'),(211,'Poison','r'),(314,'Nectar','g')]
    for x,t,c in items:
        s += arr(x+48,104,x+48,122)
        s += box(x,122,97,36,[t],c)
    s += ''.join(arr(x+48,158,210,176) for x,t,c in items)
    s += box(60,176,300,36,['No judgment: treats all the same'],'n')
    s += arr(210,212,210,230)
    s += box(40,230,340,40,['Only one thing matters:','does it land clearly?'],'b')
    return fig(282,s,'Mercury as the speaker describes it: an empty channel at the throat that carries whatever is put into it, good or bad, without judgment.','Flowchart of Mercury as a neutral pipe carrying truth, lies, poison or nectar without judgment')

def d_birth():
    s = box(60,8,300,36,['Jupiter and Tara: a married pair'],'n')
    s += arr(210,44,210,62)
    s += box(40,62,340,40,['The Moon falls for Tara:','a child comes of it, not by her fault'],'r')
    s += arr(210,102,210,120)
    s += box(90,120,240,36,['Mercury is born: a child','the family line does not own'],'b')
    s += arr(130,156,70,186) + arr(290,156,350,186)
    s += box(10,186,150,50,['Jupiter: wisdom','colour yellow'],'n')
    s += box(260,186,150,50,['Rahu: the sky','colour blue'],'n')
    s += arr(85,236,180,258) + arr(335,236,240,258)
    s += box(100,258,220,36,['Mixed through the Moon'],'b')
    s += arr(210,294,210,312)
    s += box(90,312,240,40,['Green: the colour of Mercury'],'g')
    return fig(362,s,'The speaker’s story for why Mercury is green: Jupiter’s yellow and the sky’s blue mixed through the Moon.','Flowchart of the mythological birth of Mercury and why its colour is green')

def d_scale():
    s = box(10,16,180,64,['MERCURY','intellect, speech,','trade, no judgment'],'b')
    s += box(230,16,180,64,['VENUS','enjoyment, comfort,','enjoy what you have'],'g')
    s += arr(100,80,100,100) + arr(320,80,320,100)
    s += '<line x1="40" y1="122" x2="380" y2="122" class="ln" stroke-width="3"/>'
    s += '<path d="M210,124 L190,154 L230,154 Z" class="n"/>'
    s += box(60,174,300,50,['One pan too low and the other rises:','intellect with nothing to enjoy, or','enjoyment with no sense to use it'],'n')
    s += arr(210,224,210,244)
    s += box(60,244,300,40,['Keep both pans level to feel','what your money and work give you'],'g')
    return fig(300,s,'The speaker’s balance-scale picture: Mercury (intellect, trade) and Venus (enjoyment) must stay level, or one cancels the other.','Seesaw diagram of Mercury and Venus needing to balance')

def d_atomic():
    s = box(100,6,220,34,['A coincidence he notes'],'b')
    s += arr(130,40,80,64) + arr(290,40,340,64)
    s += box(10,64,140,50,['MERCURY','atomic number 80'],'n')
    s += box(270,64,140,50,['GOLD','atomic number 79'],'n')
    s += box(60,126,300,34,['Both sit together, next to the Sun'],'n')
    s += arr(210,160,210,180)
    s += box(10,180,130,66,['URANUS','uranium','no. 92'],'n')
    s += box(145,180,130,66,['NEPTUNE','neptunium','no. 93'],'n')
    s += box(280,180,130,66,['PLUTO','plutonium','no. 94'],'n')
    s += arr(75,246,75,268) + arr(210,246,210,268) + arr(345,246,345,268)
    s += box(10,268,400,40,['He reads this as the cosmos and matter','sharing the same hidden numbers'],'b')
    return fig(328,s,'A numeric coincidence the speaker offers: Mercury and Gold, and Uranus, Neptune and Pluto, line up with their namesake elements’ atomic numbers.','Diagram pairing planets with the atomic numbers of their namesake elements')

def d_houses():
    s = box(110,6,200,34,['Mercury by house, in brief'],'b')
    s += box(5,54,200,40,['Its own houses: 3rd, 6th','trade and speech do well'],'g')
    s += box(215,54,200,40,['4th/12th shields you','from a bad Rahu or Ketu'],'g')
    s += box(5,104,200,40,['6th and 12th together:','never go into business'],'r')
    s += box(215,104,200,40,['7th: kills the warmth','between husband and wife'],'r')
    s += box(5,154,200,40,['12th: tends to','end a marriage'],'r')
    s += box(215,154,200,40,['9th: makes a self-made,','hard-living mind'],'n')
    return fig(204,s,'A rough map of where Mercury sits in the chart and the kind of result the speaker attaches to it.','Map of good and bad house placements for Mercury')

D = dict(pipe=d_pipe(), birth=d_birth(), scale=d_scale(), atomic=d_atomic(), houses=d_houses())
