from collections import defaultdict


frases = [
    "el sol brilla en la playa",
    "la playa es hermosa",
    "me encanta la playa y el sol"
]

texto = " ".join(frases).lower().split()

conteo = defaultdict(int)

for palabra in texto:
    conteo[palabra] += 1

palabra_mas_repetida = max(conteo, key=conteo.get)
veces = conteo[palabra_mas_repetida]

print(f"La palabra más común es: {palabra_mas_repetida} con {veces} apariciones.")