from diagrams import box,arr,lab,fig

def d_speed():
    rows=[('Moon','about 2.5 days','g'),('Sun','about 1 month','n'),
          ('Mars','about 1.5 months','n'),('Jupiter','about 11-13 months','n'),
          ('Saturn','about 2.5 years','b'),('Indra, Varuna, Yama','decades per sign','r')]
    s=''
    y=6
    for i,(name,dur,c) in enumerate(rows):
        s+=box(10,y,400,46,[name,dur],c)
        if i<len(rows)-1: s+=arr(210,y+46,210,y+62)
        y+=62
    return fig(y-10,s,'How long each planet stays in one sign, fastest to slowest, as the speaker gives it.','List of planets ordered from fastest-moving (Moon) to slowest-moving (Indra, Varuna, Yama)')

def d_zodiac():
    cells=[('Aries','Mars'),('Taurus','Venus'),('Gemini','Mercury'),('Cancer','Moon'),
           ('Leo','Sun'),('Virgo','Rahu'),('Libra','Varuna'),('Scorpio','Indra'),
           ('Sagittarius','Jupiter'),('Capricorn','Saturn'),('Aquarius','Yama'),('Pisces','Ketu')]
    s=''
    for i,(sign,owner) in enumerate(cells):
        cx=(i%3)*138+6; cy=(i//3)*78+6
        s+=box(cx,cy,132,70,[str(i+1),sign,owner],'n')
    return fig(cy+78,s,"The speaker's natural zodiac: each sign in order with the planet he gives as its ruler.",'Grid of the 12 zodiac signs numbered 1 to 12 with their ruling planet')

def d_ownhouse():
    s=box(110,8,200,44,['A planet sits','in a sign'],'b')
    s+=arr(140,52,70,90)+arr(210,52,210,90)+arr(280,52,350,90)
    s+=lab(80,80,'own sign','end')+lab(210,80,'friend\'s sign','middle')+lab(330,80,'opposite sign','start')
    s+=box(5,90,130,60,['Comfortable,','strong result'],'n')
    s+=box(145,90,130,60,['Can beat the','own-sign result'],'g')
    s+=box(285,90,130,60,['Weakest or most','damaging result'],'r')
    return fig(158,s,"The speaker's rule of thumb for reading any planet in any sign.",'Flowchart: own sign is strong, a friendly sign can be even better, the opposite sign is the weakest')

def d_donation():
    s=box(90,8,240,40,['Which planet rules this','house in your chart?'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,44,['Is it well placed there','(own, friendly, exalted)?'],'b')
    s+=arr(130,110,90,140)+arr(290,110,320,140)+lab(100,132,'yes','end')+lab(310,132,'no','start')
    s+=box(10,140,180,70,['Give that planet\'s item','at a sacred place','(temple, gurudwara)','Fortune multiplies'],'g')
    s+=box(230,140,180,70,['Do not improvise.','The same item given','the wrong way can','make things worse'],'r')
    return fig(222,s,"The speaker's donation rule: a good placement is strengthened by giving at a sacred place, a bad placement needs a proper reading first, not a guess.",'Decision tree for matching a donation to a house and its planet')

D=dict(speed=d_speed(),zodiac=d_zodiac(),ownhouse=d_ownhouse(),donation=d_donation())
