#Aufgabe 1
#Was ist die Ausgabe
d = [1,2,3,4,5,6]
print(d[1:3])

#Aufgabe 2
#Was ist die Ausgabe
print([(b,c) for b in range(3) for c in range(b)])

#Aufgabe 3
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

#Aufgabe 4
# Anzahl der Häufigkeit des Wertes 5
l = [5,50,55,555,5555]
print(l.count(5))

#Aufgabe 5
#Funktion division_mit_rest(a,b) die zwei Werte ungleich 0 aufruft
#Tupel als Rückgabe soll ganzzahlige divisions zahl und rest beinhalten
def division_mit_rest(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        mein_tupel = (a//b,a%b)
        return mein_tupel
print(division_mit_rest(5,2))