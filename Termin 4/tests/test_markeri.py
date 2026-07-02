import pytest,sys,time
from src.funkcije import kategorija_godina,ocena_u_rec,validan_username

# skip i skipif
# marker da preskocimo testiranje funkcije koja jos uvek nije implementirana i slicno, takodje mozemo i uslovno da preskacemo testove sa skipif
@pytest.mark.skip(reason="funkcija placanje() jos uvek nije implementirana")
def test_placanje():
    assert placanje(100)=="uspesno"

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