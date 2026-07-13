# Testiranje REST API-ja
# Unit + Integration (pravi HTTP pozivi!)
# API: https://api.restful-api.dev (javni, bez autentifikacije)
# Dva nacina testiranja:
#   1. UNIT testovi->mockujemo UredjajApiKlijent (brzo, bez interneta)
#   2. INTEGRATION->koristimo pravi klijent (sporo, treba internet)
# NAPOMENA: integration testovi prave PRAVE HTTP pozive ka restful-api.dev
#Limit je 50 zahteva dnevno na javnom API-ju!

import pytest
from unittest.mock import MagicMock
from src.servis import UredjajServis, UredjajApiKlijent, Uredjaj

# FIXTURES u conftest.py

# Zadatak 1
# Napraviti dva fixture-a:
# lazni_klijent-MagicMock(spec=UredjajApiKlijent)
# servis-UredjajServis(lazni_klijent)

# Zadatak 2
# Napraviti fixture "lista_uredjaja" - ovo je simuliran odgovor API-ja
# API vraca listu dict-ova ovog oblika:
# [
#   {"id": "1", "name": "Apple MacBook Pro 16",   "data": {"year": 2019, "price": 1849.99}},
#   {"id": "2", "name": "Apple iPhone 14",        "data": {"price": 999.0, "color": "crna"}},
#   {"id": "3", "name": "Samsung Galaxy S23",     "data": {"price": 799.0}},
#   {"id": "4", "name": "Sony WH-1000XM5",        "data": {"color": "crna"}},   ← nema price!
#   {"id": "5", "name": "Apple AirPods Pro",      "data": {"price": 249.0}},
# ]
# Koristiti: lazni_klijent.uzmi_sve.return_value = lista_uredjaja


# GRUPA 1 — smoke testovi
# Zadatak 3  @pytest.mark.smoke
# Napisati test koji proverava da svi_uredjaji() vraca listu Uredjaj objekata.
# Postaviti: lazni_klijent.uzmi_sve.return_value = lista_uredjaja
# Proveriti: len == 5 i da su svi instanca Uredjaj klase.


# Zadatak 4  @pytest.mark.smoke
# Napisati test koji proverava da dodaj() vraca Uredjaj.
# Postaviti: lazni_klijent.dodaj.return_value =
#   {"id": "99", "name": "Test uredjaj", "data": {"test": True}}
# Proveriti: isinstance(rezultat, Uredjaj) i naziv == "Test uredjaj"
