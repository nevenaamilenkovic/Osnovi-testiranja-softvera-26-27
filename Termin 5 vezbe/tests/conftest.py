# Zadatak 1 G1
# Napraviti tri fixture-a:
#
#   lazni_sms — MagicMock sa spec=SmsServis
#   lazno_placanje — MagicMock sa spec=PlacanjeServis
#   prodavnica — ProdavnicaServis koji koristi lazni_sms i lazno_placanje


# Zadatak 2 G1
# Napraviti fixture prodavnica_sa_proizvodom koja:
#- koristi fixture prodavnica
#- dodaje jedan proizvod: naziv="Slusalice", cena=3500.0, kolicina=10
#- vraca tuple (prodavnica, proizvod_id)
