"""
En Python, las matrices están soportadas por el módulo array
y es necesario importarlas antes de empezar a inicializarlas
y utilizarlas. Los elementos almacenados en una matriz están
limitados en su tipo de datos. El tipo de datos se especifica
durante la creación de la matriz y se especifica mediante un
código de tipo, que es un único carácter.
"""

import array as arr

# creamos matriz con enteros (I de Integer)
a = arr.array("I", [3, 5, 6])
print(f"Matriz de enteros: {a}")
print(f"Tipo de dato del array: {type(a)}")

a2 = arr.array("d", [2.3474, 2.51121, 10.2222])
print(f"Matriz de double: {a2}")
print(f"Tipo de dato del array: {type(a2)}")

bool_array = arr.array("b", [True, False, True, True, False])  # Se almacena como 1 y 0
# se puede usar el toList para convertir una matriz a una lista
print(f"Array de booleanos (convertidos a enteros): {bool_array.tolist()}")
print(f"Tipo de dato: {type(bool_array)}")
