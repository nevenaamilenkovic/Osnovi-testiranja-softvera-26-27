# VAZNO: Ovaj fajl se mora zvati tacno "conftest.py"!
# Stavite ga u isti folder kao test fajlove
# pytest ga automatski pronalazi — nema importa!
# Struktura foldera:
#   termin_2/
#       src/
#           taskManager.py ->app koja se testira
#       tests/
#           conftest.py ->ovaj fajl
#           test_vezba_fixtures.py ->test fajl koji koristi fixtures iz conftesta
#           test_fixtures.py->test fajl cija jedna funkcija koristi fixture odavde

import pytest
from src.taskManager import BazaKartica,Kartica

@pytest.fixture()
def prazna_baza_conftest():
    return BazaKartica()

"""
imate isto pod komentarom u test_fixture.py
"""
# fixture koji moze biti jako korisan!
# baza koja je popunjena sa test podacima kako ne bi morali da je popunjavamo unutar testa
# vrati bazu sa cetiri kartice
# cisti se automatski nakon svakog testa
# tj vraca se na prethodno dobro stanje za svaki test
@pytest.fixture()
def popunjena_baza():
    # SETUP je priprema (resursa, u nsaem slucaju baze)
    baza=BazaKartica()
    baza.dodaj(Kartica(opis="Uvod u pytest", vlasnik="Nevena"))
    baza.dodaj(Kartica(opis="Selenium", vlasnik="Nevena"))
    baza.dodaj(Kartica(opis="Python", vlasnik="Dusan"))
    baza.dodaj(Kartica(opis="C prograrmiranje", vlasnik="Dusan"))
    # yeild se koristi umesto return! da bi se fixture posle samostalno cistio sve nakon testa
    # u nasem slucaju spremi fresh bazu za sledeci test
    yield baza#test dobija popunjenu bazu ovde tj u trenutku izvrsavanja yeild-a i dalje moze da radi sa njom
    # TEARDOWN je to ciscenje koj se izvrsi nakon testa
    # kod ove nase in memory baze ovo nije potrebno, kada se radi sa pravom bazom
    # u teardown delu bi se zatvarala konekcija i sl
    print("\nBaza je ociscena")
    # Sve pre yield-a je SETUP, a sve nakon je TEARDOWN