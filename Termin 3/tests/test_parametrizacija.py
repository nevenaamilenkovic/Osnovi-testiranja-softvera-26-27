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
# imate u src/funkcije.py
# def broj_u_rec(broj:int)->str:
#     if not isinstance(broj,int):
#         raise TypeError(f"ocekivan je int, a dobijen {type(broj).__name__}")
#     if broj<1 or broj>10:
#         raise ValueError(f"broj mora biri izmedju 1 i 10, a dobijen je: {broj}")
#     brojevi={
#         1:"jedan",2:"dva",3:"tri",
#         4:"cetiri",5:"pet",6:"sest",
#         7:"sedam",8:"osam",9:"devet",10:"deset"
#     }
#     return brojevi[broj]
from src.funkcije import broj_u_rec
# tri nacina parametrizacije u pytestu:
import pytest
# 1. dekorator nad test funkcijom - najcesce koriscen
@pytest.mark.parametrize("ulaz,ocekivano",[
    (1,"jedan"),
    (2,"dva"),
    (3,"tri"),
])
def test_broj_u_rec(ulaz,ocekivano):
    assert broj_u_rec(ulaz)==ocekivano
    # na ovaj nacin dobili smo 3 testa, iste funkcije ali sa razlicitim ulaznim i izlaznim podacima

# 2. params atribut ununar fixture-a
# kada vise testova treba da rade nad istim skupom objekata
@pytest.fixture(params=["Ana","Marko","Jovana"])
def ime(request):
    return request.param

def test_ime_nije_prazno(ime):
    assert len(ime)>0

# 3. pytest_generate_tests
# to je napredna dinamicka parametrizacija
# za sada nnista o tome...

# Testovi na granicne vrednosti
# Granicne vresnosti su vazne jer se greske najcesce kriju na granicama uslova
# u folderu src imate fajl funkcije.py gde se nalaze funkcije koje ce ovde dalje biti testirane
