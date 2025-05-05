###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para realizar tareas específicas.
###


""" Definición de una funcion

def nombre_de_la_funcion(parametro1, parametro2, ...):
 # docstring
 # cuerpo de la funcion
 return valor_de_retorno # Opcional

"""

# Ejempplo de una función para imprimir algo en consola
def imprimir_mensaje():
    """ Esta función imprime un mensaje en consola """
    print("Hola, soy una función")
# Llamada a la función
imprimir_mensaje()

# Ejemplo de un afunción con parámter (el parámetro es lo que acpeta la función).
def saludar_a(nombre):
    print(f"Hola, {nombre}")

# Llamada a la función con diferentes argumentos. El argumeno es el valor que se le pasa al parámetro.
saludar_a("Juan")
saludar_a("María")
saludar_a("Pedro")

# Funciones con múltiples parámetros
def sumar(a, b):
    suma = a + b
    return suma
print(sumar(5, 3)) # Imprime 8

# Documnetar funcione con docstring

def restar(a, b):
    """ Esta función resta dos números y devuelve el resultado """
    return a - b 

print(restar.__doc__)

# parámetros por defecto
def multiplicar(a, b=1):
    """ Esta función multiplica dos números. El segundo número es opcional y por defecto es 1 """
    return a * b
print(multiplicar(5)) # Imprime 5

# parámetros posicionales
def describir_persona(nombre, edad, ciudad):
    """ Esta función describe a una persona """
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
# Llamada a la función con parámetros posicionales
describir_persona("Juan", 30, "Madrid")
describir_persona("Madrid", "Paco", 30) # El orden de los parámetros importa

# Argumentos por palabra clave
# parámetros nombrados
describir_persona(edad=30, ciudad="Madrid", nombre="Juan") # Se pueden cambiar el orden de los parámetros

# Argumneot sde longitud de variable (*args)
def sumar_varios_numeros(*args):
    """ Esta función suma varios números """
    suma = 0
    for numero in args:
        suma += numero
    return suma
print(sumar_varios_numeros(1, 2, 3, 4, 5)) # Imprime 15
print(sumar_varios_numeros(1, 2, 3)) # Imprime 6
print(sumar_varios_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Imprime 55


# Argumento de clave - valor variable (**kwargs)
def describir_persona(**kwargs):
    """ Esta función describe a una persona """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
# Llamada a la función con argumentos de clave - valor
describir_persona(nombre="Juan", edad=30, ciudad="Madrid", profesion="Ingeniero")
describir_persona(nombre="Juan", edad=30, ciudad="Madrid", profesion="Ingeniero", pais="España")
describir_persona(nombre="Pilot", edad=30, profesion="Ingeniero", pais="España", ciudad="Madrid")