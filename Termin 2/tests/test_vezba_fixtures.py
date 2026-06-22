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