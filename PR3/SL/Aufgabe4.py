import math
import sys

n = 1
summe = 0
gefunden = False

while not gefunden:
    summe += 1/n**2
    if (1.644934 - summe) < sys.float_info.epsilon:
        print("letzter Durchgang :", n)
        gefunden = True
    n += 1
    print(summe)