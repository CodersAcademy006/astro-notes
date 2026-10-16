from diagrams import box,arr,lab,fig

def d_neechbhang():
    s=box(110,8,200,40,['A planet is debilitated'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,44,['Which house is it sitting in?'],'b')
    s+=arr(130,110,90,140)+arr(290,110,320,140)
    s+=lab(100,132,'6, 8 or 12','end')+lab(320,132,'other','start')
    s+=box(5,140,180,66,['Can flip: neech bhang','raj yog, often a strong','or protective result'],'g')
    s+=box(230,140,180,66,['Stays weak:','damages that house','as expected'],'r')
    return fig(218,s,"The speaker's neech bhang raj yog rule: a weak planet can flip to a strong result in a naturally difficult house.",'Flowchart: a debilitated planet in houses 6, 8 or 12 can flip to a strong result, elsewhere it stays weak')

def d_ketu():
    s=box(90,8,240,40,['You expect 100% completion'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,44,['Ketu has no head: nothing','is ever fully finished'],'b')+arr(210,110,210,128)
    s+=box(60,128,300,56,['Plan for 60-75% effort','yourself, delegate or','partner out the rest'],'g')+arr(210,184,210,202)
    s+=box(60,202,300,44,['More income,','more free time'],'g')
    return fig(254,s,"The speaker's productivity rule built from Ketu's nature.",'Flowchart: expecting full completion causes frustration, planning partial effort and delegating the rest works better')

D=dict(neechbhang=d_neechbhang(),ketu=d_ketu())
