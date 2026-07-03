from dataclasses import dataclass, field

@dataclass
class Knjiga:
    #Jedna knjiga u biblioteci
    naslov: str
    autor: str
    godina: int
    dostupna: bool = True
    id: int = field(default=None, compare=False)

    def __str__(self):
        status = "dostupna" if self.dostupna else "pozajmljena"
        return f'"{self.naslov}" — {self.autor} ({self.godina}) [{status}]'


class Biblioteka:
    #Sistem za upravljanje knjigama u biblioteci

    def __init__(self, naziv: str):
        self.naziv = naziv
        self._knjige: dict[int, Knjiga] = {}
        self._sledeci_id = 1

    def dodaj_knjigu(self, knjiga: Knjiga) -> int:
        #Dodaje knjigu u biblioteku i vraca njen id
        if not isinstance(knjiga, Knjiga):
            raise TypeError("Ocekivan objekat tipa Knjiga")
        if not knjiga.naslov or not knjiga.autor:
            raise ValueError("Knjiga mora imati naslov i autora")
        nova = Knjiga(
            naslov=knjiga.naslov,
            autor=knjiga.autor,
            godina=knjiga.godina,
            dostupna=True,
            id=self._sledeci_id,
        )
        self._knjige[self._sledeci_id] = nova
        self._sledeci_id += 1
        return nova.id

    def uzmi_knjigu(self, knjiga_id: int) -> Knjiga:
        #Vraca knjigu po ID-u
        if knjiga_id not in self._knjige:
            raise KeyError(f"Knjiga sa ID={knjiga_id} ne postoji u biblioteci")
        return self._knjige[knjiga_id]

    def pozajmi(self, knjiga_id: int) -> None:
        # pozajmljuje knjigu. Baca ValueError ako nije dostupna
        knjiga = self.uzmi_knjigu(knjiga_id)
        if not knjiga.dostupna:
            raise ValueError(f'Knjiga "{knjiga.naslov}" nije dostupna za pozajmljivanje')
        knjiga.dostupna = False

    def vrati(self, knjiga_id: int) -> None:
        #vraca pozajmljenu knjigu. Baca ValueError ako nije bila pozajmljena
        knjiga = self.uzmi_knjigu(knjiga_id)
        if knjiga.dostupna:
            raise ValueError(f'Knjiga "{knjiga.naslov}" nije bila pozajmljena')
        knjiga.dostupna = True

    def sve_knjige(self) -> list[Knjiga]:
        #Vraca listu svih knjiga
        return list(self._knjige.values())

    def dostupne_knjige(self) -> list[Knjiga]:
        #Vraca samo knjige koje su trenutno dostupne
        return [k for k in self._knjige.values() if k.dostupna]

    def trazi_po_autoru(self, autor: str) -> list[Knjiga]:
        #Vraca sve knjige datog autora (case-insensitive)
        return [k for k in self._knjige.values()
                if autor.lower() in k.autor.lower()]

    def broj_knjiga(self) -> int:
        # vraca ukupan broj knjiga u biblioteci
        return len(self._knjige)

    def broj_dostupnih(self) -> int:
        # vraca broj trenutno dostupnih knjiga
        return len(self.dostupne_knjige())
