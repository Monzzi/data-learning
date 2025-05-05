# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora


# Ejercicio 1: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando una función.
def imprimir_numeros_inverso(inicio, fin):
    for num in range(inicio, fin - 1, -1): # range(inicio, fin - 1, -1) crea una secuencia de números del inicio al fin en orden inverso
        print(num)
# Llamada a la función
imprimir_numeros_inverso(10, 1) # Imprime los números del 10 al 1 en orden inverso
imprimir_numeros_inverso(20, 1) 

# Ejercicio 2: suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando una función.
def sumar_numeros_rango(inicio, fin):
    suma = 0 # Inicializa la variable suma en 0
    for num in range(inicio, fin + 1): # range(inicio, fin + 1) crea una secuencia de números del inicio al fin (fin incluido)
        suma += num # Suma el número a la variable suma
    return suma # Devuelve la suma total
# Llamada a la función
resultado = sumar_numeros_rango(1, 100) # Llama a la función con el rango del 1 al 100
print(f"La suma de los números del 1 al 100 es: {resultado}") # Imprime el resultado de la suma

# Ejercicio 3: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando una función.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:") # Imprime el encabezado de la tabla
    for i in range(1, 11): # range(1, 11) crea una secuencia de números del 1 al 10 (11 no incluido)
        resultado = numero * i # Calcula el resultado de la multiplicación
        print(f"{numero} x {i} = {resultado}") # Imprime la tabla de multiplicar
# Llamada a la función
numero = int(input("Introduce un número para ver su tabla de multiplicar: ")) # Pide al usuario que introduzca un número
tabla_multiplicar(numero) # Llama a la función con el número introducido por el usuario

# Ejercicio 4: Imprimir números impares
# Imprime todos los números impares entre 1 y 20 (inclusive) usando una función.
def imprimir_numeros_impares(inicio, fin):
    for num in range(inicio, fin + 1): # range(inicio, fin + 1) crea una secuencia de números del inicio al fin (fin incluido)
        if num % 2 != 0: # Verifica si el número es impar
            print(num) # Imprime el número impar
# Llamada a la función
imprimir_numeros_impares(1, 20) # Imprime los números impares del 1 al 20

def imprimir_numeros_pares(primero, ultimo):
    for num in range(primero, ultimo + 1):
        if num % 2 == 0:
            print(num)
# Llamada a la función
imprimir_numeros_pares(1, 20) # Imprime los números pares del 1 al 20