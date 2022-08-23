# Yksi leiviskä on 20 naulaa
# Yksi naula on 32 luotia
# Yksi luoti on 13.3 grammaa
# Näin ollen gramma arvot jokaisella on
# Jos leiviskä on X, naula on Y ja luoti on Z
# Y = 32z ja X = 20*32z
# Jos 3 leiviskää, 9 naulaa, 13.5 luotia
# = 13.5z + 9*32z + 3*20*32z
# Muista math.floor

import math
#Kyselyt
LeiviskätLkm = float(input("Anna leiviskät: "))
NaulatLkm = float(input("Anna naulat: "))
LuoditLkm = float(input("Anna luodit: "))

#Laskutoimitukset
Gramma = 13.3
NaulatArvo = 32*Gramma
LeiviskätArvo = 20*NaulatArvo
LuoditGram = LuoditLkm*Gramma
NaulatGram = NaulatLkm*NaulatArvo
LeiviskätGram = LeiviskätLkm*LeiviskätArvo
Yhteensä = LuoditGram + NaulatGram + LeiviskätGram

Kilogramma = Yhteensä/1000
Loput = Yhteensä-math.floor(Kilogramma)*1000

#Vastaus
print(f"Massa nykymittojen mukaan: {math.floor(Kilogramma)} kilogrammaa ja {Loput:0.2f} grammaa")