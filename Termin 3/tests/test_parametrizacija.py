# parametrizacija je tehnika kojom jedan test mozemo pokrenuti vise puta
# sa razlicitim ulaznim podacima
# umesto da pisemo desetak skoro identicnih test funkcija, pisemo jednu ali joj 
# dajemo 10 setova podataka

# Parametrizacija se koristi kada se:
# testira ista logika sa vise razlicitih vresnoti
# testiraju granicne vrednosti
# testiraju ekvivalentne klase - sve vrednosti koje treba da daju isti rezultat
# i kada se proverava vise tipova gresaka za istu fonkciju

# parametrizacija se ne koristi kada svaki test case zahteva drugaciji setup i kada testovi nisu logicki povezani

def broj_u_rec(broj:int)->str:
    if not isinstance(broj,int):
        raise TypeError(f"ocekivan je int, a dobijen {type(broj).__name__}")
    if broj<1 or broj>10:
        raise ValueError(f"broj mora biri izmedju 1 i 10, a dobijen je: {broj}")
    brojevi={
        1:"jedan",2:"dva",3:"tri",
        4:"cetiri",5:"pet",6:"sest",
        7:"sedam",8:"osam",9:"devet",10:"deset"
    }
    return brojevi[broj]

# tri nacina parametrizacije u pytestu:
import pytest
# dekorator nad test funkcijom - najcesce koriscen
@pytest.mark.parametrize("ulaz,ocekivano",[
    (1,"jedan"),
    (2,"dva"),
    (3,"tri"),
])
def test_broj_u_rec(ulaz,ocekivano):
    assert broj_u_rec(ulaz)==ocekivano
    # na ovaj nacin dobili smo 3 testa, iste funkcije ali sa razlicitim ulaznim i izlaznim podacima