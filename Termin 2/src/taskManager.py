# mini task tracker po uzoru na aplikaciju Cards iz knjige Python testing with pytest
# kartica=zadatak

from dataclasses import dataclass, field


@dataclass
class Kartica:
    #Jedan zadatak (kartica) u sistemu pracenja
    opis: str = None
    vlasnik: str = None
    #"na_cekanju", "u_toku", "zavrseno"
    stanje: str = "na_cekanju"
    id: int = field(default=None, compare=False)

    @classmethod
    def iz_recnika(cls, r: dict) -> "Kartica":
        #Kreira karticu iz recnika
        return cls(**r)

    def u_recnik(self) -> dict:
        #Pretvara karticu u recnik
        return {
            "opis": self.opis,
            "vlasnik": self.vlasnik,
            "stanje": self.stanje,
            "id": self.id,
        }


class BazaKartica:
    #Baza podataka za kartice (u memoriji, za ucenje :D)

    def __init__(self):
        self._kartice: dict[int, Kartica] = {}
        self._sledeci_id = 1

    def dodaj(self, kartica: Kartica) -> int:
        #Dodaje karticu i vraca njen ID
        if not isinstance(kartica, Kartica):
            raise TypeError("Ocekivan objekat tipa Kartica")
        nova = Kartica(
            opis=kartica.opis,
            vlasnik=kartica.vlasnik,
            stanje=kartica.stanje,
            id=self._sledeci_id,
        )
        self._kartice[self._sledeci_id] = nova
        self._sledeci_id += 1
        return nova.id

    def uzmi(self, kartica_id: int) -> Kartica:
        #Vraca karticu po ID-u
        if kartica_id not in self._kartice:
            raise KeyError(f"Kartica sa ID={kartica_id} ne postoji")
        return self._kartice[kartica_id]

    def lista(self) -> list[Kartica]:
        #Vraca sve kartice
        return list(self._kartice.values())

    def azuriraj(self, kartica_id: int, izmene: Kartica) -> None:
        #Azurira polja kartice (preskace None(odnosno polja ya koja izmene nisu unete) vrednosti)
        postojeca = self.uzmi(kartica_id)
        if izmene.opis is not None:
            postojeca.opis = izmene.opis
        if izmene.vlasnik is not None:
            postojeca.vlasnik = izmene.vlasnik
        if izmene.stanje is not None:
            postojeca.stanje = izmene.stanje

    def zapocni(self, kartica_id: int) -> None:
        #Menja stanje kartice u stanje 'u_toku'
        self.azuriraj(kartica_id, Kartica(stanje="u_toku"))

    def zavrsi(self, kartica_id: int) -> None:
        #Menja stanje kartice u stanje 'zavrseno'
        self.azuriraj(kartica_id, Kartica(stanje="zavrseno"))

    def obrisi(self, kartica_id: int) -> None:
        #Brise karticu po ID-u
        if kartica_id not in self._kartice:
            raise KeyError(f"Kartica sa ID={kartica_id} ne postoji")
        del self._kartice[kartica_id]

    def broj(self) -> int:
        #Vraca ukupan broj kartica
        return len(self._kartice)