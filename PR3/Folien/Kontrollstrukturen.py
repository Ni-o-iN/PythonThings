#If
a = 1
if (a == 5):
    print("gleich")
elif (a < 0):
    print("negative zahl")
else:
    print("ungleich")
#tenäres if
b = 5
c = 6
max = b if b > c else c
print(max)

#While
d = 0
while(d != 5):
    print(d, "ist noch nicht 5")
    d += 1
e = 0
f = 0
while(f <= 5):
    e = e + f
    f += 1
print(e)

#For
g = 0
for i in range(6):
    g = g+i
print(g)
filme = ["Pulp Fiction", "Kill Bill", "Reservoir Dogs"]
for i in filme:
    print(i)
for index, f in enumerate(filme):
    print(index, f)
barData = [5,2,8,4]
for index, value in enumerate(barData):
    bar = '*' * value
    print(f"Index: {index}, Wert {value}, Balken: {bar}")

#Break and Continue
n = 64
for i in range(0, 10):
    if i ** 2 == n:
        print("Die Wurzel von ", n, "ist", i)
        break
print("Nach der Schleife")
for num in range(2, 10):
    if num % 2 == 0:
        print(num, "ist gerade")
        continue
    else:
        print(num, "ist ungerade")

#Pass
ampel_farbe = "grün"
if ampel_farbe == "grün":
    pass
elif ampel_farbe == "gelb":
    print("Gib Gas")
else:
    print("Anhalten")