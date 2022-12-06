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
    temperatur = 20
    epsilon = 0.0001
    tabelle()
    # anfangs strecke berechen
    strecke = mein_array[rundreise[0]][rundreise[stadteanzahl - 1]]
    for j in range(stadteanzahl - 1):
        strecke = mein_array[rundreise[j + 1]][j] + strecke
    print("Die Anfangs Strecke beträgt: ", strecke)
    startstrecke = strecke
    #n mal durchlaufen
    while temperatur > epsilon:
        zufällig = random.uniform(0, 1)
        #tauschen
        n = randrange(stadteanzahl)
        m = randrange(stadteanzahl)
        rundreise[n], rundreise[m] = rundreise[m], rundreise[n]
        #strecke nach swap berechnen
        neue_strecke = mein_array[rundreise[0]][rundreise[stadteanzahl-1]]
        for j in range(stadteanzahl-1):
            neue_strecke = mein_array[rundreise[j+1]][rundreise[j]] + neue_strecke
        #hier muss noch was gemacht werden
        if neue_strecke < strecke:
            print("Die neue Strecke beträgt : ", neue_strecke)
            strecke = neue_strecke
        else:
            print(numpy.exp((-neue_strecke-(-strecke))/temperatur))
            if numpy.exp((-neue_strecke-(-strecke))/temperatur) > zufällig:
                print("Die neue Strecke beträgt : ", neue_strecke)
                strecke = neue_strecke
            else:
                rundreise[n], rundreise[m] = rundreise[m], rundreise[n]
        temperatur = temperatur - epsilon