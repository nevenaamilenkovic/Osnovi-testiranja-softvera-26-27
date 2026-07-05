import pytest
from src.biblioteka_servis import EmailServis,IzvestajServis,BibliotekaServis,Knjiga
from unittest.mock import MagicMock,call

@pytest.fixture()
def lazni_email():
    # lazni email servis koji ne salje prave emailove
    return MagicMock(spec=EmailServis)

@pytest.fixture()
def lazni_izvestaj():
    # lazni servis za generisanje izvestaja koji ne generise prave fajlove
    return MagicMock(spec=IzvestajServis)

@pytest.fixture()
def servis(lazni_email,lazni_izvestaj):
    # biblioteka servis sa mock zavisnostima
    return BibliotekaServis(
        email_servis=lazni_email,
        izvestaj_servis=lazni_izvestaj,
    )

@pytest.fixture()
def servis_sa_knjigom(servis):
    # servis sa jednom dodatom knjigom
    knjiga_id=servis.dodaj_knjigu(
        Knjiga(naslov="Baze podataka",autor="Dr Snezana R. Popovic",godina=2024)
    )
    return servis,knjiga_id