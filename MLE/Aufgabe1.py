import random
from random import randrange
import numpy

stadteanzahl = 100
mein_array = numpy.zeros((stadteanzahl, stadteanzahl))
rundreise = numpy.arange(0, stadteanzahl)

#tabelle erzugen
def tabelle():
    for i in range(stadteanzahl):
        for j in range(stadteanzahl):
            mein_array[i][j] = randrange(20)+1
            mein_array[j][i] = mein_array[i][j]
            mein_array[i][i] = 0
    print(mein_array)

if __name__ == "__main__":
    tabelle()
    # anfangs strecke berechen
    strecke = mein_array[rundreise[0]][rundreise[stadteanzahl - 1]]
    for j in range(stadteanzahl - 1):
        strecke = mein_array[rundreise[j + 1]][j] + strecke
    print("Die Anfangs Strecke beträgt: ", strecke)
    #n mal durchlaufen
    for durchgänge in range(1000):
        #tauschen
        n = randrange(stadteanzahl)
        m = randrange(stadteanzahl)
        rundreise[n], rundreise[m] = rundreise[m], rundreise[n]
        #strecke nach swap berechnen
        neue_strecke = mein_array[rundreise[0]][rundreise[stadteanzahl-1]]
        for j in range(stadteanzahl-1):
            neue_strecke = mein_array[rundreise[j+1]][rundreise[j]] + neue_strecke
        if neue_strecke < strecke:
            print("Die neue Strecke beträgt : ", neue_strecke)
            strecke = neue_strecke
        else:
            rundreise[n], rundreise[m] = rundreise[m], rundreise[n]