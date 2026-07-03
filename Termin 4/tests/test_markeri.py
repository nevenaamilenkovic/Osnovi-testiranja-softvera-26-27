import pytest
from src.funkcije import kategorija_godina,ocena_u_rec,validan_username
# marker je oznaka koja se stavlja na test funkciju
# govori pytestu nesto o tom testu
# npr. preskoci test(ne pokreci), ocekuj da padne(test mozda prolazi, ali treba da padne), pokreni samo odredjene testove i slicno...
# neki od najvaznijih ugradjenih markera su skip(uvek preskoci test), skipif(preskoci ako je uslov tacan)
# skipif moze da bude korisan za testove koji zavise od operativnog sistema, verzije pythona ili nekog drugog resursa...
# i xfail(ocekivano pada)
# Test pada ocekivano - xfail - sve je ok, bug je poznat
# Test prolazi neocekivano - xpass - bug je mozda popravljen

# postoje i custom markeri, tj mozemo da definisemo sopstvene markere i da ih koristimo za grupisanje testova
# marker mora da se registruje prethodno u novom fajlu pytest.ini:
# fajl mora biti u root folderi tj na istom nivou odakle se pokrece pytest
# [pytest]
# markers=
#     spor:testovi koji dugoo traju

# npr.
@pytest.mark.spor
def test_koji_dugo_traje():
    assert 1==1
    assert isinstance(2,int)
    # itd nisam kreativna
# ovaj test moze da se pokrene sa
# pytest -v -m spor
# pokretanje:
# pytest test_markeri.py -v (svi testovi)
# pytest test_markeri.py -v -m smoke (samo brzi smoke testovii)
# pytest test_markeri.py -v -m "not spor" (svi testovi osim sporih)
# pytest --markers (lista svih registrovanih markera)



# skip i skipif
# marker da preskocimo testiranje funkcije koja jos uvek nije implementirana i slicno, takodje mozemo i uslovno da preskacemo testove sa skipif
@pytest.mark.skip(reason="funkcija placanje() jos uvek nije implementirana")
def test_placanje():
    assert placanje(100)=="uspesno"

import sys
@pytest.mark.skipif(sys.version_info<(3,10),reason="zahteva Python 3.10+")
def test_match_naredba():
    # match case je dodat u py 3.10
    # ako je stariji py test se preskace automatski
    broj=3
    match broj:
        case 1: rezultat="jedan"
        case 2: rezultat="dva"
        case 3: rezultat="tri"
        case 4: rezultat="nepoznato"
    assert rezultat == "tri"

# xfail -> kada se ocekuje da test padne
@pytest.mark.xfail(reason="bug kategorija_godina(True) treba da baci TypeError")
def test_bool_kao_godine():
    # test pada jer bool prolazi proveru isinstance(_,int)
    # svakako bool nije isto sto i celi broj
    # kada se bug na funkciji kategorija_godina() popravi test ce postati xpass()
    with pytest.raises(TypeError):
        kategorija_godina(True)

@pytest.mark.xfail(strict=True,reason="ovo mora da pada ne sme nikada da prodje")
def test_koji_mora_da_padne():
    assert 1==2


# custom markeri
@pytest.mark.smoke
def test_kategorija_osnovna():
    # oco je najosnovniji test, provera da li finkcija uopste radi
    assert kategorija_godina(25)=="odrasla osoba"

@pytest.mark.smoke
def test_ocena_osnovna():
    assert ocena_u_rec(5)=="odlican"

@pytest.mark.validacija
@pytest.mark.parametrize("godine,ocekivano",[
    (0,"maloletnik"),
    (17,"maloletnik"),
    (18,"odrasla osoba"),
    (65,"senior"),
])
def test_kategorija_granicne_vrednosti(godine, ocekivano):
    # validacija granicnih vrednosti
    assert kategorija_godina(godine)==ocekivano

@pytest.mark.greske
@pytest.mark.parametrize("godine,tip",[
    (-1,ValueError),
    (151,ValueError),
    ("x",TypeError),
    (True,TypeError),#ovo treba da prodje ali pada! bool nije isto sto i int!
])
def test_kategorija_greske(godine,tip):
    with pytest.raises(tip):
        kategorija_godina(godine)

import time
@pytest.mark.spor
def test_spori_test():
    # simulacija sporog testa
    # npr kad se ceka na odgovvor serveera
    time.sleep(1)
    assert validan_username("nevena_test") is True


from src.biblioteka import Knjiga,Biblioteka
@pytest.fixture()
def prazna_biblioteka():
    return Biblioteka(naziv="Test biblioteka")

@pytest.mark.regression
@pytest.mark.parametrize("naslov,autor,godina",[
    ("SQL programiranje","Dr Snezana R. Popovic",2020),
    ("Baze podataka","Dr Snezana R. Popovic",2024),
    ("Python bez oklevanja","Paul Barry",2017),
])
def test_dodaj_razlicite_knjige(prazna_biblioteka,naslov,autor,godina):
    kId=prazna_biblioteka.dodaj_knjigu(
        Knjiga(naslov=naslov,autor=autor,godina=godina)
    )
    pronadjena=prazna_biblioteka.uzmi_knjigu(kId)
    assert pronadjena.naslov==naslov
    assert pronadjena.autor==autor
    assert pronadjena.godina==godina

# pokretanje jos jednom
# pytest --markers SVI MARKERI KOJI POSTOJE(LISTA)
# pytest test_markeri.py -v -m smoke SAMO SMOKE TESTOVI
# pytest test_markeri.py -v -m "not spor" SVI TESTOVI OSIM ONIH KOJI NOSE MARKER SPOR
# pytest test_markeri.py -v -m "smoke or regression" SAMO SMOKE ILI REGRESSION TESTOVI AKO IMA I SMOKE I REGRESSION POKRENUCE OBE VRSTE, AKO IMA SSAMO SMOKE ONNDA SAMO SMOKE POKRECE, ZA REGRESSIO VAZI ISTO
# IZMEDJU JE LOGICKO ILI!!!
# pytest test_markeri.py -v --runxfail POKRECE SVE TESTOVE UKLJUCUJUCI I ONE KOJI SU MARKIRANI SA XFAIL SASVIM NORMALNO!
