###
# 05 - Entrada de usuario (input()) - versión simplificada
# La función input() permite obtener datos del susario a través de la consola.
###

nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de saludarte")
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")
print("Obtener múltiples valores ala vez")
country, city = input("¿En qué país y ciudad vives?\n").split()
print(f"Vives en {country}, {city}")
