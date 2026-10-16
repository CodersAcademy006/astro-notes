from diagrams import box, arr, lab, fig

def d_flex():
    s=box(90,8,240,44,['Pride: "nothing runs','without me"'],'r')+arr(210,52,210,74)
    s+=box(60,74,300,40,['Body is ~72% water,','naturally flexible'],'n')+arr(210,114,210,136)
    s+=box(40,136,340,44,['Pride stiffens the neck,','body turns rigid'],'r')
    s+=arr(140,180,100,212)+arr(280,180,320,212)
    s+=box(10,212,190,52,['Fast food, high heat:','water dries further'],'r')
    s+=box(220,212,190,52,['Life finally breaks','the pride'],'b')
    s+=arr(315,264,315,286)
    s+=box(220,286,190,44,['Trapped water','releases as tears'],'g')
    s+=box(10,286,190,44,['Brittle bones,','less flexible body'],'r')
    return fig(346,s,'His reading of pride: a rigid body traps water until life forces it out as tears.','Flowchart linking pride and rigid posture to the body\'s water content')

def d_loop():
    s=box(130,8,160,40,['A wish forms','in the mind'],'n')+arr(210,48,210,66)
    s+=box(100,66,220,40,['Electric signal,','then a wave'],'n')+arr(210,106,210,124)
    s+=box(70,124,280,40,['Moon captures it,','relays to the cosmos'],'b')+arr(210,164,210,182)
    s+=box(50,182,320,44,['Cosmos checks: does your','inner state match the wish?'],'b')
    s+=arr(140,226,100,254)+arr(280,226,320,254)
    s+=box(10,254,190,48,['"I am not that','person yet": blocked'],'r')
    s+=box(220,254,190,48,['Matches: the wish','can return'],'g')
    s+=arr(105,302,105,324)
    s+=box(10,324,390,44,['Observer effect: focused, one-pointed','attention is what tends to land'],'n')
    return fig(384,s,'His account of how a wish is said to "manifest," built on the observer effect.','Flowchart of a wish travelling from thought to the cosmos and back')

def d_ishta():
    s=box(110,8,200,40,['Your 9th house sign'],'b')
    s+=arr(160,48,110,80)+arr(260,48,310,80)
    s+=box(10,80,200,52,['Protective deity','(Ishta): automatic,','runs without effort'],'g')
    s+=box(220,80,190,52,['Opposing deity:','that domain weakens','this house'],'r')
    s+=arr(110,132,110,154)+arr(315,132,315,154)
    s+=box(10,154,200,56,['Worship or not,','this energy is','already active'],'n')
    s+=box(220,154,190,56,['Avoid that domain;','no remedy needed','beyond avoidance'],'b')
    s+=arr(160,210,160,232)
    s+=box(10,232,390,66,['His point: outward behaviour','tracks the chart, whatever','religion is practised'],'n')
    return fig(306,s,'His method for finding a protective and an opposing deity from the 9th house.','Flowchart of protective versus opposing deity determined by the ninth house')

def d_signs():
    s=box(130,8,160,36,['Disturbed Moon'],'r')
    for x in (10,150,290):
        s+=arr(210,44,x+70,66)
    s+=box(10,66,140,60,['At home:','leaks, damp,','standing water'],'n')
    s+=box(150,66,140,60,['In the body:','OCD, allergies,','low immunity'],'n')
    s+=box(290,66,130,60,['In the mind:','comparison,','hallucination'],'n')
    s+=arr(80,126,80,148)+arr(220,126,220,148)+arr(355,126,355,148)
    s+=box(10,148,400,44,['Fix the leak; after sunset, tint rice, milk','and water rather than taking them plain'],'g')
    s+=arr(210,192,210,214)
    s+=box(60,214,300,40,['Pearl (moti) is his general','gemstone for the Moon'],'b')
    return fig(254,s,'A quick map of the "disturbed Moon" signs he lists, grouped by where they show up.','Diagram grouping disturbed-Moon symptoms by home, body and mind, with the general fix')

def d_name():
    s=box(110,8,200,36,['Your birth chart'],'b')+arr(210,44,210,66)
    s+=box(60,66,300,40,['List which houses carry','Saturn, Rahu, Sun or Pluto'],'n')+arr(210,106,210,128)
    s+=box(90,128,240,40,['Those houses\' letters','are ruled out'],'r')+arr(210,168,210,190)
    s+=box(70,190,280,44,['Remaining houses:','the safe letters to name from'],'g')+arr(210,234,210,256)
    s+=box(90,256,240,44,['Use that letter as a','first name or pen name'],'b')
    return fig(316,s,'His elimination method for choosing a "safe" first letter from the chart\'s unafflicted houses.','Flowchart for eliminating afflicted houses to find a safe naming letter')

D=dict(flex=d_flex(),loop=d_loop(),ishta=d_ishta(),signs=d_signs(),name=d_name())
