###
# 02- Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o un a lista.
###

print("\n)Bucles for:")

# Iterar una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa iterable

cadena = "Hola"
for letra in cadena:
    print(letra)

# enumerate()
frutas = ["manzana", "banana", "naranja"]
for ind, value in enumerate(frutas):
    print(f"El índice: {ind}, es el valor: {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break ÚTIL  para buscar un elemento
print("\n)break:")
animales = ["perro", "gato", "loro", "pez", "oso", "leon"]
for animal in animales:
    print(animal)
    if animal == "oso":
        break

nimales = ["perro", "gato", "loro", "pez", "oso", "leon"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "oso":
        print(f"El índice del oso es: {idx}")  # ejemplo sin break itera todo.

# continue
print("\ncontinue:")
animales = ["perro", "gato", "loro", "pez", "oso", "leon"]
for animal in animales:
    if animal == "oso":
        continue
    print(animal)

# Comprensión de listas (list comprehension)
print("\nComprensión de listas:")
animales = ["perro", "gato", "loro", "pez", "oso", "leon"]
animales_mayusculas = [animal.upper() for animal in animales] # algo parecido a un map. saca la lista en una linea y se asigna a una variable que es guay. 
print(animales_mayusculas)

# Comprensión de listas con condicionales
# Muestra los número pares
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

