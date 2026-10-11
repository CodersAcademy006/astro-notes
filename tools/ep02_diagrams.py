from diagrams import box,arr,lab,fig
def d_sync():
    s=box(10,8,190,50,['Birth chart','about 12 percent fixed'],'r')+box(220,8,190,50,['Your belief and body','the 72 percent'],'b')
    s+=arr(105,58,170,90)+arr(315,58,250,90)
    s+=box(110,90,200,44,['Body and mind in sync?'],'n')
    s+=arr(160,134,105,164)+arr(260,134,315,164)
    s+=box(10,164,190,70,['In sync','work as the chart says,','rise like a rocket'],'g')+box(220,164,190,70,['Fighting the chart','more effort,','less success'],'r')
    s+=box(30,250,360,40,['No number is lucky or unlucky'],'b')
    return fig(300,s,'The speaker\'s model: the chart is fixed, the response is yours.','Flowchart of chart, belief and body-mind sync')
def d_stones():
    items=[('Sun',['Ruby']),('Moon',['Pearl']),('Mars',['Coral']),('Mercury',['Emerald']),('Jupiter',['Yellow sapphire']),('Venus',['Diamond or','white pukhraj']),('Saturn',['Blue sapphire']),('Rahu',['Hessonite']),('Ketu',["Cat's eye"])]
    s=''
    for i,(p,l) in enumerate(items):
        x=5+(i%3)*138; y=8+(i//3)*74
        c='r' if p in('Rahu','Ketu') else 'n'
        s+=box(x,y,134,66,[p]+l,c)
    s+=box(30,236,360,40,['Only if the chart agrees, via a trained reader'],'b')
    return fig(286,s,'The stone the speaker names for each planet. Not a recommendation.','Grid of planets and their stones')
def d_degrees():
    s=box(60,8,300,40,['Chart shows a planet in a house'],'n')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Compare its degree with the lagna degree'],'b')
    s+=arr(160,106,105,134)+arr(260,106,315,134)
    s+=box(10,134,190,70,['Degree lower than lagna','the planet works in','the house behind'],'g')+box(220,134,190,70,['Near a sign edge','2 or 3 signs act','on one house'],'g')
    s+=arr(105,204,160,230)+arr(315,204,260,230)
    s+=box(60,230,300,50,['Working (chalit, KP) chart','settles where it really sits'],'n')
    return fig(290,s,'A planet shown in a house may not be working there, per the speaker.','Flowchart for checking a planet by degree')
def d_food():
    rows=[(['Mars weak, sign 4'],['Red meat, red wine']),(['Moon on sign 1 or 8'],['White meat, white','wine, vodka']),(['Ketu from sign 3'],['Seafood, smoking']),(['Rahu on sign 9'],['Beer, alcohol']),(['Venus weak, sign 6'],['Beef']),(['Sun fault'],['Spinach, gluten','allergy'])]
    s=''
    for i,(a,b) in enumerate(rows):
        y=8+i*58
        s+=box(10,y,190,48,a,'n')+box(220,y,190,48,b,'r')+arr(200,y+24,220,y+24)
    s+=box(30,362,360,40,['The speaker\'s claims. Not medical advice.'],'b')
    return fig(412,s,'Chart condition on the left, what he says to watch on the right.','Table of chart conditions and foods to watch')
def d_ishta():
    s=box(110,8,200,40,['Ninth house shows ishta'],'b')+arr(210,48,210,66)
    s+=box(60,66,300,40,['Does the navamsa agree?'],'n')
    s+=arr(160,106,105,134)+arr(260,106,315,134)+lab(120,124,'yes','end')+lab(300,124,'no','start')
    s+=box(10,134,190,70,['Place the idol in the','west of the home','no ritual needed'],'g')+box(220,134,190,70,['Pick a common deity','(he names Bhairav','or Shiva)'],'n')
    s+=arr(105,204,160,232)+arr(315,204,260,232)
    s+=box(30,232,360,66,['Family: one ishta per person.','Avoid opposing pairs,','such as Ganesh with Durga.'],'r')
    return fig(308,s,'How the speaker places an ishta deity at home.','Flowchart for placing an ishta deity')
D=dict(sync=d_sync(),stones=d_stones(),degrees=d_degrees(),food=d_food(),ishta=d_ishta())
