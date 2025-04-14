###
# 02- Booleans
# Valores lógicos: True, False
# Fundamentales para el control de fluho y la lógica de programación.
###


import os

os.system("clear")


print("\nValores booleanos básicos:")

print(True)
print(False)

# Operadorsde comparación: devuelven un valor booleano

print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 5:", 5 == 5)  # True igualdad.
print("5 != 5:", 5 != 5)  # False no igualdad.
print("5 >= 5:", 5 >= 5)  # True mayor o igual
print("5 <= 5:", 5 <= 5)  # False menor o igual

print("\nComparación de strings:\n")  # en py son lexico-graficas.
print(
    "manzana < pera:", "manzana" < "pera"
)  # True lo compara por las letras dle alfabeto
print("hola" == "hola")  # True
print("hola" == "HOLA")  # False no es case sensitive

# Operadores de lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True", True and True)
print("True and False", True and False)
print("False and True", False and True)
print("False and False", False and False)
print("True or True", True or True)
print("True or False", True or False)
print("False or True", False or True)
print("False or False", False or False)
print("not True", not True)
print("not False", not False)


# Tablas de la verdad (para referencia):
print("\nTablas de la verdad:")
print("and:")
print("A     B     A and B")
print("True  True   True")
print("True  False  False")
print("False True   False")
print("False False  False")

print("\nor:")
print("A     B     A or B")
print("True  True   True")
print("True  False  True")
print("False True   True")
print("False False  False")

print("\nnot:")
print("A     not A")
print("True", not True)
print("False", not False)

numero = 5
if numero:
    print("El número no es cero")

numero = 0
if numero:
    print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
    print("La cadena no está vacia")

nombre = ""
if nombre:
    print("Aquí no entra. La cadena vacia es false")


numero = 3  # asignación
es_el_tres = numero == 3  # comparación

if es_el_tres:
    print("El número es 3")

# Comparación ternaria muy bonita en py
print('\nLa condición ternaria')
# Es una forma concisa de hacer un if-else. en una linea de código
# [código si cumple la condición] if [condición] else [codigo si no cumple la condición
edad = 17
mensaje = 'Eres mayor de edad' if edad >= 18 else 'Eres menor de edad'
print(mensaje)

