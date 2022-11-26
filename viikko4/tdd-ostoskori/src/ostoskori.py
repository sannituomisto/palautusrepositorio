from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = []
        self._tavarat=0

    def tavaroita_korissa(self):
        return self._tavarat

    def hinta(self):
        summa=0
        for ostos in self._ostoskori:
            summa += Ostos(ostos).hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        if self.tavaroita_korissa() == 0:
            self._ostoskori.append(Ostos(lisattava))
            self._tavarat += 1
            return
        for ostos in self._ostoskori:
            if Ostos(lisattava).tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                self._tavarat += 1
                return
        self._ostoskori.append(Ostos(lisattava))
        self._tavarat += 1



    def poista_tuote(self, poistettava: Tuote):
        if self.tavaroita_korissa() == 0:
            return
        for ostos in self._ostoskori:
            if Ostos(poistettava).tuotteen_nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)
                self._tavarat -= 1
                return

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset=[]
        for ostos in self._ostoskori:
            ostokset.append(f"{ostos.tuotteen_nimi()} {ostos.lukumaara()} kpl")
        return ostokset

        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
