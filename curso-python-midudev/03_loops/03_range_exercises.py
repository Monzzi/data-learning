###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
nums = range(1, 11) # range(1, 11) crea una secuencia de números del 1 al 10 (11 no incluido)
for num in nums: # Recorre la secuencia de números del 1 al 10
    print(num) # Imprime cada número de la secuencia

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
nums = range(1, 21) # range(1, 21) crea una secuencia de números del 1 al 20 (21 no incluido)
for num in nums: # Recorre la secuencia de números del 1 al 20
    if num % 2 != 0: # Verifica si el número es impar
        print(num) # Imprime el número impar

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
nums = range(5, 51) # range(5, 51) crea una secuencia de números del 5 al 50 (51 no incluido)
for num in nums: # Recorre la secuencia de números del 5 al 50
    if num % 5 == 0: # Verifica si el número es múltiplo de 5
        print(num) # Imprime el número múltiplo de 5

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
nums = range(10, 0, -1) # range(10, 0, -1) crea una secuencia de números del 10 al 1 (0 no incluido) con un paso de -1
for num in nums: # Recorre la secuencia de números del 10 al 1
    print(num) # Imprime cada número de la secuencia en orden inverso

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma = 0 # Inicializa la variable suma en 0
nums = range(1, 101) # range(1, 101) crea una secuencia de números del 1 al 100 (101 no incluido)
for num in nums: # Recorre la secuencia de números del 1 al 100
    suma += num # Suma el número a la variable suma
print(f"La suma de los números del 1 al 100 es: {suma}")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero = int(input("Introduce un número para ver su tabla de multiplicar: ")) # Pide al usuario que introduzca un número
print(f"Tabla de multiplicar del {numero}:") # Imprime el encabezado de la tabla
for i in range(1, 11): # range(1, 11) crea una secuencia de números del 1 al 10 (11 no incluido)
    resultado = numero * i # Calcula el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}") # Imprime la tabla de multiplicar