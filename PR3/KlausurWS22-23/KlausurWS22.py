#Aufgabe 21
#Was ist die Ausgabe
d = [1,2,3,4,5,6]
print(d[1:3])

'''
Aufgabe 22
Zur Auflösung der Vererbungshierarchie wird in der Pythonversion 2.3 bzw. 3.x
der C3-Liniearisierungsalgorithmus verwendet
Wahr oder Falsch
Antwort: Wahr
'''

'''
Aufgabe 23
Python besitzt eine dynamische Typisierung
Wahr oder Falsch
Antowrt: Wahr
'''

'''
Aufgabe 24
Python ist keine multiparadigmatische Programmiersprache, denn man kann nur 
objektorientiert programmieren
Wahr oder Falsch
Antwort: Falsch
'''

'''
Aufgabe 25
Der Befehl with open('a.txt', 'r'), stellt sicher, dass die Datei automatisch 
wieder korrekt geschlossen wird
Wahr oder Falsch 
Antwort: Wahr
'''

'''
Aufgabe 26
In Python sind Listen veränderlich, wohingegen Tuple nicht veränderlich sind
Wahr oder Falsch
Antwort: Wahr
'''

'''
Aufgabe 27
Pickeling ist besonders schnell, speichereffizient und sicher
Wahr oder Falsch
Antwort: Falsch
'''

'''
Aufgabe 28
Die Ausgabe des Ausdrucks print(r"\the"=="\the") liefert das Ergebnis false
Wahr oder Falsch
Antwort: Wahr
'''

'''
Aufgabe 29
TextBlob ist eine Bibliothek für die Verarbeitung von Datenbanken und ermöglicht
das Absenden einer SQL-Query
Wahr oder Falsch
Antwort: Falsch
'''

'''
Aufgae 30
NLTKist eine Python-Bibliothek, dioe vorrangig zum Auswerten und Bearbeiten 
tabellarischer Daten gedacht ist. Sie findet hauptsächlich ihren Einsatz
im Preprocessing bei Data Mining
Wahr oder Falsch
Antwort: Falsch
'''

#Aufgabe 31
#Was ist die Ausgabe
print([(b,c) for b in range(3) for c in range(b)])

#Aufgabe 32
#Was ist die Ausgabe
class X:
    def __init__(self):
        self.__x = 100
        self.y = 200
    def print(self):
        print(self.__x, self.y)
class Z(X):
    def __init__(self):
        super().__init__()
        self.__x = 300
        self.y = 400
k = Z()
k.print()

#Aufgabe 33
# Anzahl der Häufigkeit des Wertes 5
l = [5,50,55,555,5555]
print(l.count(5))

#Aufgabe 34
#Funktion division_mit_rest(a,b) die zwei Werte ungleich 0 aufruft
#Tupel als Rückgabe soll ganzzahlige divisions zahl und rest beinhalten
def division_mit_rest(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        mein_tupel = (a//b,a%b)
        return mein_tupel
print(division_mit_rest(5,2))

#Aufgabe 35
#In welcher Reihenfolge werden die Klassen aufgerufen
class A:
    def what_am_i(self):
        print("A")
class B(A):
    def what_am_i(self):
        super().what_am_i()
        print("B")
class C(A):
    def what_am_i(self):
        super().what_am_i()
        print("C")
class D(C, B):
    def what_am_i(self):
        super().what_am_i()
        print("D")
#Antwort: D C B A Object

#Aufgabe 36
'''
Unterschied zwischen
import math = ganze Bibliothek wird mportiert und man kann sie mit math. aufrufen
import math as m = das gleiche wie oben bloß kann man nun die Bibliothek mit m. aufrufen
from math import sqrt = hier wird nur ein bestimmter Teil der Bibliothek importiert und dieser kann ohne math. davor benutzt werden
'''

#Aufgabe 37
#Datei mit Temperaturen einlesen und den max.,  min. und den durchschnittlichen Wert ausgeben
datei = open("temp.txt", "r")
zeilen = datei.readlines()
zahlen = [int(zeile.strip())for zeile in zeilen]
datei.close()
maximum = max(zahlen)
minimum = min(zahlen)
durchschnitt = sum(zahlen) / len(zahlen)
print(maximum)
print(minimum)
print(durchschnitt)

#Aufgabe 38
'''
was ist die Ausgabe wenn die Dictionarys 
x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':6, 'e':5, 'f':6}
angelegt werden und der Quellcode so aussieht
del x['d']
z = x.setdefault('g', 7)
x.update(y)
print(x)
Antwort: die Ausgabe ist {'a':6, 'b':2, 'c':3, 'g':7, 'e':5, 'f':6}
del x['d'] löscht den Inhalt mit 'd' aus dem Dictionary
an die nächste Stelle wird g mit 7 gesetzt
Dictionary x wird mit y aktualisiert und bekommt dessen Werte daher a:6
als letztes geben wir Dictionary x aus
'''

#Aufgabe 39
'''
funktion welches das Wort Donaudampfschiffahrtgesellschaftsstewardess 
in einzelne buchstaben splittet und in eine Liste macht
welche länge hat die Liste ?
doppelte Buchstaben entfernen
'''
wort = "Donaudampfschiffahrtgesellschaftsstewardess"
def split(wort):
    liste = list(wort.lower())
    print(len(liste))
    ohneDopplung = list(set(liste))
    print(ohneDopplung)
    print(len(ohneDopplung))
split(wort)

#Aufgabe 40
'''
Gegeben ist die Liste [[1,2,3],[2,1,3],[4,0,1]]
Code schreiben der die listen nach dem zweiten element sortiert
'''
liste = [[1,2,3],[2,1,3],[4,0,1]]
sortiert = sorted(liste, key=lambda x:x[1])
print(sortiert)

#Aufgabe 41
'''
Es soll eine Textdatei eingelesen werden und die Wörter hello und Hello 
sollen gezählt werden. Die Summe soll ausgegeben werden und in einer Datei 
gespeichert werden, in einer Zeile soll das Wort nur einmal gezählt werden 
auch wenn es mehrmals vorkommt
'''
dateiname = 'hello.txt'
anzahl = 0
with open(dateiname, "r") as datei:
    for zeile in datei:
        if "hello" in zeile:
            anzahl += 1
        if "Hello" in zeile:
            anzahl += 1
with open("ergebnis.txt", "w") as ergebnisdatei:
    ergebnisdatei.write(str(anzahl))

'''
Aufgabe 42
Erstellen ein Balkendiagramm mit Matplotlib zu dem DataFrame data1 wobei 
die x-Achse die Variable Name und die y-Achse die Variable Value besitzt
'''
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
data1 = pd.DataFrame({'Name' : ["A", "B", "C", "D", "E"], 'Value' : [3,12,5,18,45]})
plt.bar(data1["Name"], data1["Value"])
plt.xlabel("Name")
plt.ylabel("Value")
plt.show()


'''
Aufgabe 43
Gegeben ist der nachfolgende Satz in der Variable s. Dieser Satz soll mithilfe NLTK
verarbeitet werden, so dass die Ausgabe mit print das gewünschte Ergebnis erzeugt.
'''
from textblob import TextBlob
s = 'Ich weise höflich darauf hin, dass die Gutachtenerstellung ohne jegliche ' \
    'Verzögerung vorzunhemen ist, da sich der/die Beschuldigte/n in ' \
    'Untersuchungshaft befinden. Ich bitte, mit Herr/Frau xyz'
s1 = TextBlob(s)
print("In dem Modul Digitale Forensik erfolgt die", s1.words[7], ' '.join(s1.words[8:11]), ".")