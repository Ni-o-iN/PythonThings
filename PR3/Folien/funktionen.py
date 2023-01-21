def begrüßen(name):
    print("Hallo ", name)
begrüßen("Nico")


def multi_return(): #mehrere returns möglich
    return (1,2)
a,b = multi_return()
print(a,b)


def max(*c):    #mit * können beliebig viele Parameter übergeben werden
    result = c[0]
    for i in c:
        if result < i:
            result = i
    return result
print(max(2,5,3,7,1))


def twice(f, x):
    return f(f(x))
def quadriere(x):
    return x*x
print(twice(quadriere, 2))


def minus(x):   #funktion in funktion
    def plus(y):
        return y + 2
    return plus(x) - 1
c = minus(4)
print(c)


add = lambda a,b: a + b #lambda
print(add(3,5))


