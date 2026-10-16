from diagrams import box,arr,lab,fig
def d_fixed():
    s=box(110,8,200,40,['Every planet fixed','on its own axis'],'n')+arr(210,48,210,66)
    s+=box(90,66,240,40,['...yet every planet','keeps moving its path'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,50,['The Sun loops the galaxy','once every 25,920 years'],'n')+arr(210,174,210,192)
    s+=box(60,192,300,46,['It never returns to the','exact same point twice'],'r')+arr(210,238,210,256)
    s+=box(40,256,340,50,['Fixed, but never repeating:','that is destiny, today'],'g')
    return fig(316,s,'The paradox the speaker calls fixed but unfixed: every orbit is locked, but the combination never repeats.','Flowchart of the fixed but never repeating paradox')
def d_thirdeye():
    s=box(90,8,240,40,['Ego, greed, attachment,','jealousy, scorekeeping'],'r')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Third eye: on or off?'],'b')
    s+=arr(160,106,105,142)+arr(260,106,315,142)
    s+=box(10,142,190,40,['Keep grabbing,','keep score'],'r')+box(220,142,190,40,['Let go of the','scorekeeping'],'g')
    s+=arr(105,182,105,204)+arr(315,182,315,204)
    s+=box(10,204,190,52,['Third eye stays shut,','confusion repeats'],'r')+box(220,204,190,52,['Third eye opens,','gradually, on its own'],'g')
    s+=arr(105,256,105,278)+arr(315,256,315,278)
    s+=box(10,278,190,52,['Right guide feels','out of reach'],'r')+box(220,278,190,52,['Right guide, respect','and knowledge, free'],'g')
    return fig(338,s,'What the speaker says blocks or opens the third eye.','Flowchart of what blocks or opens the third eye')
def d_effect():
    cols=[('SCIENCE',['Asks why first','(the cause)'],['Produces discovery','and invention'],'n'),
          ('JYOTISH',['Reads the effect,','what comes next'],['A forecast built on','exact planet maths'],'b')]
    s=''
    for i,(name,q,a,c) in enumerate(cols):
        x=10+i*205
        s+=box(x,8,190,46,[name],c)+arr(x+95,54,x+95,70)+box(x,70,190,70,q,'n')+arr(x+95,140,x+95,156)+box(x,156,190,70,a,'n')
    return fig(244,s,'The speaker splits how science and Jyotish each work: cause first, or effect first.','Two columns comparing science and Jyotish')
def d_remedy():
    items=[('DAAN',['its own item,','given by','your own hand']),('DUA',['blessings from','anyone, given','with respect']),('DAVA',['care for','the body','itself'])]
    xs=[5,145,285]
    s=''
    for (name,l),x in zip(items,xs):
        s+=box(x,8,130,92,[name]+l,'b')
    for x in (70,210,350):
        s+=arr(x,100,210,140)
    s+=box(60,140,300,50,['All three work together,','none replaces the others'],'n')+arr(210,190,210,208)
    s+=box(30,208,360,54,['Peace returns to life,','the planet\'s grip eases'],'g')
    return fig(272,s,'The three remedies the speaker names: daan, dua and dava.','Flowchart of daan dua and dava converging')
D=dict(fixed=d_fixed(),thirdeye=d_thirdeye(),effect=d_effect(),remedy=d_remedy())
