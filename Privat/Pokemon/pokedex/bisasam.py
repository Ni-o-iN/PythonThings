from Privat.Pokemon.main import Pokemon

class bisasam(Pokemon):

    def __init__(self, geschlecht, level):
        self.geschlecht = geschlecht
        self.level = level

    def welchesGecshlecht(self):
        return self.geschlecht

    def welchesLevel(self):
        return self.level

    def welchesPokemon(self):
        return "Es ist " + self.name