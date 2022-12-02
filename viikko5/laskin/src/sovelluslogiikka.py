class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.kumottu = 0

    def miinus(self, arvo):
        self.kumottu = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.kumottu = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.kumottu = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.kumottu = self.tulos
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.kumottu
