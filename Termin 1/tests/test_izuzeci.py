# kada se pise kod obicno dve stvari mogu poci naopako
# 1. exception/izuzetak->python baci gresku, program stane i dobijemo neki izuzetak npr. KeyError, TypeError,ValueError,ZeroDivisionError itd...
# 2. pogresna vrednost->program NE PADA! ali vaca pogresan rezulat, testira se "normalnim assertom" kao sto je bilo na pocetku, tj proveravaju se ocekivane vrrednosti

# Testiranje na greske je jako vazno jer greska koja se desi na pogresnom mestu je bug. Ako neka funkcija TREBA da baci ValueError kada npr dobije negativan broj a NE baci nista->to je problem, i to se treba proveriti i uhvatiti testom!
"""
sintaksa
obavezno: import pytest
with pytest.raises(TipGreske):
    kod_koji_treba_da_padne
"""
# with blok bukvano kaze pytestu ocekujem exception ovde
# ako se exception dogodi test prolazi
# ako se ne dogodi test pada
# ako se baci neki drugi tip exceptiona test opet pada

# takodje mozete biti i precizniji kada proverabate tip greske!
"""
npr.
with pytest.raises(ValueError,match="mora biti pozitivan"):
    neka_funkcija(-5)
match prima regex, u ovom slucaju ako poruka sadrzi BAS TAJ TEKST test prolazi!!
"""

# mozete sacuvati i exception obj za dalju inspekciju
"""
primer
with pytest.raises(KeyError) as exc_info:
    baza.uzmi(999)
assert "999" in str(exc_info.value)
exc_info.value je sam exception objekat! moze da se ispituje poruka,atributi ili tip
"""

# jedna od cescih gresaka je pogresan redosled
# assert van bloka with, samim tim se exception nikada NE HVATA!
"""
npr.
with pytest.raises(ValueError):
    x=5
assert neka_funkcija(-1) #ovo se izvrsava, ali exception koji neka_funkcija moze da baci nije uhvacen
tako da je ispravno:
with pytest.raises(ValueError):
    assert neka_funkcija(-1) 
SAV KOD KOJI BACA EXCEPTION MORA DA BUDE UNUTAR WITH BLOKA!!!
"""

# VEZBA
# pocetni aplikacioni kod koji se testira bi u praksi bio u zasevnom fajlu
# takodje ima i zadataka gde se testiraju metode iz taskManager.py!
def podeli(a:float,b:float)->float:
    # Podeli a sa b baca ValueError ako je b nula!
    if(b==0):
        raise ValueError("delilac ne sme biti nula")
    return a/b

def uzrast_u_kategoriju(godine:int)->str:
    # pretvara broj fodina u kategoriju npr maloletnik, odrasla osoba ili senior/penzioner haha
    # baca TypeError ako godine nisu int
    # ako su godine negativne ili vece od 115(nisam sigurna da li je neko poziveo vise od 115 godina hahah) vaca ValueError!
    if not isinstance(godine,int):
        raise TypeError(f"ocekuje se ceo broj, a dobijen je {type(godine).__name__}")
    if godine<0:
        raise ValueError("Godine ne mogu biti negativne")
    if godine>115:
        raise ValueError("Godine ne mogu biti vece od 115")
    if godine<18:
        return "maloletnik"
    if godine<65:
        return "odrasla osoba"
    return "senior"

def izvuci_prvi(lista:list):
    # vraca prvi element liste
    # TypeError ako argument nije lista
    # IndexError ako je lista prazna
    if not isinstance(lista,list):
        raise TypeError("argument mora biti lista")
    if len(lista)==0:
        raise IndexError("Lista je prazna")
    return lista[0]

# zadaci

 
# Zadatak 1 
# Napisati test koji proverava da podeli() baca ValueError kada je b=0.
 
 
# Zadatak 2 
# Napisati test koji proverava da podeli() NORMALNO radi kada su oba broja validna.
# (ovde ne testirate exception — testirate ispravan rezultat)
 
 
# Zadatak 3 
# Napisati test koji proverava da izvuci_prvi() baca IndexError za praznu listu.
 
 
# Zadatak 4 
# Napisati test koji proverava da uzrast_u_kategoriju() baca TypeError
# kada prosledite string umesto int (npr. "dvadeset").
 
 
# Zadatak 5 
# Napisati test koji proverava da uzrast_u_kategoriju() baca ValueError
# i da poruka greske SADRZI rec "negativne" — kada prosledite -1.
 
 
# Zadatak 6 
# Napisati dva testa u klasi TestUzrast:
#   - jedan koji proverava da 17 vraca "maloletnik"
#   - jedan koji proverava da -5 baca ValueError
 
 
# Zadatak 7 
# Napisati test koji proverava da izvuci_prvi() baca TypeError
# kada prosledite tuple umesto liste: (1, 2, 3)
# Zatim sacuvajte exception u exc_info i proverite da poruka sadrzi
# rec "lista" koristeci str(exc_info.value)
 
 
# Zadatak 8 
# Napisati test koji proverava da BazaKartica.obrisi() baca KeyError,
# i da poruka greske sadrzi ID koji ste pokusali da obrisete (npr. 777).
# Hint: KeyError poruka se nalazi u exc_info.value.args[0]
 
 
# Zadatak 9 
# Napisati test koji proverava DVE stvari za uzrast_u_kategoriju(200):
#   1. da baca ValueError
#   2. da poruka sadrzi rec "150"
# Ali ovaj put bez match= — sacuvaj exc_info i proveriti rucno sa assert.
