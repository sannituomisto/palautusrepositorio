import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuote1=Tuote("maito",2)
        self.tuote2=Tuote("kahvi",5)
        self.tuote3=Tuote("leipa",4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        korin_saldo=self.kori.tavaroita_korissa()
        self.assertEqual((self.kori.hinta(),korin_saldo), (0,0))

    def test_tuotteen_lisäämisen_jälkeen_tavaroiden_lkm_ostoskorissa(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        korin_saldo=self.kori.tavaroita_korissa()
        self.assertEqual(korin_saldo, 1)

    def test_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        korin_hinta=self.kori.hinta()
        self.assertEqual(korin_hinta, 2)

    def test_2_eri_tuotteen_lisäämisen_jälkeen_tavaroiden_lkm_ostoskorissa(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        korin_saldo=self.kori.tavaroita_korissa()
        self.assertEqual(korin_saldo, 2)

    def test_2_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        korin_hinta=self.kori.hinta()
        self.assertEqual(korin_hinta, 7)

    def test_2_saman_tuotteen_lisäämisen_jälkeen_tavaroiden_lkm_ostoskorissa(self):
            self.setUp()
            self.kori.lisaa_tuote(self.tuote1)
            self.kori.lisaa_tuote(self.tuote1)
            korin_saldo=self.kori.tavaroita_korissa()
            self.assertEqual(korin_saldo, 2)