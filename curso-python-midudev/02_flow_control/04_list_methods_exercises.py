###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

import os
os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista1 = [1, 2, 3, 4, 5]
lista1.append(6)  # Añade el número 6 al final de la lista
lista1.insert(2, 10)  # Inserta el número 10 en la posición 2
lista1[0] = 0  # Modifica el primer elemento de la lista para que sea 0
print('Ejercicio 1:', lista1)  # Imprime la lista después de las modificaciones

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)  # Extiende lista_a con lista_b
lista_a.remove(1)  # Elimina la primera aparición del número 1 en lista_a
elemento_eliminado = lista_a.pop(3)  # Elimina el elemento en el índice 3 de lista_a    
print('Ejercicio 2:', lista_a)  # Imprime la lista luego de las modificaciones
print('Elemento eliminado:', elemento_eliminado)  # Imprime el elemento eliminado
lista_b.clear()  # Limpia completamente lista_b
print('Lista b después de limpiar:', lista_b)  # Imprime lista_b después de limpiar

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista3[2:4]  # Elimina los elementos desde el índice 2 hasta el 5 (sin incluir el 5)
print('Ejercicio 3:', lista3)  # Imprime la lista resultante


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista4 = [5, 2, 8, 1, 9, 4, 2]
lista4.sort()  # Ordena la lista de forma ascendente
print('Ejercicio 4:', lista4)  # Imprime la lista resultante
print('Cantidad de 2:', lista4.count(2))  # Cuenta cuántas veces aparece el número 2 en la lista
print('7 en la lista:', 7 in lista4)  # Comprueba si el número 7 está en la lista

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia_1 = original[:]  # Copia usando slicing
copia_2 = original.copy()  # Copia usando copy()
referencia = original  # Referencia a la lista original
referencia[0] = 10  # Modifica el primer elemento de la lista referencia
print('Ejercicio 5:')
print('Original:', original)  # Imprime la lista original
print('Copia 1:', copia_1)  # Imprime la copia 1
print('Copia 2:', copia_2)  # Imprime la copia 2
print('Referencia:', referencia)  # Imprime la referencia a la lista original

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

lista_strings = ["Manzana", "pera", "BANANA", "naranja"]
lista_strings.sort(key=str.lower)  # Ordena la lista sin diferenciar entre mayúsculas y minúsculas
print('Ejercicio 6:', lista_strings)  # Imprime la lista ordenada