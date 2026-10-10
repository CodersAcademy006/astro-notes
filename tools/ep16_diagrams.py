from diagrams import box,arr,lab,fig
def d_ask():
    s=box(110,8,200,40,['SUN = self-respect'],'r')+arr(150,48,95,76)+arr(270,48,325,76)
    s+=box(5,76,200,64,['Ask big, as an equal','"I need this"'],'g')
    s+=box(215,76,200,64,['Beg small','"please, a little"'],'r')
    s+=arr(105,140,105,160)+arr(315,140,315,160)
    s+=box(5,160,200,52,['Venus stays alive','home is calm'],'g')+box(215,160,200,52,['Sun breaks first','Venus burns next'],'r')
    return fig(222,s,'Self-respect and the Sun, per the speaker.','Ask big versus beg')
def d_year():
    s=box(5,10,200,52,['SUN','one month per sign'],'r')+box(215,10,200,52,['NEPTUNE / PLUTO','years in one sign'],'b')
    s+=arr(105,62,105,84)+arr(315,62,315,84)
    s+=box(60,84,300,40,['Once a year the Sun meets it'],'n')+arr(210,124,210,142)
    s+=box(5,142,200,64,['Bad place','that month hurts:','accident, tears'],'r')+box(215,142,200,64,['Good place','that month helps:','party, success'],'g')
    return fig(216,s,'His yearly month idea. A reading, not a forecast.','Sun yearly transit loop')
def d_merc():
    s=box(5,10,130,52,['SUN','father'],'r')+box(285,10,130,52,['SATURN','son'],'r')
    s+=box(140,10,140,52,['MERCURY','friend of both'],'g')
    s+=arr(210,62,210,84)
    s+=box(30,84,170,52,['Mercury between','no fight'],'g')+box(220,84,170,52,['Not between','Rahu angry, fights'],'r')
    s+=arr(125,136,125,156)+box(30,156,170,50,['Green moong dal','to birds (his remedy)'],'n')
    return fig(216,s,'Father and son planets with Mercury between.','Sun Saturn Mercury diagram')
def d_dog():
    s=box(110,8,200,40,['SUN + PLUTO (Yama)'],'r')+arr(210,48,210,66)
    s+=box(30,66,360,40,['Yama cannot take life while the Sun is near'],'b')+arr(210,106,210,124)
    s+=box(5,124,200,64,['Curse yourself','slow rot, tears'],'r')+box(215,124,200,64,['Do not curse','Pluto a Dharmaraj'],'g')
    return fig(198,s,'The Sun and Yama, as he teaches it.','Sun Pluto flow')
def d_prav():
    s=box(110,8,200,40,['Sun + 3 more planets'],'b')+arr(210,48,210,66)
    s+=box(30,66,360,40,['Same house, four in all, no Rahu or Ketu'],'n')+arr(210,106,210,124)
    s+=box(30,124,360,52,['Pravrajya yoga','household spark fades'],'r')
    return fig(186,s,'The four-planet rule as he states it.','Pravrajya yoga')
D=dict(ask=d_ask(),year=d_year(),merc=d_merc(),dog=d_dog(),prav=d_prav())
