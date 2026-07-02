import pytest,sys,time
from src.funkcije import kategorija_godina,ocena_u_rec,validan_username

# skip i skipif
# marker da preskocimo testiranje funkcije koja jos uvek nije implementirana
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