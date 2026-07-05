# Prosirena biblioteka sa spoljnim zavisnostima

from dataclasses import dataclass, field


@dataclass
class Knjiga:
    naslov: str
    autor: str
    godina: int
    dostupna: bool = True
    id: int = field(default=None, compare=False)


class EmailServis:
    # Pravi email servis — u testovima ga NIKAD ne koristimo direktno
    def posalji(self, na: str, naslov: str, poruka: str) -> None:
        # U produkciji bi ovde bio SMTP kod
        # U testovima ovo NIKAD ne pozivamo — koristimo mock
        print(f"[EMAIL] -> {na}: {naslov}")


class IzvestajServis:
    # Generise izvestaje — cita/pise fajlove
    def sacuvaj_izvestaj(self, putanja: str, sadrzaj: str) -> None:
        # U produkciji pise u fajl
        # U testovima mockujemo da ne pisemo na disk
        with open(putanja, "w") as f:
            f.write(sadrzaj)

    def ucitaj_izvestaj(self, putanja: str) -> str:
        with open(putanja, "r") as f:
            return f.read()


class BibliotekaServis:
    # Glavni servis biblioteke.
    # Zavisi od EmailServisa i IzvestajServisa — spoljne zavisnosti.
    # U unit testovima ih mockujemo.
    def __init__(self, email_servis: EmailServis, izvestaj_servis: IzvestajServis):
        self._email = email_servis
        self._izvestaj = izvestaj_servis
        self._knjige: dict[int, Knjiga] = {}
        self._sledeci_id = 1

    def dodaj_knjigu(self, knjiga: Knjiga) -> int:
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

    def pozajmi(self, knjiga_id: int, korisnik_email: str) -> None:
        #Pozajmljuje knjigu i salje email korisniku
        if knjiga_id not in self._knjige:
            raise KeyError(f"Knjiga sa ID={knjiga_id} ne postoji")
        knjiga = self._knjige[knjiga_id]
        if not knjiga.dostupna:
            raise ValueError(f'Knjiga "{knjiga.naslov}" nije dostupna')
        knjiga.dostupna = False
        # Spoljni poziv — u testovima mockujemo!
        self._email.posalji(
            na=korisnik_email,
            naslov="Knjiga pozajmljena",
            poruka=f'Pozajmili ste knjigu "{knjiga.naslov}"',
        )

    def vrati(self, knjiga_id: int, korisnik_email: str) -> None:
        # Vraca knjigu i salje email korisniku
        if knjiga_id not in self._knjige:
            raise KeyError(f"Knjiga sa ID={knjiga_id} ne postoji")
        knjiga = self._knjige[knjiga_id]
        if knjiga.dostupna:
            raise ValueError(f'Knjiga "{knjiga.naslov}" nije bila pozajmljena')
        knjiga.dostupna = True
        self._email.posalji(
            na=korisnik_email,
            naslov="Knjiga vracena",
            poruka=f'Uspesno ste vratili knjigu "{knjiga.naslov}"',
        )

    def generisi_izvestaj(self, putanja: str) -> str:
        #Generise izvestaj i cuva ga u fajl
        linije = []
        for k in self._knjige.values():
            status = "dostupna" if k.dostupna else "pozajmljena"
            linije.append(f"{k.id}. {k.naslov} — {k.autor} [{status}]")
        sadrzaj = "\n".join(linije)
        # Spoljni poziv — u testovima mockujemo!
        self._izvestaj.sacuvaj_izvestaj(putanja, sadrzaj)
        return sadrzaj

    def broj_knjiga(self) -> int:
        return len(self._knjige)

    def broj_dostupnih(self) -> int:
        return sum(1 for k in self._knjige.values() if k.dostupna)
