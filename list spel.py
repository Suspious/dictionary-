import random
minimum = int(input('Minumum? '))
spellenlijst = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','cluedo']
maximum = int(input('maximum? ' ))
def spel(spellenlijst,minimum,maximum):
    
    for j in range(minimum):
        x = random.randint(1,6)
        print(spellenlijst[x])
        if j == maximum:
            break
spel(spellenlijst,minimum,maximum)