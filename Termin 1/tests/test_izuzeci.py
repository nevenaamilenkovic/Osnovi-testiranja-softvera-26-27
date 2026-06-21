# kada se pise kod obicno dve stvari mogu poci naopako
# 1. exception/izuzetak->python baci gresku, program stane i dobijemo neki izuzetak npr. KeyError, TypeError,ValueError,ZeroDivisionError itd...
# 2. pogresna vrednost->program NE PADA! ali vaca pogresan rezulat, testira se "normalnim assertom" kao sto je bilo na pocetku, tj proveravaju se ocekivane vrrednosti

# Testiranje na greske je jako vazno jer greska koja se desi na pogresnom mestu je bug. Ako neka funkcija TREBA da baci ValueError kada npr dobije negativan broj a NE baci nista->to je problem, i to se treba proveriti i uhvatiti testom!