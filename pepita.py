import alimentos
alimentos = alimentos.alimentos()

class pepita:
    def __init__(self, energia=0):
        self.energia = energia

    def comer(self):
        self.energia = self.energia + alimentos.alpiste()
# your code goes here

# test code
pepita = pepita()


pepita.comer()
pepita.comer()
print(pepita.energia)