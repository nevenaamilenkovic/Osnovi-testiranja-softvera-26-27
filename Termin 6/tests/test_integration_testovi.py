# Integration/Integracioni testovi

# Do sada su pisani jedinicni(unit) testovi, gde je svaka klasa testirana izolovano,
# a sve spoljne zavisnosti su zamenjene mock-ovima
# Mock garantuje da kod test metode poziva pravu metodu, ali ne garantuje da ce prava
# implementacija ispravno reagovati

# Unit test: BibliotekaServis <-> MagicMock(IzvestajServis), brzo i izolovano
# Integration test: BibliotekaServis <-> (pravi)IzvestajServis, testira pravu saradnju

# test piramida:
#       e2e             redje se pisu, sporo i skupo
#    integration        umereno
#  jedinicni testovi    najvise se pisu/koriste, brzi i izolovani

# Unit testira jednu klasu/funkciju sve ostalo je mock
# Integration testira saradnju izmedju slojeva, bez mockova za interne komponente
# E2E(end to end) testira ceo sistem s kraja na kraj (UI,API,DB-sve zajedno)

import pytest
from src.biblioteka_servis import EmailServis,IzvestajServis,BibliotekaServis,Knjiga
# razlika u kodu
# UNIT TEST -> MOCK ZA SVE SPOLJNE ZAVISNOSTI
def test_unit(unit_servis,lazni_izvestaj):
    unit_servis.generisi_izvestaj("izvestaj.txt")
    lazni_izvestaj.sacuvaj_izvestaj.assert_called_once()
# provervamo samo da li je servis pozvan a ne sta je zaista upisano u fajl!

# INTEGRATION TEST -> PRAVI OBJEKTI, PRAVI FAJLOVI
def test_integration():
    pass