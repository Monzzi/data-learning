###
# 03 - range()
# Permite crear una secuencia de números. Puede ser utilizada en un bucle for, pero no solo para eso. 
###

print("\nrange():")

# nums = range(5) # range(5) crea una secuencia de números del 0 al 4 (5 no incluido) Por defecto el primer parámetro es 0.
# print(nums) # Imprime el objeto no la lista. 

# for num in range(5): 
#     print(num) # Imprime la secuencia de  números del 0 al 4.

# range(inicio, fin)  
for num in range(1, 10): # range(1, 10) crea una secuencia de números del 1 al 9 (10 no incluido)
    print(num) # Imprime la secuencia de números del 1 al 9. 


# range(inicio, fin, paso)
for num in range(1, 10, 2): # range(1, 10, 2) crea una secuencia de números del 1 al 9 (10 no incluido) con un paso de 2.
    print(num) # Imprime la secuencia de números del 1 al 9 con un paso de 2.

for num in range(-5, 0): # range(-5, 0) crea una secuencia de números del -5 al -1 (0 no incluido)
    print(num) # Imprime la secuencia de números del -5 al -1.
# range(inicio, fin, paso negativo)
for num in range(5, 0, -1): # range(5, 0, -1) crea una secuencia de números del 5 al 1 (0 no incluido) con un paso de -1.
    print(num) # Imprime la secuencia de números del 5 al 1.
# range(inicio, fin, paso negativo)
for num in range(5, -1, -1): # range(5, -1, -1) crea una secuencia de números del 5 al 0 (-1 no incluido) con un paso de -1.
    print(num) # Imprime la secuencia de números del 5 al 0.

# rango para listas
nums = range(10) # range(5) crea una secuencia de números del 0 al 4 (5 no incluido)
print(list(nums)) # Imprime la lista de números del 0 al 9.

# para repetir un bloque de código un número determinado de veces
# l

# Mejor así las repeticiones de acciones
for _ in range(5): # Repite el bloque de código 5 veces
    print("Hola") # Imprime Hola