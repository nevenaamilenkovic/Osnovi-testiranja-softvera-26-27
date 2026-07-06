# Kao "online" prodavnica sa spoljnim zavisnostima
from dataclasses import dataclass, field

@dataclass
class Proizvod:
    naziv: str
    cena: float
    kolicina: int
    id: int = field(default=None, compare=False)

class SmsServis:
    # Pravi SMS servis — u testovima ga NIKAD ne koristimo direktno
    def posalji(self, na: str, poruka: str) -> None:  # pragma: no cover
        print(f"[SMS] -> {na}: {poruka}")

class PlacanjeServis:
    # Pravi servis za placanje — u testovima ga NIKAD ne koristimo direktno
    def naplati(self, iznos: float, kartica: str) -> bool:  # pragma: no cover
        # U produkciji bi ovde bio poziv ka banci
        # pored funkcije, komentar pragma: no cover kaze coverage alatu da ne gleda ovu liniju, ovom slucaju ignorisace celu funkciju
        print(f"[PLACANJE] naplata {iznos} din sa kartice {kartica}")
        return True

class ProdavnicaServis:
    # Glavni servis prodavnice.
    # Zavisi od SmsServisa i PlacanjeServisa — spoljne zavisnosti
    # U unit testovima ih mockujemo.
    def __init__(self, sms_servis: SmsServis, placanje_servis: PlacanjeServis):
        self._sms = sms_servis
        self._placanje = placanje_servis
        self._proizvodi: dict[int, Proizvod] = {}
        self._sledeci_id = 1

    def dodaj_proizvod(self, proizvod: Proizvod) -> int:
        #Dodaje proizvod u prodavnicu. Vraca dodeljeni ID
        if not proizvod.naziv:
            raise ValueError("Proizvod mora imati naziv")
        if proizvod.cena <= 0:
            raise ValueError("Cena mora biti veca od nule")
        if proizvod.kolicina < 0:
            raise ValueError("Kolicina ne moze biti negativna")

        novi = Proizvod(
            naziv=proizvod.naziv,
            cena=proizvod.cena,
            kolicina=proizvod.kolicina,
            id=self._sledeci_id,
        )
        self._proizvodi[self._sledeci_id] = novi
        self._sledeci_id += 1
        return novi.id

    def kupi(self, proizvod_id: int, kolicina: int, telefon: str, kartica: str) -> float:
# kartica je broj kartice debitne itd 1234-5678-9012-3456
        # Kupovina proizvoda
        # 1. Proverava da li postoji i ima dovoljno na stanju
        # 2. Naplacuje placanje
        # 3. Ako placanje uspe — smanjuje stanje i salje SMS potvrdu
        # 4. Ako placanje ne uspe — vraca ValueError, SMS se NE salje
        if proizvod_id not in self._proizvodi:
            raise KeyError(f"Proizvod sa ID={proizvod_id} ne postoji")

        proizvod = self._proizvodi[proizvod_id]

        if kolicina > proizvod.kolicina:
            raise ValueError(
                f'Nedovoljno na stanju: trazeno {kolicina}, dostupno {proizvod.kolicina}'
            )

        ukupno = proizvod.cena * kolicina

        # Spoljni poziv — u testovima mockujemo!
        uspelo = self._placanje.naplati(ukupno, kartica)

        if not uspelo:
            raise ValueError("Placanje nije uspelo")

        # Placanje uspelo — azuriraj stanje i obavestis korisnika
        proizvod.kolicina -= kolicina

        # Spoljni poziv — u testovima mockujemo!
        self._sms.posalji(
            telefon,
            f'Kupovina potvrdjana: {kolicina}x "{proizvod.naziv}" za {ukupno} din.',
        )

        return ukupno

    def vrati_proizvod(self, proizvod_id: int, kolicina: int, telefon: str) -> None:
        # Vracanje kupljenog proizvoda.
        # Uvecava stanje i salje SMS obavestenje
        if proizvod_id not in self._proizvodi:
            raise KeyError(f"Proizvod sa ID={proizvod_id} ne postoji")

        if kolicina <= 0:
            raise ValueError("Kolicina za vracanje mora biti veca od nule")

        proizvod = self._proizvodi[proizvod_id]
        proizvod.kolicina += kolicina

        # Spoljni poziv — u testovima mokukejmo
        self._sms.posalji(
            telefon,
            f'Vracanje primljeno: {kolicina}x "{proizvod.naziv}". Hvala!',
        )

    def broj_proizvoda(self) -> int:
        #Ukupan broj razlicitih proizvoda u prodavnici
        return len(self._proizvodi)

    def dostupna_kolicina(self, proizvod_id: int) -> int:
        #Koliko komada je dostupno za dati proizvod
        if proizvod_id not in self._proizvodi:
            raise KeyError(f"Proizvod sa ID={proizvod_id} ne postoji")
        return self._proizvodi[proizvod_id].kolicina
