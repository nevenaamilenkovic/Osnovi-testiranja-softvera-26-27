import pytest
from unittest.mock import MagicMock
from src.biblioteka_servis import Knjiga,EmailServis,IzvestajServis,BibliotekaServis

@pytest.fixture()
def lazni_email():
    return MagicMock(spec=EmailServis)

@pytest.fixture()
def lazni_izvestaj():
    # ne pise fajlove vise je mock za unittestove da proverimo poziva li se servis
    return MagicMock(spec=IzvestajServis)


@pytest.fixture()
def unit_servis(lazni_email,lazni_izvestaj):
    return BibliotekaServis(lazni_email,lazni_izvestaj)

@pytest.fixture()
def pravi_izvestaj():
    # zaista pise fajlove!
    return IzvestajServis

@pytest.fixture()
def servis(lazni_email,pravi_izvestaj):
    # integration fixture
    # email servis je mock jer necemo da ssaljemo prave mejlove
    # izvestaj servis je pravi jer treba zaista da pisemo fajlove, tj testiramo upis u njih
    return BibliotekaServis(lazni_email,pravi_izvestaj)

@pytest.fixture()
def servis_sa_knjigama(servis):
    servis.dodaj_knjigu(Knjiga("Python bez oklevanja", "Paul Barry", 2017))
    servis.dodaj_knjigu(Knjiga("Baze podataka", "Snezana Popovic", 2024))
    servis.dodaj_knjigu(Knjiga("Go bez oklevanja", "Jay McGavren", 2021))
    return servis
