import alimentos


class pepita:
    def __init__(self):
        self._energy = 0

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    def energia(self):
        return self.energy

    def volar(self, kms):
        self._energy -= kms + 10

    def comer(self, cosa, gramos):
        self._energy += cosa.energiaPorGramo() * gramos

    def estaDebil(self):
        return self.energy < 50

    def estaFeliz(self):
        return 500 < self.energy < 1000

    def cuantoQuiereVolar(self):
        cuanto = self.energy() / 5
        if 300 < self.energy < 400:
            cuanto += 10
        if self.energy % 20 == 0:
            cuanto += 15
        return cuanto

    def salirAComer(self):
        self.volar(5)
        self.comer(alimentos.alpiste, 80)
        self.volar(5)

    def haceLoQueQuieras(self):
        if self.estaDebil():
            self.comer(alimentos.alpiste, 20)
        elif self.estaFeliz():
            self.volar(8)


# your code goes here

# test code
pepita = pepita()
mijo = alimentos.mijo()
mijo.mojarse()
pepita.comer(mijo, 1)
print(pepita.energy)
print(pepita.estaFeliz())

pepita.salirAComer()
pepita.salirAComer()
print(pepita.energy)

pepita.haceLoQueQuieras()
print(pepita.energy)
