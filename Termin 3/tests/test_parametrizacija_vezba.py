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


# Ocene: 1-nedovoljan, 2-dovoljan, 3-dobar, 4-vrlodobar, 5-odlican
# Zadatak 4
# Napisite parametrizovan test koji proverava SVE validne ocene (1-5)
# i njihove odgovarajuce tekstove.


# Zadatak 5
# Napisite parametrizovan test koji proverava da ocene van opsega
# bacaju ValueError: 0, 6, -1, 100


# popust_po_godinama()
# Deca (0-17): 20% popusta, Odrasli (18-64): bez popusta, Penzioneri (65-120): 30%
# Zadatak 6
# Napisite parametrizovan test sa tri parametra: godine, cena, ocekivana_cena
# Pokrijte sve tri kategorije i granicne vrednosti.
# Primer jednog slucaja: (10, 100.0, 80.0) — dete, cena 100, sa popustom 80
# Napisite najmanje 6 test slucajeva.


# Zadatak 7
# Napisite parametrizovan test koji proverava greske:
# negativna cena baca ValueError
# godine van opsega (npr. -1, 121) bacaju ValueError


# Zadatak 8
# Napisitee parametrizovan test za VALIDNE username-ove koji vraca True.
# Pokrijte: normalan username, sa brojevima, sa donjom crtom,
# minimalna duzina (3), maksimalna duzina (20 karaktera).


# Zadatak 9
# Napisite parametrizovan test za NEVALIDNE username-ove koji vraca False.
# Pokrijte: prekratak (2 slova), predugacak (21 slovo),
# pocinje brojem, sadrzi specijalan karakter (@, -, razmak).


# Zadatak 10
# Napisite parametrizovan test koji proverava TypeError
# kada username nije string: 123, 3.14, None, ["lista"]
# Zatim ga kombinujte sa Zadatkom 9 u jednu klasu TestValidanUsername
# koja ima oba testa kao metode.
