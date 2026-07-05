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
# metode koje ne koriste spoljne zavisnosti!
def test_dodaj_knjigu(servis):
    knjiga_id=servis.dodaj_knjigu(
        Knjiga(naslov="Baze podataka",autor="Dr Snezana R. Popovic",godina=2024)
    )
    assert servis.broj_knjiga()==1
    assert isinstance(knjiga_id,int)

def test_dodaj_knjigu_bez_naslova(servis):
    with pytest.raises(ValueError):
        servis.dodaj_knjigu(
            Knjiga(naslov="",autor="Dr Snezana R. Popovic",godina=2024)
        )


#testiranje sa mock-om
# provera da li su spoljni servisi pozvani ispravno
def test_pozajmi_salje_email(servis_sa_knjigom,lazni_email):
    servis,knjiga_id=servis_sa_knjigom
    # act
    servis.pozajmi(knjiga_id,"nevena@test.com")
    # assert provera da li je email poslat, ne da li je stigao
    lazni_email.posalji.assert_called_once()
    # assert_called_once() proverava da li je metoda pozvana tacno jednom
    # nije bitno sa kojim argumentima
    # u ovom slucaju prolazi ako je posalji() pozvana jednom sa bilo kojim argumentima
    # pada ako nije pozvana ili je pozvana vise puta
    # koristi se kada nas zanima SAMO DA LI SE NESTO DESILO, A NE KAKO!

def test_pozajmi_salje_email_pravom_korisniku(servis_sa_knjigom,lazni_email):
    servis,knjiga_id=servis_sa_knjigom
    servis.pozajmi(knjiga_id,"nevena@test.com")

    # provera tacnih argumenara sa kojima je email pozvan
    lazni_email.posalji.assert_called_once_with(
        na="nevena@test.com",
        naslov="Knjiga pozajmljena",
        poruka='Pozajmili ste knjigu "Baze podataka"'
    )
    # assert_called_once_with() proverava i da je pozvana jednom i sa tacno tim argumentima
    # u ovom slucaju ako je metoda posalji() pozvana sa pogresnim emailom ili sa pogresnom porukom test pada
    # ovo je dosta strozije i preciznije od assert_called_once()

def test_pozajmi_menja_dostupnost(servis_sa_knjigom):
    servis,knjiga_id=servis_sa_knjigom
    servis.pozajmi(knjiga_id,"nevena@test.com")
    assert servis.broj_dostupnih()==0

def test_vrati_salje_email(servis_sa_knjigom,lazni_email):
    servis,knjiga_id=servis_sa_knjigom
    servis.pozajmi(knjiga_id,"nevena@test.com")

    # reset servisa, da se ignorise poziv iz pozajmi
    lazni_email.reset_mock()

    servis.vrati(knjiga_id,"nevena@test.com")

    # provera da li je email poslat i za vracanje
    lazni_email.posalji.assert_called_once_with(
        na="nevena@test.com",
        naslov="Knjiga vracena",
        poruka='Uspesno ste vratili knjigu "Baze podataka"'
    )


def test_email_se_ne_salje_ako_knjiga_nije_dostupna(servis_sa_knjigom,lazni_email):
    servis,knjiga_id=servis_sa_knjigom
    servis.pozajmi(knjiga_id,"nevena@test.com")
    lazni_email.reset_mock()

    # pokusaj ponovnog pozajmljivanja iste knjige treba da baci valueerror i email ne sme biti poslan
    with pytest.raises(ValueError):
        servis.pozajmi(knjiga_id,"nevena@test.com")
    lazni_email.posalji.assert_not_called()
    # assert_not_called() poverava da metoda nije pozvana ni jednom koristi se kada treba da se osigura da se nesto nije desilo
    # u ovom slucaju email ne sme da se posalje ako je knjiga nedostupna

# ukratko
# assert_called_once() proverava da je mock pozvan tacno jednom bez obzira na argumente
# assert_called_once_with(...) proverava i da je mock pozvan jednom i tacno sa tim argumentima
# assert_not_called() proverava da mock NIJE pozvan, vazno za test gde ne sme da se desi nesto
# reset_mock() brise pamcenje mock-a, koristi se kada se isti mock koriti u vise faza testa


# Mockovanje fajl sistema

def test_generisi_izvestaj_cuva_fajl(servis_sa_knjigom,lazni_izvestaj):
    servis,knjiga_id=servis_sa_knjigom
    servis.generisi_izvestaj("izvestaj.txt")
    # provera da je fajl servis pozvan sa ispravnom putanjom
    lazni_izvestaj.sacuvaj_izvestaj.assert_called_once()
    pozvan_sa=lazni_izvestaj.sacuvaj_izvestaj.call_args#call args izvlaci argumente iz poziva
    assert pozvan_sa[0][0] == "izvestaj.txt"#prvi pozicioni argument

def test_generisi_izvestaj_vraca_sadrzaj(servis_sa_knjigom):
    servis,knjiga_id=servis_sa_knjigom
    sadrzaj=servis.generisi_izvestaj("izvestaj.txt")
    # sadrzaj treba da sadrzi naziv knjige
    assert "Baze podataka" in sadrzaj




# pokretanje
# pytest -v --cov=biblioteka_servis --cov-report=html
# pytest -v --cov=biblioteka_servis