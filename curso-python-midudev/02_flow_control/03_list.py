###
# 03 - Listas
# Secuencias mutables de elementos. Pueden contener cualquier tipo de dato.
# Se pueden modificar, añadir o eliminar elementos.
# Se declaran con corchetes []
# Se pueden crear listas vacías o listas con elementos.
# Se pueden crear listas con diferentes tipos de datos.
# Se pueden crear listas anidadas.
###

import os
os.system("clear")

# Crear una lista 
print('\nCrear una lista')
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ['manzanas', 'peras', 'naranjas'] # Lista de cadenas
lista3 = [1, 'manzanas', 2.5, True] # Lista de diferentes tipos de datos. Tipos mixtos

lista4 = [] # Lista vacía
lista_de_listas = [[1, 2, 3], [4, 5000, 6]] # Lista de listas
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz de 3x3

print('lista1:', lista1)
print('lista2:', lista2)
print('lista3:', lista3)
print('lista4:', lista4)
print('lista_de_listas:', lista_de_listas)
print('matrix:', matrix)

# Acceder a los elementos de una lista
print('\nAcceder a los elementos de una lista')
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[2])  # naranjas
print(lista2[-1]) # naranjas
print(lista2[-2]) # peras
print(lista2[-3]) # manzanas

print(lista_de_listas[1][1]) # 5000

# Slicing (rebanado de listas)

print('\nSlicing (rebanado)')
lista1 = [1, 2, 3, 4, 5] # quiero imprimir [2, 3, 4]
print(lista1[:]) # [1, 2, 3, 4, 5] Te hace una copia de la lista
print(lista1[1:4]) # [2, 3, 4]
print(lista1[1:])  # [2, 3, 4, 5]
print(lista1[:4])  # [1, 2, 3, 4]

# Hay más magias con el slicing. EL PASO
print(lista1[::2]) # [1, 3, 5] # Cada segundo elemento
print(lista1[::-1]) # [5, 4, 3, 2, 1] # Invertir la lista
print(lista1[1:4:2]) # [2, 4] # Cada segundo elemento de la rebanada.El tercer elemento es el paso
print(lista1[1:4:1]) # [2, 3, 4] # Cada elemento de la rebanada
print(lista1[1:4:3]) # [2] # Cada tercer elemento de la rebanada
print(lista1[1:4:-1]) # [] # No hay elementos

# Modificar elementos de una lista
print('\nModificar elementos de una lista')
lista2[0] = 'pomelo' # Reemplaza el elemento en la posició 0 de la lista
print(lista2)

lista1[0] = 100 # Reemplaza el elemento en la posició 0 de la lista
print(lista1) # [100, 2, 3, 4, 5]

# Concatenar. Añadir elementos a una lista
print('\nAñadir elementos a una lista')

lista1 = [1, 2, 3, 4, 5] # Lista de enteros
# Forma larga y menos eficiente
lista1 = lista1 + [6] # Añade el elemento 6 al final de la lista
print(lista1) # [1, 2, 3, 4, 5, 6]
lista1 = lista1 + [7] # Añade el elemento 7 al final de la lista
print(lista1) # [1, 2, 3, 4, 5, 6, 7]

# Forma corta y más eficiente
lista1 += [8] # Añade el elemento 8 al final de la lista
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8]


lista1.append(6) # Añade el elemento 6 al final de la lista
print(lista1) # [100, 2, 3, 4, 5, 6]
lista1.append(7) # Añade el elemento 7 al final de la lista
print(lista1) # [100, 2, 3, 4, 5, 6, 7]

# Recuperar la longitud de una lista
print('\nRecuperar la longitud de una lista')
print(lista1)
print(len(lista1)) # 7