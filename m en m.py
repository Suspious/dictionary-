import random
Lijstm = ['rood','groen','geel','blauw']
aantal = int(input('hoeveel m en m wil je hebben? '))
def zakmm(aantal,lijstm):
    kleuren = int((input('hoeveel kleuren wil je?  ')))
    if kleuren < 4:
        lijstm.pop((kleuren ))
    for x in range(aantal):
        random.shuffle(lijstm)
        for x in range(3):
            (lijstm[x])
            lijst2 = []
            lijst2.extend(lijstm)
        ja = str(aantal)
    print(''''
        --------------------------------
        in je m en m zitten 
        ------------------------------------
        ''',aantal,'m en m'
        )
    for x in range(aantal):
        print('      ',lijst2[(random.randint(1,2))])
        if  lijst2 == 'blauw':
            blauw = 0 
            blauw += 1
        if lijst2 =='rood':
            rood = 0 
            rood += 1 
        if lijst2 == 'groen':
            groen = 0
            groen += 1
        if lijst2 =='geel':
            geel = 0
            geel += 1
    lijstjekleur = [groen or blauw or rood or geel]
    for i in range(1,4):
        print(lijstjekleur[i], str(lijstjekleur[i]))
    
zakmm(aantal,Lijstm)

