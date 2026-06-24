import pytest
from src.biblioteka import Biblioteka,Knjiga

@pytest.fixture()
def prazna_biblioteka():
    biblioteka=Biblioteka(naziv="Biblioteka")
    return biblioteka