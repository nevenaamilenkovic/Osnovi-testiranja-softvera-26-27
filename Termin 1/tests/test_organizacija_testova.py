# Za organizaciju testova u pytestu se koriste klase,
# mozete da ih posmatrate kao fascikle za srodne testove, nista vise
# ne treba nam ni dunder metoda init, nema polimorfizma i nasledjivanja!!!

from src.taskManager import BazaKartica,Kartica
class TestBazaKartica:
    def test_prazna_baza(self):
        # arrange assert
        baza=BazaKartica()
        assert baza.broj()==0
    def test_dodata_jedna_kartica(self):
        # arrange
        baza=BazaKartica()
        kartica=Kartica(opis="nesto")
        # act
        baza.dodaj(kartica)
        # assert
        assert baza.broj()==1
# razlika u odnosu na dosadasnje (uvodne) test funkcije
# definicija funkcija:
# uvodne -> def test_prazna_baza(): | "organizovane"-> def test_prazna_baza(self):
# self mora da se stavi ali se nikada ne koristi direktno, mora jer je to python metoda!!!
# pokretanje -> funkcije organizovane po klasama se mogu pokretati samostalo pytest test_fajl.py::TestKlasa::test_fajl
# pytest '.\Termin 1\tests\test_organizacija_testova.py::TestBazaKartica' -v