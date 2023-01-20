a = (1,2,3,4)

print(a)
print(*a)

print(a[0])

print(a[1:3])
print(a[:2])
print(a[2:])

#a[0] = 3    #tuples sind unveränderbar FEHLER
print(a)


b = 'A', 'B', 'C'   #Packing
print(b)
c, d, e = b         #Unpacking
print(c, d, e)


def func():
    return 'D', 'E', 'F'

x = func()
print(x)

f, g, h = func()
print(f, g, h)

tu = ("test", "test2", [1,2,3])
print(tu)
tu[2][2] = 4
print(tu)