import pytest
from src.kalkulator import saberi, oduzmi,pomnozi,podeli

# test 1 sabiranje
def test_saberi_pozitivni_brojevi():
    rezultat = saberi(3,5)
    assert rezultat == 8
def test_saberi_negativni_broj():
    assert saberi(-2,5) == 3
def test_saberi_nule():
    assert saberi(0,0) == 0

#  test 2 oduzimanje
def test_oduzmi_veci_od_manjeg():
    assert oduzmi(10,3) == 7
def test_oduzmi_rezultat_negativan():
    assert oduzmi(3,10) == -7

# test 3 mnozenje
def test_pomnozi_pozitivni():
    assert pomnozi(4,5) == 20
def test_pomnozi_sa_nulom():
    assert pomnozi(7,0) == 0

# test 4 deljenje (i test greskee)
def test_podeli_normalno():
    assert podeli(10,2) == 5
# @pytest.mark.skip
def test_podeli_nulom_greska():
    with pytest.raises(ValueError):
        podeli(5,0)

"""
pokretanje svih testova: pytest
pokretanje sa detaljnim izlazom: pytest -v
potretanje datoteke: pytest .\tests\test_kalkulator.py
pokretanje specificnog testa: pytest .\tests\test_kalkulator.py::test_saberi_pozitivni_brojevi -v

Izlaz
PASSED(zeleno) - test je prosao, kod se ponasa ispravno
FAILED(crveno) - test je pao, postoji bug ili je test pogresno napisan
ERROR - doslo je do greske pri pokretanju testa(ne u kodu)
SKIPPED - test je preskocen(ako je koriscen dekorator @pytest.mark.skip)
"""

# prosirenje testova
# test 5 sabiranje decimalnih
def test_saberi_decimalni_brojevi():
    assert saberi(1.5,2.3)==3.8
# test 6 mnozenje negativnih
def test_pomnozi_dva_negativna():
    assert pomnozi(-3,-4)==12
def test_pomnozi_pozitivan_i_negativan():
    assert pomnozi(5,-3)==-15
# test 7 deljenje
def test_podeli_rezultat_decimalan():
    assert podeli(7,2)==3.5
def test_podeli_negativnim_brojem():
    assert podeli(10,-2)==-5.0