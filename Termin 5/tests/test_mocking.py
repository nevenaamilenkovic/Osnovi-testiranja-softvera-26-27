# Porebno je instalirati pytest-mock i pytest-cov
# pytest-mock daje mocker fixture
# pytest-cov meri pokrivenost

# sa pip install pytest-mock pytest-cov

# Svi dalji testovi se pisu za biblioteka_servis iz src
# sa mockovima za spoljne servise(ovo je samo demo nemamo pravi npr. email servis)

import pytest
# MagicMock je lazni objekat koji prima bilo koji poziv!
from unittest.mock import MagicMock,call
from src.biblioteka_servis import BibliotekaServis,EmailServis,IzvestajServis,Knjiga

# Primer problema koji mock resava:
# Npr. BibliotekaServis klasa salje email svaki put kada se knjiga pozajmi
# i kako dalje testiramo funkciju za pozajmljivanje knjiga salju se emailovi i to nije dobro
# testiranje bez slanja pravog email-a se resava sa mock-om, samim tim dobijamo lazni email sercis koji ce se ponasati onako kako mi zelimo i nece slati prave emailove da spamuje

# osnovno testiranje bez mock-a
# metode koje ne koriste spoljne zavisnosti
def test_dodaj_knjigu(servis):
    knjiga_id=servis.dodaj_knjigu(
        Knjiga(naslov="Baze podataka",autor="Dr Snezana R. Popovic",godina=2024)
    )
    assert servis.broj_knjiga()==1
    assert isinstance(knjiga_id,int)