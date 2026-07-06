# Vezba mocking i coverage
import pytest
from unittest.mock import MagicMock
from src.prodavnica_servis import ProdavnicaServis, SmsServis, PlacanjeServis, Proizvod

# GRUPA 1 — Fixtures (sve pravite u conftest.py gde je dat i tekst zadataka)

# GRUPA 2 — Testiranje bez mocka(metode koje ne pozivaju spoljne servise)
# Zadatak 1 G2
# Napisati test koji proverava da dodaj_proizvod() vraca int ID.
# Koristiti fixture prodavnica.
def test_dodaj_proizvod(prodavnica):
    proizvod_id=prodavnica.dodaj_proizvod(
        Proizvod(naziv="Telefon",cena=85990.99,kolicina=2)
    )
    assert isinstance(proizvod_id,int)
    assert proizvod_id==1

# Zadatak 2 G2
# Napisati test koji proverava da dodaj_proizvod() sa praznim nazivom baca ValueError
def test_dodaj_proizvod_bez_naziva(prodavnica):
    with pytest.raises(ValueError):
        prodavnica.dodaj_proizvod(
            Proizvod(naziv="",cena=85990.99,kolicina=2)
        )

# Zadatak 3 G2
# Napisati test koji proverava da dodaj_proizvod() sa cenom 0 baca ValueError
def test_dodaj_proizvod_besplatan(prodavnica):
    with pytest.raises(ValueError):
        prodavnica.dodaj_proizvod(
            Proizvod(naziv="Telefon",cena=0,kolicina=2)
        )

# GRUPA 3 — Testiranje SMS-a pri kupovini
# Zadatak 1 G3
# Napisati test koji proverava da kupi() poziva SMS servis tacno jednom.
# Koristiti: prodavnica_sa_proizvodom i lazni_sms.
# VAZNO: lazno_placanje mora da vraca True (placanje uspeva)
# Postaviti return_value na laznom placanju pre poziva kupi().
#   lazno_placanje.naplati.return_value = True
def test_kupi_sms(prodavnica_sa_proizvodom,lazni_sms,lazno_placanje):
    prodavnica,proizvod_id=prodavnica_sa_proizvodom
    lazno_placanje.naplati.return_value=True
    
    prodavnica.kupi(
        proizvod_id=proizvod_id,
        kolicina=1,
        telefon="0651234567",
        kartica="1234-5678-9012-3456",
    )
    lazni_sms.posalji.assert_called_once()


# Zadatak 2 G3
# Napisati test koji proverava TACNE argumente SMS-a pri kupovini:
#telefon: "0641234567"
#poruka treba da sadrzi naziv proizvoda i ukupan iznos


# Zadatak 3 G3
# Napisati test koji proverava da kupi() smanjuje kolicinu na stanju.
# Ako je bilo 10, nakon kupovine 3 treba da bude 7.
# Koristiti dostupna_kolicina() za proveru.


# GRUPA 4 — Testiranje placanja
# Zadatak 1 G4
# Napisati test koji proverava da kupi() poziva placanje servis
# sa ispravnim iznosom
# Slusalice kostaju 3500, kupujemo 2,ocekujemo naplatu 7000.0

# Zadatak 2 G4
# Napisati test koji proverava da se SMS NE salje ako placanje ne uspe.
# Scenario:
#   lazno_placanje.naplati.return_value = False (placanje pada)
#   kupi() treba da baci ValueError
#   SMS NE sme biti poslat


#  GRUPA 5 — Testiranje vracanja proizvoda
# Zadatak 1 G5
# Napisati test koji proverava da vrati_proizvod() salje SMS
# Koristiti prodavnica_sa_proizvodom.


# Zadatak 2 G5
# Napisati test koji proverava da vrati_proizvod() uvecava kolicinu
# Pre vracanja kupi 3 komada, pa vrati 2.
# Na kraju treba biti: 10-3+2 = 9 komada


# GRUPA 6 — Error grane (za coverage)
# Zadatak 1 G6
# Napisati test koji proverava da kupi() sa nepostojecim ID-em baca KeyError.


# Zadatak 2 G6
# Napisati test koji proverava da kupi() baca ValueError kada je trazena
# kolicina veca od dostupne
# Primer: dostupno je 10, trazimo 20.


# Zadatak 3 G6
# Napisari test koji proverava da vrati_proizvod() sa nepostojecim ID-em baca KeyError



# Pokrenuti coverage i dostici iznad 90%
# dokumentovati izvestaj (ako je cli report u komentaru, ako je html on ce svakako biti tu)
# dodai i komande koje ste slali u cli
# ukoliko ima smisla, nakon izvestaja, pokriti i linije/funkcije/grane koje nisu
# pokrivene testovima