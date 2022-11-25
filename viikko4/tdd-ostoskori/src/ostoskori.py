from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = []

    def tavaroita_korissa(self):
        return len(self._ostoskori)

    def hinta(self):
        summa=0
        for ostos in self._ostoskori:
            summa += Ostos(ostos).hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        self._ostoskori.append(Ostos(lisattava))


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset=[]
        for ostos in self._ostoskori:
            ostokset.append(f"{Ostos(ostos.tuote).tuotteen_nimi()} {Ostos(ostos.tuote).lukumaara()} kpl")
        return ostokset

        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
