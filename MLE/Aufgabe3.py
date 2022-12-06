import random
from random import randrange
import numpy

gene = 10
geschenkeAnzahl = 4
sackGroeße = 4
geschenkeGroeßen = numpy.zeros(geschenkeAnzahl)
test = numpy.zeros((gene, geschenkeAnzahl))
bestePackung = 0
zweitBestePackung = 0
besteGene = 0
zweitBesteGene = 0
r = 0.8

#geschenke groeßen setzen
for i in range(geschenkeAnzahl):
    geschenkeGroeßen[i] = random.uniform(0.1 , 2.0)
    #print("Geschenk Nummer ", i, " ist ", geschenkeGroeßen[i], " groß.")

#entscheiden welche geschenke eingepackt werden
for i in range(gene):
    print("gene Nummer : ", i)
    jetzigePackung = 0
    for j in range(geschenkeAnzahl):
        einpacken = random.randrange(2)
        if einpacken == 1:
            test[i][j] = 1
            jetzigePackung += geschenkeGroeßen[j]
            print(test[i][j])
            print("Das Geschenk ist", geschenkeGroeßen[j], "gross")
        else:
            test[i][j] = 0
            print(test[i][j])
        if jetzigePackung > sackGroeße:
            test[i][j] = 0
            jetzigePackung -= geschenkeGroeßen[j]
            print("Das Geschenk mit der grösse", geschenkeGroeßen[j], "passt nicht mehr in den Sack und wird wieder entnommen")
        if jetzigePackung > bestePackung:
            zweitBestePackung = bestePackung
            bestePackung = jetzigePackung
            zweitBesteGene = besteGene
            besteGene = i

    print("Die jetzige Packung ist :", jetzigePackung)
print("Die beste Packung ist :", bestePackung, "gepackt und ist die Genenummer", besteGene)
print("Die zweit beste Packung ist :", zweitBestePackung, "gepackt und ist die Genenummer", zweitBesteGene)