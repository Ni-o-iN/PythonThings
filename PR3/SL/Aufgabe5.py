"""
#1)
import numpy
#a)
print("Aufgabe 1a):")
m = [[3,0,-2,11],[0,0,9,0],[0,7,0,0],[0,0,0,-3]]
print(m)

#b & c)
print("Aufgabe 1b&c):")
länge = 4
m = numpy.zeros((länge, länge))

for i in range(länge):
    for j in range(länge):
        n = int(input("Welche Zahl soll in die Matrix?"))
        m[j][i] = n
print(m)

#d)
print("Aufgabe 1d):")
print(m[1][1])

#2)
1 ist ein ungültiger dictonary key
'bob' ist ein gültiger dictonary key
('tom',[1,2,3]) ist ein ungültiger dictonary key
["filename"] ist ein ungültiger dictonary key
"filename" ist ein gültiger dictonary key
("filename","extension") ist ein ungültiger dictonary key


#3)
print("Aufgabe 3:")
list = [1,2,3,4,5,6,7,8,9,10]
letzten = list[-3:]
del list[-3:]
list[0:0] = letzten
print(list)


#4)
print("Aufgabe 4:")
wort = "Donaudampfschiffahrtsgesellschaftsstewardess"
liste = list(wort)
print(liste)
print(len(liste))
klein = wort.lower()

vorhaden = ""
for i in range(len(klein)):
    if klein[i] not in vorhaden:
        vorhaden += klein[i]

print(vorhaden)
print(len(vorhaden))


#5)
print("Aufgabe 5):")
def sort(neue_liste):
    neue_liste.sort(key=lambda x: x[1])
    return neue_liste
liste = [[1, 2, 3],[2, 1, 3],[4, 0, 1]]
print(sort(liste))


#6)
print("Aufgabe 6):")
dictonary = {"Hund": "Wau", "Katze": "Miau", "Kuh": "Muh"}
tier = input("Welchen Laut von welchem Tier wollen Sie? [Hund,Katze,Kuh]")
print(dictonary.get(tier, "Kein gültiges Tier"))
"""
