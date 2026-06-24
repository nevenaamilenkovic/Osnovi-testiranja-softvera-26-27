# GRUPA 1 — Knjiga dataclass
# Fixture nije potreban — testira se samo objekat u izolaciji
from src.biblioteka import Knjiga
# Zadatak 1
# Napisati test koji proverava da Knjiga kreirana sa svim argumentima
# ima ispravne vrednosti svih polja, i da je podrazumevano dostupna=True.
def test_knjiga():
    # arrange
    knjiga=Knjiga(naslov="Proces",autor="Dostojevski",godina=1970)
    # act, assert
    assert knjiga.naslov=="Proces"
    assert knjiga.autor=="Dostojevski"
    assert knjiga.godina==1970
    assert knjiga.dostupna
    assert knjiga.id==None

# Zadatak 2
# Napisati test koji proverava da dve Knjige sa istim podacima
# (isti naslov, autor, godina, dostupna) ali razlicitim ID-jem
# JESU jednake. (pogledajte kako je id definisan u dataclass-u)
def test_dve_knjige_razlicit_id():
    k1=Knjiga(naslov="Proces",autor="Dostojevski",godina=1970,id=1)
    k2=Knjiga(naslov="Proces",autor="Dostojevski",godina=1970,id=2)
    # id se ne poredi!!
    assert k1==k2

# Zadatak 3
# Napisati test koji proverava da dve Knjige sa razlicitim dostupna
# vrednostima (jedna True, druga False) NISU jednake.
def test_dve_knjige_razlicita_dostupnost():
    k1=Knjiga(naslov="Proces",autor="Dostojevski",godina=1970,dostupna=True)
    k2=Knjiga(naslov="Proces",autor="Dostojevski",godina=1970,dostupna=False)
    # id se ne poredi!!
    assert k1!=k2

# GRUPA 2 — Osnovna upotreba biblioteke
# Koristiti fixture: prazna_biblioteka, biblioteka_sa_knjigama
# fixtures su u conftest.py

# Zadatak 4
# Napisati test koji proverava da prazna biblioteka ima 0 knjiga.
def test_prazna_biblioteka(prazna_biblioteka):
    assert prazna_biblioteka.broj_knjiga()==0

# Zadatak 5
# Napisati test koji proverava da nakon dodavanja knjige u praznu biblioteku,
# broj_knjiga() vraca 1 i ta knjiga se moze pronaci pomocu uzmi_knjigu().
def test_prazna_biblioteka_dodate_knjige(prazna_biblioteka):
    knjiga_id=prazna_biblioteka.dodaj_knjigu(Knjiga(naslov="Test knjiga",autor="Test autor",godina=2026))
    assert prazna_biblioteka.broj_knjiga()==1
    assert prazna_biblioteka.uzmi_knjigu(knjiga_id).naslov=="Test knjiga"
    assert prazna_biblioteka.uzmi_knjigu(knjiga_id).autor=="Test autor"
    assert prazna_biblioteka.uzmi_knjigu(knjiga_id).godina==2026


# Zadatak 6
# Napisati test koji proverava da biblioteka_sa_knjigama ima tacno 3 knjige
# i da su sve 3 dostupne (broj_dostupnih() == 3).
def test_biblioteka_sa_knjigama(biblioteka_sa_knjigama):
    assert biblioteka_sa_knjigama.broj_knjiga()==3
    assert biblioteka_sa_knjigama.broj_dostupnih()==3

# Zadatak 7
# Napisati test koji proverava da trazi_po_autoru("Dostojevski")
# vraca tacno 2 knjige iz biblioteka_sa_knjigama.


# GRUPA 3 — Pozajmljivanje i vracanje knjiga
# Koristiti fixture: biblioteka_sa_knjigama, biblioteka_sa_pozajmljenom

# Zadatak 8
# Napisati test koji proverava kompletan ciklus pozajmljivanja:
#   1. Pozajmi prvu knjigu
#   2. Proveri da knjiga vise nije dostupna
#   3. Proveri da broj_dostupnih() opao za 1 (sa 4 na 3)


# Zadatak 9
# Napisati test koji proverava kompletan ciklus vracanja:
# Koristiti biblioteka_sa_pozajmljenom (knjiga je vec pozajmljena).
#   1. Vrati tu pozajmljenu knjigu
#   2. Proveri da je knjiga ponovo dostupna
#   3. Proveri da je broj_dostupnih() ponovo 4


# Zadatak 10
# Napisati test koji proverava da pozajmi() baca ValueError
# kada pokusate da pozajmite knjigu koja je vec pozajmljena.
# Proveri i da poruka greske sadrzi naslov te knjige.
# Koristi biblioteka_sa_pozajmljenom.


# GRUPA 4 — Greske i izuzeci

# Zadatak 11
# Napisati test koji proverava da vrati() baca ValueError
# kada pokusas da vratis knjigu koja nije bila pozajmljena.


# Zadatak 12
# Napisati test koji proverava da uzmi_knjigu() baca KeyError
# za nepostojeci ID, i da poruka sadrzi taj ID.


# Zadatak 13
# Napisati test koji proverava da dodaj_knjigu() baca ValueError
# kada knjiga nema naslov (prazan string "").


# GRUPA 5 — Klase i scope

# Zadatak 14
# Grupisati zadatke 8 i 9 u klasu TestPozajmljivanje.
# Svaki test treba da bude nezavistan — koristi function scope fixture
# (biblioteka_sa_knjigama) tako da svaki test pocinje sa svezom bibliotekom.


# Zadatak 15
# Napraviti klasu TestPozajmljivanjeScope sa scope="class" fixture-om.
# Napisati 3 testa koji se izvrsavaju sekvencijalno:
#   test 1: pozajmi prvu knjigu, proveri da nije dostupna
#   test 2: pokusaj da pozajmis istu knjigu ponovo — ocekuj ValueError
#   test 3: vrati knjigu, proveri da je ponovo dostupna
