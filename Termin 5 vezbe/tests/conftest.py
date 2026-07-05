# Zadatak 1 G1
# Napravi tri fixture-a:
#
#   lazni_sms — MagicMock sa spec=SmsServis
#   lazno_placanje — MagicMock sa spec=PlacanjeServis
#   prodavnica — ProdavnicaServis koji koristi lazni_sms i lazno_placanje
# Hint: isto kao lazni_email i servis iz lekcije


# Zadatak 2 G1
# Napravi fixture prodavnica_sa_proizvodom koja:
#- koristi fixture prodavnica
#- dodaje jedan proizvod: naziv="Slusalice", cena=3500.0, kolicina=10
#- vraca tuple (prodavnica, proizvod_id)
