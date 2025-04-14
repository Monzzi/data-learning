###
# 01- Bucles while
# Permiten ejecutar un bloque de código mientras una condición sea verdadera.
###

import os

os.system("clear")

# # Bucle con una simple condición
# contador = 0

# while contador < 5:
#     print(contador)
#     contador += 1  # Super importante, si no se pone, el bucle se ejecuta infinitamente

# # Utilizamos la palabra break para salir del bucle.
# print("\nBucle con break")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break  # Salimos del bucle cuando contador es igual a 3

# # continue, que lo hace es saltaresa iteración en concreto
# # y continuar con el bucle

# print("\nBucle con continue")
# contador = 0
# while contador < 10:
#     contador += 1

#     if contador % 2 == 0:
#         continue
#     print(contador)  # Imprime solo los números impares


# # else, esta condición cuándo se ejecuta??
# print("\nBucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# else:
#     print("El bucle ha terminado")

# # else, esta condición cuándo se ejecuta??
# print("\nBucle while con else")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     break   # si se pone break, el else no se ejecuta
# else: # interesante cuando te quieres asegurar que el bucle ha terminado
#     print("El bucle ha terminado")

# pedir al usuario un número positvo, si no lo es, volver a pedirlo
# numero = -1
# while numero < 0:
#     numero = int(input("Introduce un número positivo: "))
#     if numero < 0:
#         print("El número no es positivo, vuelve a intentarlo")
    
#     print(f"El número {numero} es positivo")


numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
            print("El número no es positivo, vuelve a intentarlo")
    except:
        print("Debes introducir un número, si no peta!!")

print(f"El número {numero} es positivo")