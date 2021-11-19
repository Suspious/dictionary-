List1 = 1,2,3,4,5,6,7,8,9,10
list2 = 1,2,3,4,5,6,7,8,9,10
def addAndDisplayLists(list1, list2):
    for x in range(10):
        total = List1[x] + (list2[x] * 2)
        print(List1[x],'  +  ', (list2[x]* 2),'  =   ',total )

def substractAndDisplayLists (List1, list2):
    for x in range(10):
        total = List1[x] - (list2[x] * 2)
        print(List1[x],'  -  ', (list2[x]* 2),'  =   ',total )

def multiplyAndDisplayLists (List1, list2):
    for x in range(10):
        total = List1[x] * (list2[x] * 2)
        print(List1[x],'  *  ', (list2[x]* 2),'  =   ',total )
def divideAndDisplayLists (List1, list2):
    for x in range(10):
        total = List1[x] / (list2[x] * 2)
        print(List1[x],'  / ', (list2[x]* 2),'  =   ',total )
addAndDisplayLists(List1, list2)
print('--------------------------------------------------')
substractAndDisplayLists(List1, list2)
print('--------------------------------------------------')
multiplyAndDisplayLists(List1, list2)
print('--------------------------------------------------')  
divideAndDisplayLists (List1, list2)
