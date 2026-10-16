from diagrams import box, arr, lab, fig

def d_navel():
    s=box(110,8,200,36,['Venus: the heart'],'n')+arr(210,44,210,66)
    s+=box(90,66,240,40,['The diaphragm:','Earth, the dividing line'],'b')+arr(210,106,210,128)
    s+=box(110,128,200,36,['Mars: the navel'],'n')+arr(210,164,210,186)
    s+=box(60,186,300,44,['Digestive fire (jathragni):','processes whatever arrives'],'g')+arr(210,230,210,252)
    s+=box(40,252,340,48,['A sound navel: clear mind,','strong heart rhythm, real resolve'],'g')
    return fig(312,s,'His body map: Venus above the diaphragm, Mars below it, each governing its own zone.','Vertical diagram placing Venus above the diaphragm and Mars below it as the navel')

def d_shield():
    s=box(90,6,240,40,['Cosmic debris drifts','toward Earth'],'n')+arr(210,46,210,64)
    s+=box(60,64,300,40,["Jupiter's gravity catches","most of it"],'b')+arr(210,104,210,126)
    s+=box(90,126,240,36,['What still gets through'],'n')+arr(210,162,210,184)
    s+=box(40,184,340,44,['Mars absorbs the impact,','sits just ahead of Earth'],'g')+arr(210,228,210,250)
    s+=box(90,250,240,36,['Earth, and the body,','stay protected'],'g')
    return fig(310,s,'The asteroid-belt story: Mars as the last line of defence after Jupiter.','Flowchart of Jupiter and Mars shielding Earth from debris, paralleling the body')

def d_pipe():
    s=box(120,8,180,40,['A fixed intention','forms (Mars)'],'n')+arr(210,48,210,70)
    s+=box(70,70,280,40,['A steady channel opens','to the cosmos'],'b')+arr(210,110,210,132)
    s+=box(90,132,240,44,['Cosmos amplifies','whatever is sent'],'b')
    s+=arr(140,176,100,208)+arr(280,176,320,208)
    s+=box(10,208,190,52,['New, unrelated wish:','the channel collapses'],'r')
    s+=box(220,208,190,52,['Held steady:','it keeps building'],'g')
    s+=arr(315,260,315,282)
    s+=box(120,282,190,36,['Outcome returns'],'g')
    return fig(342,s,'His account of why a fixed intention, held by Mars, reaches the cosmos; a changed wish breaks the channel.','Flowchart of a fixed intention building a channel to the cosmos versus a changed wish breaking it')

def d_switch():
    s=box(130,8,160,36,['One switch'],'b')
    s+=arr(170,44,100,76)+arr(250,44,320,76)
    s+=box(10,76,190,48,['Ease (sahajta):','let it happen'],'g')
    s+=box(220,76,190,48,['Force (zid):','push it through'],'r')
    s+=arr(105,124,105,146)+arr(315,124,315,146)
    s+=box(10,146,190,56,['Mars stays positive:','friendship, bhog,','real enjoyment'],'g')
    s+=box(220,146,190,56,['Mars turns negative:','strained ties,','lost enjoyment'],'r')
    s+=arr(105,202,105,224)+arr(315,202,315,224)
    s+=box(10,224,190,40,['Same chart, better','outcome either way'],'n')
    s+=box(220,224,190,40,['Same chart, worse','outcome either way'],'n')
    return fig(284,s,'His central claim: ease versus force decides Mars for you, whatever the chart underneath.','Diagram contrasting ease and force as the switch that decides a Mars placement\'s outcome')

def d_manglik():
    s=box(90,8,240,40,['Mars in 1st, 4th, 7th,','8th or 12th house'],'r')+arr(210,48,210,70)
    s+=box(60,70,300,36,['Is Saturn also in one','of these five houses?'],'b')
    s+=arr(130,106,90,134)+arr(290,106,330,134)+lab(100,126,'yes','end')+lab(320,126,'no','start')
    s+=box(10,134,190,56,['Dosha cancelled:','marry either partner'],'g')
    s+=box(220,134,190,56,['Dosha stands:','match manglik pairs'],'n')
    s+=arr(315,190,315,212)
    s+=box(110,212,260,64,['Marriage comes later:','low 20s for her,','late 20s for him'],'n')
    return fig(288,s,'His method for checking manglik dosha, and whether Saturn\'s aspect cancels it.','Flowchart for checking whether Saturn cancels a manglik Mars placement')

D=dict(navel=d_navel(),shield=d_shield(),pipe=d_pipe(),switch=d_switch(),manglik=d_manglik())
