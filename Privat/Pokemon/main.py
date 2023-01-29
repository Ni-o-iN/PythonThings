from Privat.Pokemon.pokedex import *
import os

class Pokemon:

    def __init__(self, name):
        self.name = name


eins = input("Welches Pokemon?")
eins = eins.lower()


#durchsuchen ob dieses Pokemon hinterlegt ist
folder = "pokedex/"
file = eins + ".py"
file_path = os.path.join(folder, file)
if os.path.exists(file_path):
    print(eins, "ist im Pokedex registriert.")
else:
    print(eins, "ist noch nicht im Pokedex registriert!")
