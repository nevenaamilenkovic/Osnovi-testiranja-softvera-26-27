import pytest
from src.biblioteka import Biblioteka, Knjiga


@pytest.fixture()
def prazna_biblioteka():
    return Biblioteka(naziv="Test Biblioteka")

@pytest.fixture()
def popunjena_biblioteka():
    b=Biblioteka(naziv="Test biblioteka")
    b.dodaj_knjigu(Knjiga("Python bez oklevanja", "Paul Barry",2017))
    b.dodaj_knjigu(Knjiga("Baze podataka","Snezana Popovic",2024))
    b.dodaj_knjigu(Knjiga("Zlocin i kazna","Fjodor Dostojevski",1866))
    return b