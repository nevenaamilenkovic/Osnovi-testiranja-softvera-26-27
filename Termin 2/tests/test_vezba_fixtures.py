# Pokretanje
# pytest test_vezba_fixtures.py -v
# pytest test_vezba_fixtures.py -v -s (-s prikazuje print iz teardowna)
# pytest test_vezba_fixtures.py -v --setup-show (prikazuje redosled setup/teardown)

from src.taskManager import Kartica

# osnovni fixture prazna i popunjena baza iz conftesta

def test_broj_nula_kartica(prazna_baza_conftest):
    assert prazna_baza_conftest.broj()==0

def test_dodaj_u_praznu_bazu(prazna_baza_conftest):
    kartica_id=prazna_baza_conftest.dodaj(Kartica(opis="novi zadatak"))
    assert prazna_baza_conftest.broj()==1
    assert prazna_baza_conftest.uzmi(kartica_id).opis=="novi zadatak"

def test_broj_cetiri_kartice(popunjena_baza):
    assert popunjena_baza.broj()==4

# test pada zbog slovne greske pri popunjavanju baze
# nema C programiranje nego C prograrmiranje
# evo jednog dobrog testa hahah kojim se testira i kakvi su test podaci ubaceni
def test_lista_vraca_sve_kartice(popunjena_baza):
    # arrange
    sve=popunjena_baza.lista()
    # act
    opisi=[k.opis for k in sve]
    # assert
    assert "C programiranje" in opisi
    assert "Selenium" in opisi

# vise testova jedan fuxture
# svaki test dobija svoju kopiju fixture-a (pod uslovom da je scope="function")
# bilo kakva promena u jednom testu ne utice na drui test
def test_dodaj_ne_utice_na_drugi_test(prazna_baza_conftest):
    prazna_baza_conftest.dodaj(Kartica(opis="ovaj task vidi samoo ovaj test!!"))
    assert prazna_baza_conftest.broj()==1

def test_baza_je_ponovo_prazna(prazna_baza_conftest):
    assert prazna_baza_conftest.broj()==0#prethodni test je dodao jednu karticu, ovaj test koristi SVEZ FIXTURE

# FIXTURE U KLASI radi isto samo se dodaju
# @pytest.fixture(scope="class") nije dat fixturi tako da nece biti jedna baza za sve testove u klasi!!!
class TestZapocniZavrsi:
    # testovi za promenu stanja
    def test_zapocni(self,popunjena_baza):
        # arrange->uzima se id prve kartice
        prva_id=popunjena_baza.lista()[0].id
        # act
        # inace intelisense/autokomplit ovde ne rade bas
        popunjena_baza.zapocni(prva_id)
        # assert
        assert popunjena_baza.uzmi(prva_id).stanje=="u_toku"

    def test_zavrsi(self,popunjena_baza):
        prva_id=popunjena_baza.lista()[0].id
        # print(f"\n{popunjena_baza.uzmi(prva_id).stanje}")#na cekanju!!
        popunjena_baza.zavrsi(prva_id)
        assert popunjena_baza.uzmi(prva_id).stanje=="zavrseno"

    def test_svaki_test_dobija_svez_fixture(self,popunjena_baza):
        # bez obzira sto je prethodni test promenio stanje
        # ovaj test vidi originalnu bazu, gde je stanje za karticu 1 na cekanju!
        prva_id=popunjena_baza.lista()[0].id
        assert popunjena_baza.uzmi(prva_id).stanje=="na_cekanju"


# koriscenje scope class fixture
class TestZapocniZavrsiScopeClass:
    # testovi za promenu stanja sa jednom bazom
    def test_zapocni(self,popunjena_baza_klasni):
        prva_id=popunjena_baza_klasni.lista()[0].id
        popunjena_baza_klasni.zapocni(prva_id)
        # assert
        assert popunjena_baza_klasni.uzmi(prva_id).stanje=="u_toku"

    def test_zavrsi(self,popunjena_baza_klasni):
        prva_id=popunjena_baza_klasni.lista()[0].id
        print(f"\n{popunjena_baza_klasni.uzmi(prva_id).stanje}")#prvi zapoceo
        assert popunjena_baza_klasni.uzmi(prva_id).stanje=="u_toku"
        popunjena_baza_klasni.zavrsi(prva_id)
        assert popunjena_baza_klasni.uzmi(prva_id).stanje=="zavrseno"
# ne dobija svez fixturee
    def test_svaki_test_u_ovoj_klasi_isti_fixture(self,popunjena_baza_klasni):
        prva_id=popunjena_baza_klasni.lista()[0].id
        assert popunjena_baza_klasni.uzmi(prva_id).stanje=="zavrseno"#prethodni test zavrsio zadatak
        # dakle promene se prenose!!! scope=class se koristi samo kada testovi namerno zavise jedni od drugih
        # pytest .\tests\test_vezba_fixtures.py::TestZapocniZavrsiScopeClass -v --setup-show TEARDOWN TEK POSLE POSLEDNJEG TESTA!!!!!

# takodje moguce je da jedan FIXTURE koristi drugi FIXTURE
# OVO TREBA U CONFTEST DA IDE ALI EVO OVDE PRIMERA RADI
import pytest
@pytest.fixture()
def kartica_u_bazi(prazna_baza_conftest):
    kartica_id=prazna_baza_conftest.dodaj(Kartica(opis="Test kartica"))
    return prazna_baza_conftest,kartica_id

def test_fixture_u_fixture(kartica_u_bazi):
    baza,id=kartica_u_bazi
    assert baza.uzmi(id).opis=="Test kartica"