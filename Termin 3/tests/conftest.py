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

@pytest.fixture()
def biblioteka_sa_pozajmljenom(biblioteka_sa_knjigama):
    za_zajam_id=biblioteka_sa_knjigama.sve_knjige()[0].id
    biblioteka_sa_knjigama.pozajmi(za_zajam_id)
    yield za_zajam_id,biblioteka_sa_knjigama
