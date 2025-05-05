"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# Monzzi
# def huevos_carnivoros(huevos):
#     suma = 0
#     for cantidad in huevos:
#         if cantidad % 2 == 0:
#             suma += cantidad

#     return suma 
# lista_de_huevos = [2, 3, 4, 10]
# print(huevos_carnivoros(lista_de_huevos))


# Midudev

def count_carnivore_dinosaur_eggs(egg_list) -> int:
  total_carnivore_eggs = 0

  for eggs in egg_list:
    if eggs % 2 == 0:
      total_carnivore_eggs += eggs

  return total_carnivore_eggs   

egg_list = [2, 3, 4, 10]
print(count_carnivore_dinosaur_eggs(egg_list))


