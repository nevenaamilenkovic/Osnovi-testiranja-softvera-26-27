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


from unittest.mock import MagicMock
# INTEGRATION TEST -> PRAVI OBJEKTI, PRAVI FAJLOVI
def test_integration(tmp_path):
# tmp_path je pytest ugradjeni fixture za fajlove, daje privremeni folder, sto ga #cini savrsenim za integration testove koji pisu fajlove!!
# fajlovi su na putanji
# C:\Users\<ime_racunara>\AppData\Local\Temp\pytest-of-<ime>\pytest-<broj>\test_naziv0\
# ako treba da vidimo putanju do fajla dok test traje pokrecemo sa -s i u test dodajemo print(tmp_path)
    pravi_izvestaj=IzvestajServis()
    # email je i dalje mock, ne mozemo slati prave mejlove tj nema ni potrebe sada
    pravi_email=MagicMock(spec=EmailServis)
    servis=BibliotekaServis(pravi_email,pravi_izvestaj)

    servis.dodaj_knjigu(Knjiga("Python","Barry",2022))
    putanja=tmp_path/"izvestaj.txt"
    sadrzaj=servis.generisi_izvestaj(str(putanja))
    # print(tmp_path)
    assert putanja.exists()#provera da li je fajl zaista napravljen
    assert "Python" in putanja.read_text()#provera da li je sadrzaj zaista upisan u fajl

#ne treba @pytest.fixture() jer pytest automatski ubrizgava kada se tmp_path
# doda u parametre
def test_primer_tmp(tmp_path):
    putanja=tmp_path/"moj_fajl.txt"#path objekat!!!
    putanja.write_text("test sadrzaj")
    assert putanja.read_text()=="test sadrzaj"

# Mockovanje po vrsti testa
"""
komponenta                              Unit        Integration
----------------------------------------------------------------
Interne klase(servis,repozitorijum)     mock        pravi objekat
Fajl sistem                             mock        pravi fajl(tmp_path)
Email/SMS                               mock        mock(i dalje)
Placanje/banka                          mock        mock(i dalje)
Baza podataka                           mock        ponekad pravi(test DB)
"""
# u sustini spoljni servisi koji kostaju ili salju stvarne poruke i slicno se uvek mockuju bez obzira na vrstu testa


#Osnovna integracija - dodavanje i citanje
def test_dodaj_i_prebroj_knjige(servis):
    # integration test u kome dodaj_knjigu zapravo dodaje knjigu a broj_knjiga zapravo broji
    # arrange
    knjiga=Knjiga("Baze podataka","Snezana Popovic",2024)
    # act
    servis.dodaj_knjigu(knjiga)
    # assert
    assert servis.broj_knjiga()==1
    assert servis.broj_dostupnih()==1

def test_dodaj_vise_knjiga(servis):
    # vise knjiga radi provere da li brojac knjiga radi ispravno
    servis.dodaj_knjigu(Knjiga("Knjiga A", "Autor A", 2020))
    servis.dodaj_knjigu(Knjiga("Knjiga B", "Autor B", 2021))
    servis.dodaj_knjigu(Knjiga("Knjiga C", "Autor C", 2022))
    
    assert servis.broj_knjiga()==3
    assert servis.broj_dostupnih()==3


# integracija pozajmljivanja i vracanja knjiga
def test_pozajmi_menja_dostupnost(servis_sa_knjigama):
    # pozajmi() zzapravo menja stanje knjige, ne poziva mock!!!
    servis_sa_knjigama.pozajmi(1,"nevena@test.com")
    # 3 knjige ukupno, jedna pozajmljena, a dve dostupne
    assert servis_sa_knjigama.broj_knjiga()==3
    assert servis_sa_knjigama.broj_dostupnih()==2

def test_pozajmi_pa_vrati(servis_sa_knjigama):
    # kompletan ciklus pozajmljivanja i vracanja
    # provera dostupnosti pre i nakon vracanja
    servis_sa_knjigama.pozajmi(1,"nevena@test.com")
    assert servis_sa_knjigama.broj_dostupnih()==2
    
    servis_sa_knjigama.vrati(1,"nevena@test.com")
    assert servis_sa_knjigama.broj_dostupnih()==3

def test_pozajmljivanje_iste_knjige(servis_sa_knjigama):
    # nije moguce pozajmiti knjigu dva puta
    # provera da servis cuva stanje pozajmica
    servis_sa_knjigama.pozajmi(1,"nevena@test.com")
    with pytest.raises(ValueError):
        servis_sa_knjigama.pozajmi(1,"maci@test.com")


# integracioni sa fajl sistemom
def test_generisi_izvestaj_pravi_fajl(servis_sa_knjigama,tmp_path):
    putanja=tmp_path/"izvestaj.txt"
    servis_sa_knjigama.generisi_izvestaj(str(putanja))
    assert putanja.exists()#provera da li fajl zapravo postoji

def test_generisi_izvestaj_sadrzaj(servis_sa_knjigama,tmp_path):
    putanja=tmp_path/"izvestaj.txt"
    servis_sa_knjigama.generisi_izvestaj(str(putanja))
    sadrzaj=putanja.read_text()
    assert "Python bez oklevanja" in sadrzaj
    assert "Baze podataka" in sadrzaj
    assert "Go bez oklevanja" in sadrzaj

def test_generisi_izvestaj_status_knjige(servis_sa_knjigama,tmp_path):
    # pozajmi prvu knjigu
    servis_sa_knjigama.pozajmi(1,"nevena@test.com")
    # napravi izvestaj
    putanja=tmp_path/"izvestaj.txt"
    servis_sa_knjigama.generisi_izvestaj(str(putanja))
    # procitaj izvestaj
    sadrzaj=putanja.read_text()
    # provera da je knjiga 1 pozajmljena
    assert "pozajmljena" in sadrzaj
    # knjige 2 i 3 treba da budu dostupne
    assert "dostupna" in sadrzaj


# integracioni email+stanje kombinovano
def test_email_se_salje_pri_pozajmljivanju(servis_sa_knjigama,lazni_email):
    # kombinovani test
    # pravi servis, pravi izvestaj, mock email
    servis_sa_knjigama.pozajmi(1,"nevena@test.com")
    assert servis_sa_knjigama.broj_dostupnih()==2
    lazni_email.posalji.assert_called_once()
