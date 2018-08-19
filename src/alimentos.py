class alpiste:
    @staticmethod
    def energiaPorGramo():
        return 4

class mondongo:
    @staticmethod
    def energiaPorGramo():
        return 100

class bigMac:
    @staticmethod
    def energiaPorGramo():
        return 2

class bigMac:
    @staticmethod
    def energiaPorGramo():
        return 20

class bigMac:
    @staticmethod
    def energiaPorGramo():
        return 9

class mijo:
    def __init__(self):
        self.estaMojado = False

    estaMojado: bool

    def mojarse(self):
        self.estaMojado = True

    def secarse(self):
        self.estaMojado = False

    def energiaPorGramo(self):
        proporciona = 20
        if self.estaMojado:
            proporciona = 15
        return proporciona

class canelones:
    def __init__(self):
        self.haySalsa = False
        self.hayQueso = False

    haySalsa: bool
    hayQueso: bool

    def ponerQueso(self):
        self.hayQueso = True

    def quitarQueso(self):
        self.hayQueso = False

    def ponerSalsa(self):
        self.haySalsa = True

    def quitarSalsa(self):
        self.haySalsa = False

    @staticmethod
    def energiaPorGramo(self):
        proporciona = 20
        if self.haySalsa:
            proporciona += 15
        if self.hayQueso:
            proporciona += 7
        return proporciona
