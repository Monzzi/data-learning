###
# EJERCICIOS
###

import os

os.system("clear")

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

nuevo_mensaje = mensaje[
    7:
]  # Extrae los elementos de la lista desde el índice 7 hasta el final
print(mensaje)  # Imprime la lista original
print(nuevo_mensaje)  # Imprime la nueva lista


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = (
    numeros[-1],
    numeros[0],
)  # Intercambia el primer y último elemento
print(numeros)  # Imprime la lista después del intercambio

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sandwich = pan + ingredientes + pan_abajo  # Concatenación de listas
print(sandwich)  # Imprime la lista del sándwich

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

nueva_lista = lista * 2  # Duplica la lista
nueva_lista2 = lista + lista  # Otra forma de duplicar la lista
nueva_list3a3 = lista[:3] + lista[:3]  # Otra forma de duplicar la lista
print(nueva_lista)  # Imprime la lista duplicada
print(nueva_lista2)  # Imprime la lista duplicada
print(nueva_list3a3)  # Imprime la lista duplicada


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista_centro = [10, 20, 30, 40, 50, 60, 70]
centro = lista_centro[len(lista_centro) // 2]  # Extrae el elemento central
print(centro)



# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista_reversa = [1, 2, 3, 4, 5, 6]
mitad = len(lista_reversa) // 2  # Encuentra la mitad de la lista
primera_mitad = lista_reversa[:mitad][::-1]  # Invierte la primera mitad
segunda_mitad = lista_reversa[mitad:]  # Mantiene la segunda mitad
lista_final = primera_mitad + segunda_mitad  # Combina ambas mitades
print(lista_final)  # Imprime la lista con la primera mitad invertida
