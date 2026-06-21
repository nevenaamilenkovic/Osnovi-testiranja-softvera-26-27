from src.taskManager import Kartica,BazaKartica

"""
Zadatak 1: Klasa BazaKartica ima metodu dodaj() koja prima
kartica objekat.
Potrebno je napisati test kojim se proverava da li se po
dodavanju nove kartice u "praznu bazu" pozivanjem metode
broj() vraca 1 (odnosno intidzer, dodata kartica koja je jedina u bazi)

AAA -> Arrange, Act,Assert
"""
def test_prva_kartica():
    # Arrange
    baza = BazaKartica()
    kartica = Kartica(opis="termin 1",vlasnik="Nevena",stanje="na_cekanju")
    # Act
    baza.dodaj(kartica)
    # Assert
    assert baza.broj() == 1

"""
Metoda dodaj() iz klase BazaKartica vraca id novokreirane kartice.
Potrebno je napisati test koji proverava da li ID koji je 
vratila metoda dodaj zaista postoji u bazi.
Hint: metoda uzmi() vraca karticu iz baze po id-ju
"""
def test_dodaj_karticu():
    # Arrange
    baza=BazaKartica()
    kartica=Kartica(opis="test 2",vlasnik="Nevena",stanje="na_cekanju")
    # Act
    id_dodate_kartice=baza.dodaj(kartica)
    kartica_iz_baze=baza.uzmi(id_dodate_kartice)
    # Assert
    assert id_dodate_kartice==kartica_iz_baze.id
    assert kartica==kartica_iz_baze
