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

    def test_2_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_oikea(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        korin_hinta=self.kori.hinta()
        self.assertEqual(korin_hinta, 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.tuote1)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.tuote1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos, "maito 1 kpl")

    def test_2_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    
    def test_2_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisäämisen_jalkeen_ostoskori_näyttää_oikealta(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset, "maito 2 kpl")

    def test_kahden_saman_tuotteen_lisäämisen_jalkeen_toinen_poistetaan_ja_ostoskori_näyttää_oikealta(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.poista_tuote(self.tuote1)
        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset, "maito 1 kpl")

    def test_jos_koriin_lisätään_tuote_ja_sama_tuote_poistetaan_niin_kori_on_tyhjä(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.poista_tuote(self.tuote1)
        ostokset = self.kori.ostokset()
        korin_hinta=self.kori.hinta()
        self.assertEqual(len(ostokset), 0)
        self.assertEqual(korin_hinta, 0)

    def test_ostoskori_tyhjennetään_metodilla_tyhjennä(self):
        self.setUp()
        self.kori.lisaa_tuote(self.tuote1)
        self.kori.lisaa_tuote(self.tuote2)
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

