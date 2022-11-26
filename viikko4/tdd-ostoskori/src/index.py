from ostoskori import Ostoskori
from tuote import Tuote



def main():
    ostoskori = Ostoskori()
    maito = Tuote("Maito", 3)
    kahvi=Tuote("Kahvi", 4)
    ostoskori.lisaa_tuote(maito)
    ostoskori.lisaa_tuote(maito)
    print(ostoskori.ostokset())

    


if __name__ == "__main__":
    main()
