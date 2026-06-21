# zadaci za vezbu

# Testiranje dataclass-e Kartica

# Zadatak 1
# Napisati test koji proverava da Kartica kreirana bez ijednog argumenta
# ima sve vrednosti None, osim stanja koje je "na_cekanju".
 
 
# Zadatak 2
# Napisati test koji proverava da metoda u_recnik() ispravno pretvara
# karticu u recnik — ali ovaj put kartica ima samo opis, ostalo je None.
# (sta oceekujete da bude u recniku za vlasnik i id?)
 
 
# Zadatak 3
# Napisati test koji proverava da dve Kartice sa istim opisom i vlasnikom, ali RAZLICITIM stanjem, NISU jednake.




# Testiranje "Baze kartica"

# Zadatak 4
# Napisati test koji proverava da nova (prazna) baza ima broj() == 0.
# (najmanji moguci "smoke test" — da li baza uopste radi?)
 
 
# Zadatak 5
# Napisati test koji proverava da nakon dodavanja TRI kartice,
# lista() vraca tačno 3 elementa.
 
 
# Zadatak 6
# Napisati test koji proverava da zavrsi() ispravno menja stanje kartice.
# Kartica treba da pocne u stanju "u_toku", a nakon zavrsi() bude "zavrseno".
 
 
# Zadatak 7
# Napisati test koji proverava da azuriraj() menja SAMO opis kartice,
# a da vlasnik i stanje ostanu nepromenjeni.
# mali hint: kreirati karticu sa svim poljima, pa azurirajte samo opis.




# Testiranje gresaka i izuzetaka
# Zadatak 8
# Napisati test koji proverava da obrisi() baca KeyError
# kada pokusate da obrisete karticu koja ne postoji (npr. id=42).
 
 
# Zadatak 9
# Napisatii test koji proverava da dodaj() baca TypeError
# kada mu prosledite nešto sto nije Kartica objekat (npr. string "greska").


# Oranizacija testova u klase


