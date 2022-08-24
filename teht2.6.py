# x = random.randint(0, 9)
# print(f"Kolminumeroinen koodi on: {x}")

import random
Numero = ""
for x in range(0,3):
    Numero += str(random.randint(0,9))
Numero2 = ""
for x in range(0,4):
    Numero2 += str(random.randint(1,6))

print(f"Kolminumeroinen luku: {Numero}")
print(f"Nelinumeroinen luku: {Numero2}")