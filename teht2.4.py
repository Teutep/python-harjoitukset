# Ohjelma pyytää kolme kokonaislukua, ja tulostaa niiden summan, tulon ja keskiarvon

#syötteet
Luku1 = int(input("Kerro ensimmäinen kokonaisluku?: "))
Luku2 = int(input("Kerro toinen kokonaisluku: "))
Luku3 = int(input("Kerro kolmas kokonaisluku: "))

#laskujärjestys
Summa = (Luku1+Luku2+Luku3)
Tulo = (Luku1*Luku2*Luku3)
Keskiarvo = (Summa/3)

#tulostus
print(f"Suorakulmion summa on: {Summa}")
print(f"Suorakulmion tulo on: {Tulo}")
print(f"Suorakulmion keskiarvo on: {Keskiarvo}")