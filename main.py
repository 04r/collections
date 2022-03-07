import random
from re import L

dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

# Alle dagen van de week zijn: maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag.
# De werkdagen zijn: maandag, dinsdag, woensdag, donderdag, vrijdag.
# De weekenddagen zijn: zaterdag, zondag.
# Alle dagen van de week in omgekeerde volgorde zijn: zondag, zaterdag, vrijdag, donderdag, woensdag, dinsdag, maandag.
# De werkdagen in omgekeerde volgorde zijn: vrijdag, donderdag, woensdag, dinsdag, maandag.
# De weekenddagen in omgekeerde volgorde zijn: zondag, zaterdag

werkdagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']
weekenddagen = ['zaterdag', 'zondag']
omgekeerd = ['zondag', 'zaterdag', 'vrijdag', 'donderdag', 'woensdag', 'dinsdag', 'maandag']
omgekeerdewerkdagen = ['vrijdag', 'donderdag', 'woensdag', 'dinsdag', 'maandag']
omgekeerdeweekend = ['zondag', 'zaterdag']

    


listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20] 

def addAndDisplayLists(list1, list2):
    for x in range(len(listOne)):
        print(f"{listOne[x]} + {listTwo[x]} = {listOne[x] + listTwo[x]}")
        
addAndDisplayLists(listOne, listTwo)

def substractAndDisplayLists(list1, list2):
    for x in range(len(listOne)):
        print(f"{listOne[x]} - {listTwo[x]} = {listOne[x] - listTwo[x]}")
        
substractAndDisplayLists(listOne, listTwo)

def multiplyAndDisplayLists(list1, list2):
    for x in range(len(listOne)):
        print(f"{listOne[x]} * {listTwo[x]} = {listOne[x] * listTwo[x]}")
        
multiplyAndDisplayLists(listOne, listTwo)

def divideAndDisplayLists(list1, list2):
    for x in range(len(listOne)):
        print(f"{listOne[x]} / {listTwo[x]} = {listOne[x] / listTwo[x]}")
        
divideAndDisplayLists(listOne, listTwo)

spelLijst = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimum, maximum):
    for i in range(random.randint(minimum,maximum)):
        print(random.choice(spelLijst))

spelProgramma(spelList = spelLijst, minimum=13 , maximum=10)