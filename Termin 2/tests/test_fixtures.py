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
# scope="function" -> nova prazna baza za svaki test, nema ponavljanja
@pytest.fixture()#obavezan dekorator
def prazna_baza():
    return BazaKartica()
# test koji koristi fixture
def test_broj_prazna_baza(prazna_baza):#koristi fixture!!
    # sam fixture se "trazi" kada se postavi kao parametar test funkcije!
    assert prazna_baza.broj()==0

# fixture koji moze biti jako korisan!
# baza koja je popunjena sa test podacima kako ne bi morali da je popunjavamo unutar testa
# vrati bazu sa cetiri kartice
# cisti se automatski nakon svakog testa
# tj vraca se na prethodno dobro stanje za svaki test
@pytest.fixture()
def popunjena_baza():
    # SETUP je priprema (resursa, u nsaem slucaju baze)
    baza=BazaKartica()
    baza.dodaj(Kartica(opis="Uvod u pytest", vlasnik="Nevena"))
    baza.dodaj(Kartica(opis="Selenium", vlasnik="Nevena"))
    baza.dodaj(Kartica(opis="Python", vlasnik="Dusan"))
    baza.dodaj(Kartica(opis="C prograrmiranje", vlasnik="Dusan"))
    # yeild se koristi umesto return! da bi se fixture posle samostalno cistio sve nakon testa
    # u nasem slucaju spremi fresh bazu za sledeci test
    yield baza#test dobija popunjenu bazu ovde tj u trenutku izvrsavanja yeild-a i dalje moze da radi sa njom
    # TEARDOWN je to ciscenje koj se izvrsi nakon testa
    # kod ove nase in memory baze ovo nije potrebno, kada se radi sa pravom bazom
    # u teardown delu bi se zatvarala konekcija i sl
    print("\nBaza je ociscena")
    # Sve pre yield-a je SETUP, a sve nakon je TEARDOWN

"""
SCOPE->pokretanje fixtura u nasem slucaju, tj koliko se cesto fixture pokrece!
@pytest.fixture(scope="function") ili samo @pytest.fixture() default — nova baza za SVAKI test
@pytest.fixture(scope="class")    jedna baza za sve testove u klasi
@pytest.fixture(scope="module")   jedna baza za sve testove u fajlu
@pytest.fixture(scope="session")  jedna baza za ceo test run
"""
# kada radite sa bazom uvek se koristi function scope da bi svaki test imao svezu praznu bazu!!!
def test_broj(popunjena_baza):
    assert popunjena_baza.broj()==4