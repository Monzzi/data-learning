###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# Ejercico 1
# num_1 = int(input("Introduce el primer número: "))
# num_2 = int(input("Introduce el segundo número: "))
# if num_1 > num_2:
#     print(f"{num_1} es mayor que {num_2}")
# elif num_1 < num_2:
#     print(f"{num_2} es mayor que {num_1}")
# else:
#     print(f"{num_1} y {num_2} son iguales")

# Ejercicio 2
# num_1 = float(input("Introduce el primer número: "))
# num_2 = float(input("Introduce el segundo número: "))
# operacion = input("Introduce la operación (+, -, *, /): ")
# if operacion == "+":
#     resultado = num_1 + num_2
# elif operacion == "-":
#     resultado = num_1 - num_2
# elif operacion == "*":
#     resultado = num_1 * num_2  
# elif operacion == "/":
#     if num_2 != 0:
#         resultado = num_1 / num_2
#     else:
#         resultado = "Error: División entre cero"
# else:
#     resultado = "Operación no válida"
# print(f"El resultado es: {resultado}")

# Ejercicio 3
# year = int(input("Introduce un año: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} es un año bisiesto")
# else:
#     print(f"{year} no es un año bisiesto")

# Ejercicio 4
edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad <= 2:
    print("Eres un bebé")
elif edad >= 3 and edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Edad no válida")

