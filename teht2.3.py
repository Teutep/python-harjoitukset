# Tämä ohjelma tulostaa suorakulmion piirin ja pinta-alan
# jahka ohjelma tietää suorakulmion kannan ja korkeuden

Kanta = float(input("Mikä on suorakulmion leveys senttimetreinä?: "))
Korkeus = float(input("Mikä on suorakulmion korkeus senttimetreinä?: "))
Ala = (Kanta*Korkeus)
Piiri = (Kanta*2) + (Korkeus*2)

print(f"Suorakulmion pinta-ala on: {Ala}cm^2")
print(f"Suorakulmion piiri on: {Piiri}cm")
