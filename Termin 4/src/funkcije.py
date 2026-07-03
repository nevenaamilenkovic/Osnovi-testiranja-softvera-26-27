# funkcija 1
# Vraca kategoriju na osnovu godina
# Baca TypeError ako godine nisu int
# Baca ValueError ako su godine < 0 ili > 150
# Kategorije:
# 0  - 17  -> "maloletnik"
# 18 - 64  -> "odrasla osoba"
# 65 - 150 -> "senior"
def kategorija_godina(godine: int) -> str:
    # ZA DEMO ZA XPASS FIXED BUG za scenario 2 u test_markeri.py
    if isinstance(godine, bool):
        raise TypeError("bool nije dozvoljen, ocekivan int")
    if not isinstance(godine, int):
        raise TypeError(f"Ocekivan int, dobijen {type(godine).__name__}")
    if godine < 0:
        raise ValueError("Godine ne mogu biti negativne")
    if godine > 150:
        raise ValueError("Godine ne mogu biti vece od 150")
    if godine < 18:
        return "maloletnik"
    if godine < 65:
        return "odrasla osoba"
    return "senior"

# funkcija 2
# Pretvara broj (1-10) u rec na srpskom
# Baca TypeError ako broj nije int
# Baca ValueError ako je broj van opsega 1-10
def broj_u_rec(broj: int) -> str:
    if not isinstance(broj, int):
        raise TypeError(f"Ocekivan int, dobijen {type(broj).__name__}")
    if broj < 1 or broj > 10:
        raise ValueError(f"Broj mora biti izmedju 1 i 10, dobijeno: {broj}")
    brojevi = {
        1: "jedan", 2: "dva",    3: "tri",
        4: "cetiri", 5: "pet",   6: "sest",
        7: "sedam",  8: "osam",  9: "devet", 10: "deset"
    }
    return brojevi[broj]

# funkcija 3
# Pretvara brojcanu ocenu (1-5) u rec
# Baca ValueError za ocene van opsega
# Ocene:
# 1 -> "nedovoljan"
# 2 -> "dovoljan"
# 3 -> "dobar"
# 4 -> "vrlodobar"
# 5 -> "odlican"
def ocena_u_rec(ocena: int) -> str:
    if not isinstance(ocena, int):
        raise TypeError(f"Ocekivan int, dobijen {type(ocena).__name__}")
    if ocena < 1 or ocena > 5:
        raise ValueError(f"Ocena mora biti izmedju 1 i 5, dobijeno: {ocena}")
    ocene = {1: "nedovoljan", 2: "dovoljan", 3: "dobar", 4: "vrlodobar", 5: "odlican"}
    return ocene[ocena]


# funkcija 4
# Racuna cenu sa popustom na osnovu godina korisnika
# Baca ValueError ako je cena negativna ili godine van opsega 0-120
# Popusti:
# 0  - 17  -> 20% popusta (deca)
# 18 - 64  -> bez popusta
# 65 - 120 -> 30% popusta (penzioneri)
def popust_po_godinama(godine: int, cena: float) -> float:
    if cena < 0:
        raise ValueError("Cena ne moze biti negativna")
    if godine < 0 or godine > 120:
        raise ValueError(f"Godine moraju biti izmedju 0 i 120, dobijeno: {godine}")
    if godine < 18:
        return round(cena * 0.80, 2)
    if godine < 65:
        return round(cena, 2)
    return round(cena * 0.70, 2)


# funkcija 5
# Proverava da li je username validan
# Pravila:
# - mora biti string
# - duzina 3-20 karaktera
# - samo slova, brojevi i donja crta (_)
# - ne sme pocinjati brojem
# Vraca True ako je validan, False ako nije
# Baca TypeError ako username nije string
def validan_username(username: str) -> bool:
    if not isinstance(username, str):
        raise TypeError(f"Ocekivan string, dobijen {type(username).__name__}")
    if len(username) < 3 or len(username) > 20:
        return False
    if username[0].isdigit():
        return False
    return all(c.isalnum() or c == "_" for c in username)
