from diagrams import box,arr,lab,fig
def d_chakras():
    labels=['Saturn','Jupiter','Mars','Venus','Mercury','Sun / Moon']
    s=''
    for i,l in enumerate(labels):
        s+=box(60,8+i*42,300,34,[l],'n' if i else 'b')
        if i<len(labels)-1: s+=arr(210,42+i*42,210,50+i*42)
    s+=lab(210,8+len(labels)*42+14,'Lower body to upper torso, in his scheme')
    return fig(8+len(labels)*42+26,s,'The speaker\'s mapping of the body onto the solar system, Saturn lowest and the Sun and Moon highest.','Stacked diagram of six planets mapped onto the body from Saturn up to Sun and Moon')
def d_ganeshbirth():
    s=box(90,8,240,40,['Parvati shapes a child','to guard the door'],'n')+arr(210,48,210,66)
    s+=box(60,66,300,40,['The child doubts Shiva,','will not let him in'],'b')+arr(210,106,210,124)
    s+=box(60,124,300,40,['Shiva beheads the child','out of that same doubt'],'r')+arr(210,164,210,182)
    s+=box(30,182,360,46,['A new head is chosen:','an elephant\'s, strongest memory,','least prone to suspicion'],'g')+arr(210,228,210,246)
    s+=box(60,246,300,40,['Ganesh: worshipped first,','to remove doubt itself'],'g')
    return fig(306,s,'The speaker\'s reading of the Ganesh birth story: doubt is what gets punished, and an elephant\'s mind is his fix for it.','Flowchart of the Ganesh birth story read as a lesson about doubt')
def d_chaturthi():
    s=box(20,8,180,54,['SUN','in Leo (its own sign)','a mouse-shaped pattern'],'b')
    s+=box(220,8,180,54,['MOON','in Pisces','an elephant-shaped pattern'],'n')
    s+=arr(110,62,210,110)+arr(310,62,210,110)
    s+=box(60,110,300,50,['Same day, every year:','an elephant riding a mouse'],'g')+arr(210,160,210,178)
    s+=box(30,178,360,40,['The festival\'s image, read','as this sky event'],'g')
    return fig(238,s,'The speaker\'s astronomy for Ganesh Chaturthi: the Sun and Moon\'s positions on that day, read as the mouse-and-elephant image.','Diagram of the Sun in Leo and Moon in Pisces combining into the Ganesh Chaturthi image')
def d_eclipse():
    s=box(130,8,160,40,['The Sun (clarity)'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,46,['The Moon (prarabdha, fate)','passes directly in front'],'n')+arr(210,112,210,130)
    s+=box(30,130,360,46,['Sun\'s light is blocked:','a solar eclipse, Rahu/Ketu "eat" it'],'r')+arr(210,176,210,194)
    s+=box(30,194,360,54,['In a life: your own clarity is blocked','by a fixed stretch of fate, not gone,','just temporarily hidden'],'n')
    return fig(248,s,'The speaker\'s eclipse mechanics, read onto personal destiny: fate blocks clarity the way the moon blocks the sun, temporarily.','Flowchart reading a solar eclipse as a metaphor for destiny blocking clarity')
def d_fakir():
    s=box(90,8,240,40,['Rahu and Ketu unsettled'],'r')+arr(210,48,210,66)
    s+=box(40,66,340,40,['Find someone who asks for nothing'],'b')+arr(210,106,210,124)
    s+=box(40,124,340,46,['A stray dog, a cow, a quiet fakir,','not someone actively begging'],'n')+arr(210,170,210,188)
    s+=box(40,188,340,40,['Serve them without announcing it'],'g')+arr(210,228,210,246)
    s+=box(70,246,280,40,['Rahu and Ketu settle'],'g')
    return fig(306,s,'The speaker\'s one remedy for Rahu and Ketu: serve whoever asks for nothing, quietly.','Flowchart of the fakir remedy for settling Rahu and Ketu')
D=dict(chakras=d_chakras(),ganeshbirth=d_ganeshbirth(),chaturthi=d_chaturthi(),eclipse=d_eclipse(),fakir=d_fakir())
