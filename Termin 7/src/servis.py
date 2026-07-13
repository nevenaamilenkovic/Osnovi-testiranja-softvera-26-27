# rest api https://api.restful-api.dev
# Javni endpointi (bez autentifikacije):
# GET    https://api.restful-api.dev/objects        lista svih
# GET    https://api.restful-api.dev/objects/{id}   jedan
# POST   https://api.restful-api.dev/objects        dodaj
# PATCH  https://api.restful-api.dev/objects/{id}   delimicno azuriraj
# DELETE https://api.restful-api.dev/objects/{id}  obrisi
# za rad sa apijem treba requests
# pip install requests


from dataclasses import dataclass, field
import requests

@dataclass
class Uredjaj:
    naziv: str
    podaci: dict
    id: str = field(default=None, compare=False)

class UredjajApiKlijent:
    # HTTP klijent koji direktno poziva restful-api.dev.
    # U unit testovima ga UVEK mockujemo
    # U integration testovima koristimo pravi

    BASE_URL = "https://api.restful-api.dev/objects"

    def uzmi_sve(self) -> list[dict]:  # pragma: no cover
        odgovor = requests.get(self.BASE_URL)
        odgovor.raise_for_status()
        return odgovor.json()

    def uzmi_jedan(self, uredjaj_id: str) -> dict:  # pragma: no cover
        odgovor = requests.get(f"{self.BASE_URL}/{uredjaj_id}")
        odgovor.raise_for_status()
        return odgovor.json()

    def dodaj(self, naziv: str, podaci: dict) -> dict:  # pragma: no cover
        odgovor = requests.post(
            self.BASE_URL,
            json={"name": naziv, "data": podaci},
        )
        odgovor.raise_for_status()
        return odgovor.json()

    def azuriraj(self, uredjaj_id: str, naziv: str) -> dict:  # pragma: no cover
        odgovor = requests.patch(
            f"{self.BASE_URL}/{uredjaj_id}",
            json={"name": naziv},
        )
        odgovor.raise_for_status()
        return odgovor.json()

    def obrisi(self, uredjaj_id: str) -> str:  # pragma: no cover
        odgovor = requests.delete(f"{self.BASE_URL}/{uredjaj_id}")
        odgovor.raise_for_status()
        return odgovor.json().get("message", "")


class UredjajServis:
    # Servis za upravljanje uredjajima
    # Sadrzi poslovnu logiku — filtriranje, validaciju, formatiranje
    # Zavisi od UredjajApiKlijent koji poziva pravi API

    def __init__(self, klijent: UredjajApiKlijent):
        self._klijent = klijent

    def svi_uredjaji(self) -> list[Uredjaj]:
        # Vraca sve uredjaje sa API-ja
        sirovi = self._klijent.uzmi_sve()
        return [
            Uredjaj(naziv=u["name"], podaci=u.get("data") or {}, id=u["id"])
            for u in sirovi
        ]

    def uzmi(self, uredjaj_id: str) -> Uredjaj:
        # Vraca jedan uredjaj po ID-u
        if not uredjaj_id or not uredjaj_id.strip():
            raise ValueError("ID ne sme biti prazan")
        sirovi = self._klijent.uzmi_jedan(uredjaj_id)
        return Uredjaj(
            naziv=sirovi["name"],
            podaci=sirovi.get("data") or {},
            id=sirovi["id"],
        )

    def dodaj(self, naziv: str, podaci: dict) -> Uredjaj:
        #Dodaje novi uredjaj
        if not naziv.strip():
            raise ValueError("Naziv uredjaja ne sme biti prazan")
        sirovi = self._klijent.dodaj(naziv, podaci)
        return Uredjaj(naziv=sirovi["name"], podaci=sirovi.get("data") or {}, id=sirovi["id"])

    def preimenuj(self, uredjaj_id: str, novi_naziv: str) -> Uredjaj:
    # Menja naziv uredjaja
        if not novi_naziv.strip():
            raise ValueError("Novi naziv ne sme biti prazan")
        sirovi = self._klijent.azuriraj(uredjaj_id, novi_naziv)
        return Uredjaj(naziv=sirovi["name"], podaci=sirovi.get("data") or {}, id=sirovi["id"])

    def obrisi(self, uredjaj_id: str) -> str:
        # Brise uredjaj i vraca poruku
        return self._klijent.obrisi(uredjaj_id)

    def pretrazi_po_nazivu(self, kljucna_rec: str) -> list[Uredjaj]:
        # Pretrazuje uredjaje po nazivu (case-insensitive)
        svi = self.svi_uredjaji()
        return [u for u in svi if kljucna_rec.lower() in u.naziv.lower()]

    def apple_uredjaji(self) -> list[Uredjaj]:
    # Vraca samo Apple uredjaje.
        return self.pretrazi_po_nazivu("apple")

    def uredjaji_sa_cenom(self) -> list[Uredjaj]:
        # Vraca samo uredjaje koji imaju cenu u podacimas
        svi = self.svi_uredjaji()
        return [u for u in svi if "price" in u.podaci]
