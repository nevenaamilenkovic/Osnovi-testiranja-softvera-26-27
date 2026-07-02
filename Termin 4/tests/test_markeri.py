import pytest,sys,time
from src.funkcije import kategorija_godina,ocena_u_rec,validan_username

# skip i skipif
# marker da preskocimo testiranje funkcije koja jos uvek nije implementirana
@pytest.mark.skip(reason="funkcija placanje() jos uvek nije implementirana")
def test_placanje():
    assert placanje(100)=="uspesno"