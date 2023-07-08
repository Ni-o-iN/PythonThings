googol = 10**100
print(googol)

#3g = 1
#87 = 1
score_4 = 1

#Ich
lieblingsfilm = "Avengers Endgame"
geld = 12
#Kino
film = "Avengers Endgame"
eintritt = 13
#Eisidiele
eis = 6
#Kann ich ins Kino
print(lieblingsfilm==film and geld>=eintritt)
#Kann ich Eis essen
print(geld>=eis)

my_list = [1,2,"Hello",4,5]
my_list[1] = 0
my_list.append(6)
my_list[0:0] = [0,1]
#richtiges kopieren
my_list2 = my_list[:]
unpacking_list = ['a', 'b', 'c']
a, b, c = unpacking_list    #a='a', b='b', c='c'
#list comprehensions
comrehension_list = [i**2 for i in range(5)]

my_tuple = (1,2,3,4)
def more_returns():
    return "Das", "Klappt", "Ja"
a, b, c = more_returns()
print(a, b, c)

my_dictionary = {1:"one", 2:"two", 3:"three"}
print(my_dictionary.get(1))

#Geben Sie aus wie oft die einzelnen Wörter des Satzes: „To be or not to be“ jeweils vorkommen.
satz = "To be or not to be"
vorkommen = {}
for word in satz.split():
    vorkommen[word] = vorkommen.get(word, 0) +1
print(vorkommen)

my_set = set([1,2,3,4,2,1,5])
print(my_set)
set2 = {x for x in "python rocks" if x not in "aeiou"}
print(set2)

string1 = "Hello"
string2 = "World"
print(string1 + string2)
print(string1, string2)
print(string1 * 2, string2)
