import pytest
from src.string_helper import obrni_string,je_palindrom,izbroj_samoglasnike

# test 1 obrni
def test_obrni_normalni_string():
    assert obrni_string("hello") == "olleh"
def test_obrni_prazan_string():
    assert obrni_string("")==""
def test_obrni_jedan_karakter():
    assert obrni_string("a")=="a"

# test 2 prebroj samoglasnike
def test_prebroj_samoglanike_normalno():
    assert izbroj_samoglasnike("hello")==2
def test_prebroj_samoglasnike_bez_samoglasnika():
    assert izbroj_samoglasnike("xyz")==0
def test_prebroj_samoglasnike_samo_samoglasnici():
    assert izbroj_samoglasnike("aeiou")==5

# test 3 palindrom
def test_je_palindrom_da():
    assert je_palindrom("mace jede jecam") == True
def test_je_palindrom_ne():
    assert je_palindrom("hello")==False
def test_je_palindrom_spojeno():
    assert je_palindrom("anavolimilovana")==True
