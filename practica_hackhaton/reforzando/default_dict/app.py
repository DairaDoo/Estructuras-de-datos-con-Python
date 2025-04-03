# from collections import defaultdict

# mi_diccionario = defaultdict(list)

# mi_diccionario["carro"].append("rojo")
# mi_diccionario["carro"].append("azul")

# print(mi_diccionario)

# conteo = defaultdict(int)

# palabras =  ["rojo", "azul", "rojo", "verde", "azul", "azul"]

# for palabra in palabras:
#     conteo[palabra] += 1

# print(conteo)

from collections import defaultdict

palabras = ["manzana", "mango", "pera", "papaya", "fresa", "frambuesa"]

palabras_agrupadas = defaultdict(list)

for palabra in palabras:
    palabras_agrupadas[palabra[0]].append(palabra)

print(dict(palabras_agrupadas))
