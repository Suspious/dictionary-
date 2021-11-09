#hier beschrijf ik de dagen van de week
dagen_van_de_week = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
#nu ga ik een vraag maken om te kunnen bepalen wat voor for loop ik moet bepalen
Vraag = input('''
_________________________________________________________
Welke dagen wil je weten 

A werk dagen 
b alle dagen van de week 
c weekendagen 
d werkdagen omgekeerd 
e alle dagen omgekeerd
f alle weekend dagen omgekeerd

''').lower()
X = 0 
J = 0
B = 0 
# nu ga ik twee defs maken 1 voor normaal en 1 voor omgekeerd
def normaal():
    global dagen_van_de_week
    global X
    global J
    for x in range(X,J):
        print(dagen_van_de_week[x])
def omgekeerd():
    global dagen_van_de_week
    global X
    global J
    global B 
    for x in range(J,X,B):
        print(dagen_van_de_week[x])

#x is mijn begin en j is mijn eindpunt voor de while loop Plus b is voor hoeveel eraf moet
if Vraag == 'a':
    X += 0
    J += 5
    normaal()
if Vraag == 'b':
    X += 0
    J += 7
    normaal()
if Vraag == 'c':
    X += 5
    J += 7
    normaal()
if Vraag == 'd':
    J += 4
    X += -1
    B = -1
    omgekeerd()
if Vraag == 'e':
    J += 6
    X += -1
    B = -1
    omgekeerd()
if Vraag == 'f':
    J += 6
    X += 4
    B =  -1
    omgekeerd()

