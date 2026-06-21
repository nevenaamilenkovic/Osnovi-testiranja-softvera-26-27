"""
unit testovi
testiraju se male izolovane jedinice koda

pip install pytest
"""

# najjednostavniji test
def test_prolazi():
    assert 1+1==2

def test_pada():
    # assert 1+1==4
    pass

def test_stringovi():
    poruka="zdravo svete"
    assert "zdravo" in poruka
    assert poruka.startswith("zdravo")
    assert len(poruka)==12

def test_liste():
    boje=["crvena","plava","zelena"]
    assert "zelena" in boje
    assert len(boje) == 3
    assert boje[0]=="crvena"

def test_recnik():
    korisnik={"ime":"Ana","godine":25}
    assert korisnik["ime"]=="Ana"
    assert "godine" in korisnik
    assert korisnik["godine"]>18

# testiranje na greske
import pytest

def podeli(a,b):
    return a/b

def test_deljenje_nulom():
    with pytest.raises(ZeroDivisionError):
        podeli(10,0)
def test_deljenje_nulom_sa_porukom():
    with pytest.raises(ZeroDivisionError,match="division by zero"):
        podeli(4,0)

# pytest.raises - ocekujem da ce ova linija baciti gresku ako ne baci test pada

def test_namerna_greska():
    ocekivano = [1,2,3]
    dobijeno=[3,2,1]
    assert ocekivano == dobijeno
    # obratiti paznju na assertation error poruku
    # prikazuje koji se element razlikuje
    