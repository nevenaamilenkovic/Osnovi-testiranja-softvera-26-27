import pytest
from src.prodavnica_servis import SmsServis,PlacanjeServis,ProdavnicaServis,Proizvod
from unittest.mock import MagicMock,call

# Zadatak 1 G1
# Napraviti tri fixture-a:
#   lazni_sms — MagicMock sa spec=SmsServis
#   lazno_placanje — MagicMock sa spec=PlacanjeServis
#   prodavnica — ProdavnicaServis koji koristi lazni_sms i lazno_placanje
@pytest.fixture()
def lazni_sms():
    return MagicMock(spec=SmsServis)

@pytest.fixture()
def lazno_placanje():
    return MagicMock(spec=PlacanjeServis)

@pytest.fixture()
def prodavnica(lazni_sms,lazno_placanje):
    # return ProdavnicaServis(lazni_sms,lazno_placanje)
    # citljivije je sa argumentima
    return ProdavnicaServis(
        sms_servis=lazni_sms,
        placanje_servis=lazno_placanje,
    )


# Zadatak 2 G1
# Napraviti fixture prodavnica_sa_proizvodom koja:
#- koristi fixture prodavnica
#- dodaje jedan proizvod: naziv="Slusalice", cena=3500.0, kolicina=10
#- vraca tuple (prodavnica, proizvod_id)
@pytest.fixture()
def prodavnica_sa_proizvodom(prodavnica):
    proizvod_id=prodavnica.dodaj_proizvod(
        Proizvod(naziv="Slusalice",cena=3500.0,kolicina=10)
    )
    return prodavnica,proizvod_id
