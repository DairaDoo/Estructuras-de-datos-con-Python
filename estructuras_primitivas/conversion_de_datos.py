#conversión de tipos de datos

# imprimir el tipo de dato de una variable.
# i = 4.0
# print(type(i))

# i = int(i)
# print(type(i))

# i = str(i)
# print(type(i))

#Cuando cambias el tipo de una entidad de un tipo de datos a otro,
# esto se llama "encasillamiento". Puede haber dos tipos de conversiones
# de datos posibles: la implícita, denominada coerción, y la explícita, a menudo
# denominada fundición.

# Conversión ímplicita de tipos de datos (automática).

# float
# x = 4.0

# #int
# y = 2

# # Divido x entre y
# z = x/y

# print("Tipo de dato en z: ", type(z))


# CONVERSIÓN EXPLICITA DE DATOS

x = 2
y = "The Godfather Part "

# fav_movie = y + x < este da error, no se puede concatenar un entero con string
fav_movie = y + str(x)
print(fav_movie)
