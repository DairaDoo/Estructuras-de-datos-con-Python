# Ejercicio: Comprimir una Lista de Strings
# Descripción:
# Dada una lista de strings, escribe una función en Python que agrupe las palabras que tienen las mismas letras (anágramas) y las almacene en una lista de listas.

# Ejemplo de entrada:

# python
# Copiar
# Editar
# palabras = ["roma", "amor", "mora", "perro", "ropa", "paro"]
# Salida esperada:

# python
# Copiar
# Editar
# [
#     ["roma", "amor", "mora"],
#     ["perro"],
#     ["ropa", "paro"]
# ]
# Las palabras que tienen las mismas letras deben agruparse en una sublista.

from collections import defaultdict


# # Prueba con un ejemplo
# palabras = ["roma", "amor", "mora", "perro", "ropa", "paro"]
# resultado = agrupar_anagramas(palabras)
# print(resultado)


# SORTED QUE HACE

# lista = []

# for nombre in ["roma", "amor", "mora", "perro", "ropa", "paro"]:
#     palabra_ordenada = sorted(nombre.lower())
#     lista.append(palabra_ordenada)
#     # print(palabra_ordenada)

# print(lista)

# JOIN

# lista_letras = ['a', 'm', 'o', 'r']
# palabra_unida = "".join(lista_letras)
# print(palabra_unida)


# palabra = 'papichulo'

# palabra_alfabetica = "".join(sorted(palabra.lower()))

# print(palabra_alfabetica)


# from collections import defaultdict

# grupos = defaultdict(list)

# palabras = ["roma", "amor", "mora", "perro", "ropa", "paro"]

# for palabra in palabras:
#     clave = "".join(sorted(palabra))  # Ordenamos las letras para usar como clave
#     grupos[clave].append(palabra)  # Guardamos la palabra original en esa clave

# print(grupos)

from collections import defaultdict

def agrupar_anagramas(palabras):
    grupos = defaultdict(list)  # Diccionario donde las claves serán las palabras ordenadas

    for palabra in palabras:
        clave = "".join(sorted(palabra.lower()))  # Ordenamos las letras de la palabra
        grupos[clave].append(palabra)  # Agregamos la palabra a su grupo

    return list(grupos.values())  # Convertimos los valores del diccionario en una lista de listas

# Prueba con un ejemplo
palabras = ["roma", "amor", "mora", "perro", "ropa", "paro"]
resultado = agrupar_anagramas(palabras)
print(resultado)



