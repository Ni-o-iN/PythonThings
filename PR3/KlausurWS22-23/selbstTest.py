#Aufgabe 21
#Was ist die Ausgabe
d = [1,2,3,4,5,6]
print(d[1:3])
#Antwort:

'''
Aufgabe 22
Zur Auflösung der Vererbungshierarchie wird in der Pythonversion 2.3 bzw. 3.x
der C3-Liniearisierungsalgorithmus verwendet
Wahr oder Falsch
Antwort: 
'''

'''
Aufgabe 23
Python besitzt eine dynamische Typisierung
Wahr oder Falsch
Antowrt: 
'''

'''
Aufgabe 24
Python ist keine multiparadigmatische Programmiersprache, denn man kann nur 
objektorientiert programmieren
Wahr oder Falsch
Antwort: 
'''

'''
Aufgabe 25
Der Befehl with open('a.txt', 'r'), stellt sicher, dass die Datei automatisch 
wieder korrekt geschlossen wird
Wahr oder Falsch 
Antwort: 
'''

'''
Aufgabe 26
In Python sind Listen veränderlich, wohingegen Tuple nicht veränderlich sind
Wahr oder Falsch
Antwort: 
'''

'''
Aufgabe 27
Pickeling ist besonders schnell, speichereffizient und sicher
Wahr oder Falsch
Antwort: 
'''

'''
Aufgabe 28
Die Ausgabe des Ausdrucks print(r"\the"=="\the") liefert das Ergebnis false
Wahr oder Falsch
Antwort: 
'''

'''
Aufgabe 29
TextBlob ist eine Bibliothek für die Verarbeitung von Datenbanken und ermöglicht
das Absenden einer SQL-Query
Wahr oder Falsch
Antwort: 
'''

'''
Aufgae 30
NLTK ist eine Python-Bibliothek, die vorrangig zum Auswerten und Bearbeiten 
tabellarischer Daten gedacht ist. Sie findet hauptsächlich ihren Einsatz
im Preprocessing bei Data Mining
Wahr oder Falsch
Antwort: 
'''

#Aufgabe 31
#Was ist die Ausgabe
print([(b,c) for b in range(3) for c in range(b)])
#Antwort: [(1,0), (2,0), (2,1)]

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
#Antwort:

#Aufgabe 33
# Anzahl der Häufigkeit des Wertes 5



#Aufgabe 34
#Funktion division_mit_rest(a,b) die zwei Werte ungleich 0 aufruft
#Tupel als Rückgabe soll ganzzahlige divisions zahl und rest beinhalten


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
x = D()
x.what_am_i()
#Antwort:


#Aufgabe 36
'''
Unterschied zwischen
import math = ganze Bibliothek wird mportiert und man kann sie mit math. aufrufen
import math as m = das gleiche wie oben bloß kann man nun die Bibliothek mit m. aufrufen
from math import sqrt = hier wird nur ein bestimmter Teil der Bibliothek importiert und dieser kann ohne math. davor benutzt werden
'''

#Aufgabe 37
#Datei mit Temperaturen einlesen und den max., min. und den durchschnittlichen Wert ausgeben


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
Antwort:
'''

#Aufgabe 39
'''
funktion welches das Wort Donaudampfschiffahrtgesellschaftsstewardess 
in einzelne buchstaben splittet und in eine Liste macht
welche länge hat die Liste ?
doppelte Buchstaben entfernen wie lange jetzt
'''



#Aufgabe 40
'''
Gegeben ist die Liste [[1,2,3],[2,1,3],[4,0,1]]
Code schreiben der die listen nach dem zweiten element sortiert
'''



#Aufgabe 41
'''
Es soll eine Textdatei eingelesen werden und die Wörter hello und Hello 
sollen gezählt werden. Die Summe soll ausgegeben werden und in einer Datei 
gespeichert werden, in einer Zeile soll das Wort nur einmal gezählt werden 
auch wenn es mehrmals vorkommt
'''



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



'''
Aufgabe 43
Gegeben ist der nachfolgende Satz in der Variable s. Dieser Satz soll mithilfe NLTK
verarbeitet werden, so dass die Ausgabe mit print das gewünschte Ergebnis erzeugt.
'''
from textblob import TextBlob
s = 'Ich weise höflich darauf hin, dass die Gutachtenerstellung ohne jegliche ' \
    'Verzögerung vorzunhemen ist, da sich der/die Beschuldigte/n in ' \
    'Untersuchungshaft befinden. Ich bitte, mit Herr/Frau xyz'
print("In dem Modul Digitale Forensik erfolgt die", s1.words[7], ' '.join(s1.words[8:11]), ".")