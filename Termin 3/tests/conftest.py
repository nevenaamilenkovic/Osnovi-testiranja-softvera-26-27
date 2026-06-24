import pytest
from src.biblioteka import Biblioteka,Knjiga

@pytest.fixture()
def prazna_biblioteka():
    biblioteka=Biblioteka(naziv="Biblioteka")
    yield biblioteka

@pytest.fixture()
def biblioteka_sa_knjigama(prazna_biblioteka):
    b=prazna_biblioteka
    b.dodaj_knjigu(Knjiga(naslov="SQL programiranje",autor="Dr Snezana R. Popovic",godina=2020))
    b.dodaj_knjigu(Knjiga(naslov="Baze podataka",autor="Dr Snezana R. Popovic",godina=2024))
    b.dodaj_knjigu(Knjiga(naslov="Python bez oklevanja",autor="Paul Barry",godina=2017))
    yield b
    print("Biblioteka ociscena")


