# testiraju se funkcije iz funkcije.py
import pytest
from src.funkcije import kategorija_godina
# Kategorije: 0-17 "maloletnik", 18-64 "odrasla osoba", 65-150 "senior"
# Zadatak 1
# Napisite parametrizovan test za VALIDNE vrednosti.
# Obavezno pokrijte sve granicne vrednosti:
#   0, 17, 18, 64, 65, 150
# i po jednu vrednost iz sredine svake kategorije.
@pytest.mark.parametrize("godine,kategorija",[
    (0,"maloletnik"),
    (17,"maloletnik"),
    (18,"odrasla osoba"),
    (64,"odrasla osoba"),
    (65,"senior"),
    (150,"senior"),
])
def test_kategorije_validne(godine,kategorija):
    assert kategorija_godina(godine)==kategorija

# Zadatak 2
# Napisite parametrizovan test za NEVALIDNE vrednosti koje bacaju ValueError:
#   -1, 151, -100, 200
# Hint: sve treba da bacaju ValueError tj. tip greske je isti za sve
@pytest.mark.parametrize("godine,greska",[
    (-1,ValueError),
    (151,ValueError),
    (-100,ValueError),
    (200,ValueError),
])
def test_kategorije_nevalidne(godine,greska):
    with pytest.raises(greska):
        kategorija_godina(godine)

# Zadatak 3
# Napisite parametrizovan test za NEVALIDNE tipove koji bacaju TypeError:
# "dvadeset", 3.5, None, True
# Hint: True je bool, a bool je podklasa int u Pythonu
# da li kategorija_godina(True) baca TypeError ili ne? Probajtee!
@pytest.mark.parametrize("godine,greska",[
    ("dvadeset",TypeError),
    (3.5,TypeError),
    (None,TypeError),
    (True,TypeError),
])
def test_kategorije_losi_tipovi(godine,greska):
    with pytest.raises(greska):
        kategorija_godina(godine)

# Ocene: 1-nedovoljan, 2-dovoljan, 3-dobar, 4-vrlodobar, 5-odlican
# Zadatak 4
# Napisite parametrizovan test koji proverava SVE validne ocene (1-5)
# i njihove odgovarajuce tekstove.
from src.funkcije import ocena_u_rec
@pytest.mark.parametrize("ocena,znacenje",[
    (1,"nedovoljan"),
    (2,"dovoljan"),
    (3,"dobar"),
    (4,"vrlodobar"),
    (5,"odlican"),
])
def test_ocene_validne(ocena,znacenje):
    assert ocena_u_rec(ocena)==znacenje

# Zadatak 5
# Napisite parametrizovan test koji proverava da ocene van opsega
# bacaju ValueError: 0, 6, -1, 100
@pytest.mark.parametrize("ocena,greska",[
    (0,ValueError),
    (6,ValueError),
    (-1,ValueError),
    (100,ValueError),
])
def test_ocene_van_opsega(ocena,greska):
    with pytest.raises(greska):
        ocena_u_rec(ocena)

# popust_po_godinama()
# Deca (0-17): 20% popusta, Odrasli (18-64): bez popusta, Penzioneri (65-120): 30%
# Zadatak 6
# Napisite parametrizovan test sa tri parametra: godine, cena, ocekivana_cena
# Pokrijte sve tri kategorije i granicne vrednosti.
# Primer jednog slucaja: (10, 100.0, 80.0) — dete, cena 100, sa popustom 80
# Napisite najmanje 6 test slucajeva.
from src.funkcije import popust_po_godinama
@pytest.mark.parametrize("godine,cena,cena_sa_popustom",[
    (0,100.0,80.0),
    (17,100.0,80.0),
    (18,100.0,100.0),
    (64,100.0,100.0),
    (65,100.0,70.0),
    (120,100.0,70.0),
])
def test_popust_validno(godine,cena,cena_sa_popustom):
    assert popust_po_godinama(godine,cena)==cena_sa_popustom



# Zadatak 7
# Napisite parametrizovan test koji proverava greske:
# negativna cena baca ValueError
# godine van opsega (npr. -1, 121) bacaju ValueError
@pytest.mark.parametrize("godine,cena,greska",[
    (-1,100.0,ValueError),
    (121,100,ValueError),
    (18,-100.0,ValueError),
    # (16,0.0,ValueError), ovde nece da baci valueeroor svakako nije negativna cena 0.00

])
def test_popust_nevalidno(godine,cena,greska):
    with pytest.raises(greska):
        popust_po_godinama(godine,cena)

# Zadatak 8
# Napisitee parametrizovan test za VALIDNE username-ove koji vraca True.
# Pokrijte: normalan username, sa brojevima, sa donjom crtom,
# minimalna duzina (3), maksimalna duzina (20 karaktera).
from src.funkcije import validan_username
@pytest.mark.parametrize("username,vrednost",[
    ("str",True),#minimalna duzina
    ("nevenamilenkovicraf1",True),#maksimalna duzina
    ("ynevenay",True),#normalan username
    ("nmilenkovic1121s",True),#sa brojevima
    ("nevena_milenkovic",True),#sa donjom crtom
])
def test_username_validan(username,vrednost):
    assert validan_username(username)==vrednost

# Zadatak 9
# Napisite parametrizovan test za NEVALIDNE username-ove koji vraca False.
# Pokrijte: prekratak (2 slova), predugacak (21 slovo),
# pocinje brojem, sadrzi specijalan karakter (@, -, razmak).
@pytest.mark.parametrize("username,vrednost",[
    ("nm",False),#prekratak
    ("nevenamilenkovicraf12",False),#predugacak
    ("1ynevenay",False),#pocinje brojem
    ("nmilenkovic1121s@",False),#specijalan katakter @
    ("nevena milenkovic",False),#razmak
    ("nevena-milenkovic",False),#crta
])
def test_username_nevalidan(username,vrednost):
    assert validan_username(username)==vrednost

# Zadatak 10
# Napisite parametrizovan test koji proverava TypeError
# kada username nije string: 123, 3.14, None, ["lista"]
# Zatim ga kombinujte sa Zadatkom 9 u jednu klasu TestValidanUsername
# koja ima oba testa kao metode.
