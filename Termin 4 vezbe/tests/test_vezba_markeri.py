import pytest
from src.biblioteka import Biblioteka,Knjiga

# fixtures su u conftest.py


# GRUPA 1 - smoke testovi
# najosnovniji testovi, da li app uopste radi
# ako smoke testovi padnu nema smisla pisati ostale ili pokretati

# Zadatak 1 G1
# Markirati test sa smoke
# Napisati test koj proverava da se Biblioteka moze kreirati sa zadatim nazivom
@pytest.mark.smoke
def test_biblioteka_create():
    b=Biblioteka(naziv="Test 1")
    assert b.naziv=="Test 1"

# Zadatak 2 G1
# Markirati test sa smoke
# Napisati test koji proverava da se Knjiga moze dodati u biblioteku i da broj_knjiga() vraca 1 
@pytest.mark.smoke
def test_knjiga_add(prazna_biblioteka):
    prazna_biblioteka.dodaj_knjigu(Knjiga(naslov="Test knjiga",autor="Test autor",godina=2026))
    assert prazna_biblioteka.broj_knjiga() == 1

# Zadatak 3 G1
# Markirati test sa smoke
# Napisati test koji proverava da pozajmi() i vrati() rade osnovni ciklus bez gresaka
@pytest.mark.smoke
def test_pozajmi_vrati_init(popunjena_biblioteka):
    knjiga_id=popunjena_biblioteka.sve_knjige()[0].id
    popunjena_biblioteka.pozajmi(knjiga_id)
    assert popunjena_biblioteka.broj_dostupnih()==2
    popunjena_biblioteka.vrati(knjiga_id)
    assert popunjena_biblioteka.broj_dostupnih()==3

# ---------------------------------------------------------------------------

# GRUPA 2 - regression testovi
# testovi koji proveravaju da popravljeni bugovi nisu vratili

# Zadatak 1 G2
# Markirati test sa regression
# Bug #1: funkcija trazi_po_autoru() nije radila case-insensitive pretragu
# Napisati test koji proverava da "dostojevski"(sve malim slovima) pronalazi Dostojevskog tj knjigu Zlocin i kazna Fjodor Dostojevski 1866
@pytest.mark.regression
def test_trazi_po_autoru_case_insensitive(popunjena_biblioteka):
    rezultat=popunjena_biblioteka.trazi_po_autoru("dostojevski")
    pass


# Zadatak 2 G2
# Markirati test sa regression
# Bug #2: funkcija dodaj_knjigu() nije bacala ValueError na prazno ime autora
# Napisati test koji proverava da "" kao autor baca ValueError

# ---------------------------------------------------------------------------

# GRUPA 3 - skip i skipif

# Zadatak 1 G3
# Markirati test sa skip i razlogom: funkcija rezervisi() jos nije implementirana
# Napisati test koji poziva nepostojecu metodu biblioteka.rezervisi(1)
# test treba da bude preskocen, a ne da padne!

# Zadatak 2 G3
# Markirati test sa skipif
# potrebno je preskociti test ako je Python verzija manja od 3.14
# (uvezite sys biblioteku i koristite sys.version_info)
# sam test neka proverava bilo sta jednostavno, bitna je skipif logika

# ---------------------------------------------------------------------------


# GRUPA 4 - xfail

# Zadatak 1 G4
# Postoji poznat bug: dodaj_knjigu() ne proverava da li je godina
# negativna (npr. -500) — treba da baci ValueError ali ne baca
# Markirati test sa xfail i odgovarajucim razlogom
# Napisati test koji ocekuje ValueError za negativnu godinu
# (test ce biti xfail jer bug postoji)

# Zadatak 2 G4
# isti test kao u zadatku 1 G4, ali sa argumentom strict=True
# pokrenuti oba zajedno i uporediti output

# ---------------------------------------------------------------------------


# GRUPA 5 - vise markera i parametrizacija

# Zadatak 1 G5
# Markirati test sa smoke i regression(oba!!)
# napisati parametrizovani test koji proverava da si sve knjige u popunjenoj
# biblioteci inicijalno dostupne
# fixture vraca biblioteku sa 3 knjige
# parametrizovati sa [0,1,2] kao indeksima

# Zadatak 2 G5
# Markirati test sa spor
# test treba da simulira sporiji scenario,
# dodati 100 knjiga u petlji i proveriti da funkcija broj_knjiga() vraca 100
# test nije zaista spor, ali demonstrira upotrebu markera za testove koji bi
# u realnosti bili spori, npr bulk operacije
# pokrenuti sve testove koji imaju marker spor i dodati komentar u kodu
# i pokrenuti sve testove koji nemaju marker spor, takodje dokumentovati