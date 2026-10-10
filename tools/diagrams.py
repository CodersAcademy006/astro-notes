from html import escape
LH=17
def box(x,y,w,h,lines,c='n'):
    t=''.join(f'<tspan x="{x+w/2}" dy="{LH if i else 0}">{escape(l) or chr(160)}</tspan>' for i,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*LH/2+5
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="{c}"/><text x="{x+w/2}" y="{ty}" text-anchor="middle">{t}</text>'
def arr(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="ln" marker-end="url(#ah)"/>'
def lab(x,y,s,a='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{a}" class="lb">{escape(s)}</text>'
def fig(h,inner,cap,alt):
    return (f'<figure class="dg"><svg viewBox="0 0 420 {h}" role="img" aria-label="{escape(alt)}">'
      '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="ahp"/></marker></defs>'
      f'{inner}</svg><figcaption>{escape(cap)}</figcaption></figure>')

def d_window():
    s=box(110,8,200,40,['Someone says something'],'n')+arr(210,48,210,66)
    s+=box(90,66,240,40,['Mind goes blank: your own eclipse','(Rahu)'],'r')+arr(210,106,210,124)
    s+=box(90,124,240,40,['The next few minutes','What do you do?'],'b')
    s+=arr(160,164,105,200)+arr(260,164,315,200)
    s+=box(10,200,190,40,['Hold yourself','do not react'],'g')+box(220,200,190,40,['Fight or react','in the heat'],'r')
    s+=arr(105,240,105,262)+arr(315,240,315,262)
    s+=box(10,262,190,52,['Rahu is set','mind clears, wisdom'],'g')+box(220,262,190,52,['Ketu (the body) acts','on the corrupted decision'],'r')
    s+=arr(105,314,105,336)+arr(315,314,315,336)
    s+=box(10,336,190,52,['Witness mind','grows over time'],'g')+box(220,336,190,52,['Grudge loop, then','years of Rahu dasha'],'r')
    return fig(398,s,'The speaker\'s rule for anger: the eclipse window is short, and what you do inside it decides the result.','Flowchart of the anger window: hold yourself leads to wisdom, reacting leads to a grudge loop')
def d_seesaw():
    s='<line x1="40" y1="110" x2="380" y2="110" class="ln" stroke-width="3"/><path d="M210,112 L190,150 L230,150 Z" class="n"/>'
    s+=box(10,22,180,70,['RAHU: the head','sees, thinks, speaks','cannot act'],'r')+box(230,22,180,70,['KETU: the body','acts, feels, intuits','no judgement'],'g')
    s+=arr(100,92,100,106)+arr(320,92,320,106)
    s+=box(60,162,300,52,['Raise one and the other goes down','Level together: both are set (siddha)'],'b')
    s+=box(60,228,300,40,['Fix Rahu using Ketu, fix Ketu using Rahu'],'n')
    return fig(278,s,'Rahu and Ketu sit opposite each other like a seesaw. The balance is the remedy.','Seesaw diagram of Rahu and Ketu')
def d_daan():
    s=box(110,8,200,40,['A planet is troubling you'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Give that planet\'s own item','never the item of a good planet'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['With your own hand','anonymously, no receipt'],'b')
    for x in (70,210,350): s+=arr(210,164,x,196)
    s+=box(5,196,130,100,['Illness, mind','distress','','Barley, body weight,','into flowing water'],'g')
    s+=box(145,196,130,100,['Cannot do that?','','Feed soaked barley','to birds, animals,','strangers'],'g')
    s+=box(285,196,130,100,['Rahu tormenting','','Beer to strangers','or into a river','never in a temple'],'g')
    return fig(306,s,'Daan, the speaker\'s main Rahu remedy. The item matches the planet, and the giving is anonymous.','Flowchart of the daan method')
def d_thread():
    s=box(120,8,180,36,['Which problem?'],'b')
    for x in (70,210,350): s+=arr(210,44,x,66)
    s+=box(5,66,130,76,['Enemies, court,','debt, spine or','leg nerve pain'],'n')+box(145,66,130,76,['Leg trouble','sleeplessness','in-law conflict'],'n')+box(285,66,130,76,['Debilitated planet','in the 10th','job problems'],'n')
    s+=arr(70,142,70,164)+arr(210,142,210,164)+arr(350,142,350,164)
    s+=box(5,164,130,64,['Cancer lagna or','Cancer navamsa','lagna?'],'b')
    s+=box(145,164,130,64,['LEFT foot','blue thread'],'g')+box(285,164,130,64,['LEFT wrist','blue thread'],'g')
    s+=arr(40,228,40,252)+arr(100,228,100,252)+lab(30,246,'yes','end')+lab(110,246,'no','start')
    s+=box(5,252,62,48,['Skip it'],'r')+box(73,252,62,48,['RIGHT','foot'],'g')
    s+=box(5,316,410,70,['Check the navamsa is not hostile.','Tie with a knot. Never cut it with scissors','or burn it. Foot threads go on the foot.'],'n')
    return fig(396,s,'Blue thread placement as the speaker describes it. A trained astrologer should confirm the chart conditions.','Decision tree for blue thread placement')
def d_compass():
    s=''
    cells={(0,0):(['NW'],'e'),(1,0):(['NORTH','Failed ancestor:','never here'],'r'),(2,0):(['NE'],'e'),
           (0,1):(['WEST','Very wise ancestor:','gains come easy'],'g'),(1,1):(['HOUSE'],'e'),(2,1):(['EAST'],'e'),
           (0,2):(['SOUTH-WEST','Ancestors live here','keep it clean'],'b'),(1,2):(['SOUTH'],'e'),(2,2):(['SOUTH-EAST','Clever, happy','woman relative:','helps in-law','trouble'],'g')}
    for (cx,cy),(l,c) in cells.items():
        s+=box(5+cx*138,6+cy*98,134,90,l,c)
    return fig(306,s,'Where to hang ancestor photos, from the speaker\'s vastu advice. Empty cells were not discussed.','Compass grid of ancestor photo placement')
def d_start():
    s=box(110,8,200,40,['Rahu is troubling you'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Is Saturn badly placed in your chart?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,320,134)+lab(100,126,'yes','end')+lab(310,126,'no','start')
    s+=box(10,134,180,64,['Fix Saturn first','blue sapphire instead','of gomed, if allowed'],'g')
    s+=box(230,134,180,64,['Which planet is','Rahu with, or what','is the symptom?'],'b')
    s+=arr(320,198,366,216)
    for i,(t,x) in enumerate([(['Moon','mother, milk,','silver'],5),(['Sun','moist eyes,','water at night'],109),(['Mars','act without','attachment'],213),(['Mercury,','Jupiter','guru, calm','speech'],317)]):
        s+=box(x,216,98,76,t,'g')
    s+=''.join(arr(320,198,x,216) for x in (54,158,262))
    s+=box(5,308,205,52,['Illness, helplessness','barley in flowing water'],'g')+box(215,308,200,52,['Enemies, court, debt','blue thread, right foot'],'g')
    return fig(370,s,'A starting path through the remedies. Section 24 has the full list with timestamps.','Flowchart for choosing a Rahu remedy')
D=dict(window=d_window(),seesaw=d_seesaw(),daan=d_daan(),thread=d_thread(),compass=d_compass(),start=d_start())
