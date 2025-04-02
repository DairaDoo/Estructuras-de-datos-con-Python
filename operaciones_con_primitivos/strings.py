#STRING

x = "Cake"
y = "Cookie"


# multiplicando una string por dos
print(x * 2)

#concatenando dos strings
print(x + ' & ' + y)

# Range Slicing
z1 = x[2:] # z1 = x[2:4]
print(z1)

#Slicing
z2 = y[0] + y[3] # piensa en los index de ese string.

print(z2)

# añadir mayúsculas
print(str.capitalize('cookie'))
print('cookie'.title())
print('cookie'.capitalize())

# obtener longitud de una cadena (string)
str1 = "Cake 4 U"
str2 = "404"
print(len(str1))
print(len('text'))

# comprobar si la cadena esta formada por dígitos (si la cadena solo tiene numeros)
print(str1.isdigit())

# esta es cierta por que la cadena si tiene solo números
print(str2.isdigit())

# sustituir partes de cadenas por otras cadenas
print(str1.replace('4 U', str2))

# devuelve 3 por que el kie comienza ahí
str3 = 'cookie'
str4 = 'kie'
print(str3.find(str4))

