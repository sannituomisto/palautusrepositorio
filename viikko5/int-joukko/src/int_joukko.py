KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI
        self.kasvatuskoko = OLETUSKASVATUS
        self.ljono = []

    def vaara_kapasiteetti(self):
        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = self.kapasiteetti

    def vaara_kavatuskoko(self):
        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise Exception("kapasiteetti2")
        else:
            self.kasvatuskoko = self.kasvatuskoko

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        else:
            return False


    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono.append(n)
            return True

        return False


    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)

        return False


    def mahtavuus(self):
        return len(self.ljono)

    def to_int_list(self):
        kopio=[]
        for alkio in self.ljono:
            kopio.append(alkio)
        return kopio

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if len(self.ljono) == 0:
            return "{}"
        elif len(self.ljono) == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, len(self.ljono) - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[len(self.ljono) - 1])
            tuotos = tuotos + "}"
            return tuotos
