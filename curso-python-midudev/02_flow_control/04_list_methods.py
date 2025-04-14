###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas son:
###

import os
os.system("cls" if os.name == "nt" else "clear")

lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos en una lista
lista1.append('e')  # Agrega un elemento al final de la lista
print(lista1)

lista1.insert(1, '@')
print(lista1)  # Agrega un elemento en la posición 1 de la lista

lista1.extend(['f', 'g', 'h'])  # Agrega varios elementos al final de la lista
print(lista1)

# Eliminar elementos de una lista
lista1.remove('@')  # Elimina el primer elemento que coincide con el valor '@'
print(lista1)

  
ultimo = lista1.pop()  # Elimina y devuelve el último elemento de la lista
print(ultimo)  # Imprime el elemento eliminado
print(lista1)  # Imprime la lista después de eliminar el último elemento 

lista1.pop(1)  # Elimina el elemento en la posición 1 de la lista
print(lista1)  # Imprime la lista después de eliminar el elemento en la posición 1

del lista1[-1]  # Eliminar por lo bestia. aquí el útlimo
print(lista1)  # Imprime la lista después de eliminar el último elemento

# Eliminar un rango de elementos.

del lista1[1:3]  # Elimina los elementos en las posiciones 1 a 2 (sin incluir la posición 3)

lista1.clear()  # Elimina todos los elementos de la lista
print(lista1)  # Imprime la lista después de eliminar todos los elementos

# Más métodos útiles
print('Ordenar listas mofificando la original')
numbers = [3, 10, 2, 99, 101, 0]
numbers.sort()  # Ordena la lista en orden ascendente. Ojo la modifica NO la deveulve. 
print(numbers)

# si queremos guardarla creando una nueva lista
print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 99, 101, 0]
sorted_numbers = sorted(numbers)  # Ordena la lista en orden ascendente y crea una nueva lista
print(sorted_numbers)  # Imprime la nueva lista ordenada 

print('Ordenar una lista de strings (todo minúscula)')
frutas =['apple', 'banana', 'cherry', 'date']
sorted_frutas = sorted(frutas)  # Ordena la lista de frutas en orden alfabético
print(sorted_frutas)  # Imprime la nueva lista ordenada

print('Ordenar una lista de strings (mezclas con mayúscula y minúscula)')
frutas =['apple', 'Banana', 'cherry', 'Date']
sorted_frutas = sorted(frutas)  # Ordena la lista de frutas en orden alfabético
print(sorted_frutas)  # Imprime la nueva lista ordenada
#para areeglar esto y que no se vea raro, podemos usar el método lower() para convertir todas las cadenas a minúsculas antes de ordenarlas
frutas =['apple', 'Banana', 'cherry', 'Date']
frutas.sort(key=str.lower)  # Ordena la lista de frutas en orden alfabético ignorando mayúsculas y minúsculas
print(frutas)  # Imprime la lista ordenada


# Más cositas útiles
animals = ['dog', 'cat', 'elephant', 'cat', 'tiger']
print(len(animals))
print(animals.count('cat')) 
print('dog' in animals) #comprobar si un elemento está en la lista
print('lion' in animals) #comprobar si un elemento está en la lista