'''
print("Hello World")

a = 5
b = "5"
c = 'hi'
print(a, ":", type(a), b, ":", type(b), c, ":", type(c))

print(2**2) #potenzierung
print(5//2) #ganzzahl division
'''
my_tuple = (1,2,3)  #nicht veränderbar
list(my_tuple)  #konvention von tuple zu liste möglich
print(my_tuple) #mit einem * vor my_tuple ist die Ausgabe -> 1 2 3
my_list = [1,2,3]   #veränderbar, liste in tuple ist auch möglich
tuple(my_list)  #konvention von liste zu tuple möglich
länder_code = {'deutschland' : 'de', 'england' : 'en', 'niederlande' : 'ne'}
länder_code['niederlande'] = 'neth'
print(länder_code)
def test():
    return 'A', 'B', 'C'
a = test()
print(a)

a, b, c = test()
print(a, b, c)

