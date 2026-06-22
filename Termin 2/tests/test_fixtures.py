"""
Dosadasnji testovi su bili malo redudantni,
mahom je svaki test pocinjao istim kodom
npr:
def test_dodaj():
    baza=BazaKartica()
    ....
def test_obrisi():
    baza=BazaKartica()
    ....
def test_broj():
    baza=BazaKartica()
    ....
Kako bi to sprecili, odnosno kako bi smanjili ponavljanje koristimo nesto sto se zove FIXTURE
Fixture je funkcija koja taj zajednicki ARRANGE kod izvuce na
jedno mesto i pytest(ako je fixture inkludovan) moze da je pozove automatskki pre svakog testa 
Ispod je data sintaksa(osnovna)
"""
import pytest
from src.taskManager import BazaKartica,Kartica
# fixture
@pytest.fixture()#obavezan dekorator
def prazna_baza():
    return BazaKartica()
# test koji koristi fixture
def test_broj(prazna_baza):#koristi fixture!!
    assert prazna_baza.broj()==0