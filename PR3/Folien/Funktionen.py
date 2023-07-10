def multi_return(a, b):
    return a+b, a-b
a, b = multi_return(3,1)
print(a, b)

def größte_zahl(*zahl):
    max = zahl[0]
    for i in zahl:
        if i > max:
            max = i
    return max
print(größte_zahl(5,3,9,2,0,4))

def grüße(name = "Nico"):
    print("Hallo", name)
grüße()

def twice(f, x):
    return f(f(x))
def quadriere(x):
    return x*x
print(twice(quadriere, 2))

x = 1
def add_one(x):
    x = x+1
    return x
y = add_one(x)
print(y)

def function1(x):
    def function2(y):
        print(y + 2)
        return y + 2
    return 3 * function2(x)
a = function1(2)
print(a)

def add(a,b):
    return a+b
add2 = lambda a, b: a+b
print(add(2, 2))
print(add2(2, 3))

my_list = [1,2,3,4,5,6,7,8]
gerade = list(filter(lambda e: e % 2 == 0, my_list))
print(gerade)

filme = ["Pulp Fiction", "Kill Bill", "Reservoir Dogs"]
filme_groß = list(map(lambda f: f.upper(), filme))
print(filme_groß)

def fak(n):
    return n * fak(n-1) if n > 1 else 1
def fak2(n):
    ergebnis = 1
    for i in range(2, n + 1):
        ergebnis *= i
    return ergebnis

