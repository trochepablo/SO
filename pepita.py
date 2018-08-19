import alimentos

alimentos = alimentos.alimentos()


class pepita:
    def __init__(self, energy = 0):
        self.energy = energy

    def comer(self, cosa, gramos):
        self.energy = self.energy + cosa.alpiste(gramos)


# your code goes here

# test code
pepita = pepita()

pepita.comer(alimentos, 50)
print(pepita.energy)
