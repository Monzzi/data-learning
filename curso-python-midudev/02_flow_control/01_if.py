###
# 01- Sentencias condicionales (if, elif, else)
# Permite ejecutar un bloque de instrucciones si una condición se cumple.
# Tambien se conoce como estructura de control condicional.
###

import os
os.system("clear")

print("\n  Sentencia simple condicional\n ")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir")


print("\n  Sentencia condicional con else\n ")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir")
else:
    print("Eres menor de edad")
    print("No puedes conducir")

print("\n  Sentencia condicional con elif\n ")   

nota = 8.5

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspendido")

print("\n  Condicionales múltiples\n ") 

edad = 25
tiene_carnet = False

# && en js es and n python
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# || en js es or n python
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# ! en js es not n python
if not tiene_carnet:
    print("No tienes carnet")
else:
    print("Tienes carnet")

print("\n  Condicionales anidados\n ")
edad = 20
tiene_dinero = False

if edad >= 18:
    if tiene_dinero:
        print('Puedes entrar en la discoteca')
    else:
        print('Te quedas en casita')
else:
    print('Np puedes entrar en la discoteca')

# Más simplificado
# if edad < 18:
#    print('No puedes entrar en la discoteca')
# elif tiene_dinero:
#     print('Puedes entrar en la discoteca')
# else:
#     print('Te quedas en casita')