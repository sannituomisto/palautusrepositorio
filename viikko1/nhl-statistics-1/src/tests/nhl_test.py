import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_loytaa_pelaajan(self):
        pelaaja=self.statistics.search("Yzerman")

        self.assertAlmostEqual(str(pelaaja),"Yzerman DET 42 + 56 = 98")


    def test_ei_loyda_pelaajaa(self):
        pelaaja=self.statistics.search("Tuomisto")

        self.assertAlmostEqual(pelaaja,None)
    

    def test_loytaa_joukkueen_pelaajat_lkm(self):
        pelaajat=self.statistics.team("EDM")
        pelaajat_lkm=len(pelaajat)

        self.assertAlmostEqual(pelaajat_lkm,3) 


    def test_loytaa_joukkueen_pelaajat(self):
        pelaajat=self.statistics.team("EDM")
        laskin=0
        for pelaaja in pelaajat:
            if pelaaja.team == "EDM":
                laskin += 1
            else:
                laskin -= 1

        self.assertAlmostEqual(laskin,3)


    def test_top_pelaajat(self):
        top=self.statistics.top(2)
        pelaajat=[]
        for pelaaja in top:
            pelaajat.append(pelaaja.name)
        result=", ".join(pelaajat)

        self.assertEqual(result,"Gretzky, Lemieux, Yzerman")

    
    def test_top_pelaajat_points(self):
        top=self.statistics.top(2,1)
        pelaajat=[]
        for pelaaja in top:
            pelaajat.append(pelaaja.name)
        result=", ".join(pelaajat)

        self.assertEqual(result,"Gretzky, Lemieux, Yzerman")

    def test_top_pelaajat_goals(self):
        top=self.statistics.top(2,2)
        pelaajat=[]
        for pelaaja in top:
            pelaajat.append(pelaaja.name)
        result=", ".join(pelaajat)

        self.assertEqual(result,"Lemieux, Yzerman, Kurri")

    def test_top_pelaajat_assists(self):
        top=self.statistics.top(2,3)
        pelaajat=[]
        for pelaaja in top:
            pelaajat.append(pelaaja.name)
        result=", ".join(pelaajat)

        self.assertEqual(result,"Gretzky, Yzerman, Lemieux")