class Auto:
    autos_anzahl = 0
    def __init__(self, km_h):
        self.km_h = km_h
        Auto.autos_anzahl += 1
    def fahr(self):
        print("Dieses Auto kann", self.km_h, "schnell fahren")
audi = Auto(250)
audi.fahr()
lambo = Auto(300)
print(lambo.km_h)
print(Auto.autos_anzahl)

class Circle:
    pass
my_circle = Circle
my_circle.radius = 5
print(2 * 3.1415 * my_circle.radius)

class A(B,C):
    def I(self):
        print('A')
class B(D,E):
    def I(self):
        A.I()
        print('B')
class C(E,D):
    def I(self):
        A.I()
        print('C')
class D(F):
    def I(self):
        B.I()
        C.I()
        print('D')
class E(F):
    def I(self):
        print('E')
class F:
    def I(self):
        print('F')
test = F
test.mro()
