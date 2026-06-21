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
Zadatak 2: Metoda dodaj() iz klase BazaKartica vraca id novokreirane kartice.
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
    # ovde imamo dve varijante provere, obe su okej
    # Samo sto dataclass kartica poredi polja vlasnik,stanje,opis a id ignorise
    assert id_dodate_kartice==kartica_iz_baze.id#da li vraceni id postoji u bazi
    assert kartica==kartica_iz_baze#da li su podaci kartice ispravno sacuvani

"""
Zadatak 3: Napisati test koji proverava metodu uzmi(),
potrebno je proveriti da li metoda baca KeyError kada se trazi
kartica sa ID-jem koji ne postoji u bazi
"""
import pytest
def test_uzmi_nepostojeci_id():
    # arrange
    baza=BazaKartica()
    #act i assert
    with pytest.raises(KeyError):
        baza.uzmi(999)

"""
Zadatak 4: Napisati test za metodu obrisi(). Potreno je proveriti da li metoda
broj() nakon brisanja kartice vraca 0.
"""
def test_obrisi():
    # arrange
    baza=BazaKartica()
    kartica=Kartica(vlasnik="Nevena",stanje="na_cekanju",opis="zadatak 4")
    baza.dodaj(kartica)
    # act
    baza.obrisi(1)
    # assert
    assert baza.broj()==0
"""
Bolja varijanta resenja za zadatak 4
u prvom testu imamo tzv slabost, jer se pretpostavlja da ce uvek id da bude 1 (ok je ali nije sigurno app moze da se menja)
Najbolje je sacuvati id koji vrati metoda dodaj pa tek onda brisati
"""
def test_obrisi_bolja_varijanta():
        # arrange
    baza=BazaKartica()
    kartica=Kartica(vlasnik="Nevena",stanje="na_cekanju",opis="zadatak 4")
    id=baza.dodaj(kartica)
    # act
    baza.obrisi(id)
    # assert
    assert baza.broj()==0

"""
"""