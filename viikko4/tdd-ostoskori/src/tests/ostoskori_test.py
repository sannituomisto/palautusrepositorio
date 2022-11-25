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
