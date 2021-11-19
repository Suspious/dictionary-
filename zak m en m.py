import random
blauw = 0 
geel = 0 
groen = 0 
rood = 0 

Kleur = int(input('Hoeveel m en m wil je? '))
for j in range(Kleur):
    x =  random.randint(1,4)
    if x in [1]:
        blauw = blauw + 1
    if x in [2]:
        geel = geel + 1
    if x in [3]:
        rood = rood + 1
    if x in [4]:
        groen = groen + 1

    
Soortenmm = [{"kleur":"blauw","aantal":blauw},{"kleur":"geel","aantal":geel},{"kleur":"groen","aantal":groen},{"kleur":"rood","aantal":rood}]
print('je hebt een zak met')
for x in range(4):
    j = Soortenmm[x]["aantal"]
    m = Soortenmm[x]["kleur"]
    print('de kleur',m,"heeft ",j,'  m en m')
