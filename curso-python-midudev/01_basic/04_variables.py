###
# 04- variables
# las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Para asignar una variables solo hace falta poner esto:


# my_name = 'Monzzi'
# # print(my_name)

# # # pueden reasignarse

# age = 32
# print(age)

# age = 40
# print(age)

# # Tipado dinámco: el tipo de dato que se determina en tiempo de ejecución
# # no tienes que declararlo explícitamente. (js también)

name = 'Monzzi'
print(type(name))

name = 50
print(type(name))

# Tipado fuerte:  Python no realiza conversiones de tipo autómaticas. JS es de de tipo débil, si lo hace

# print (10 + '2') # no convierte, da error. 

# f-string (literal de cadena de formato)
# print(f'Hola {my_name}, tengo {age +5} años')


# Forma no recomendada de asignar vairables. Varias en una linea
name, age, city = 'Monzzi', 50, 'Mollet'

# Convenciones de nombres de variables. No empezar con número ni palabras reservadas.  No tiene constantes aunque se pueden simular. 
mi_nombre_de_variable = 'sí' # snake_case
nombre ='Sí' 
mi_nombre_de_variable_123 = 'Sí'

MiNombreDeVariable = 'No' # Pascal_Case
ninombredevariable = 'No'  # todo junto no. 

# simular constantes
MI_COSNTANTE = 3.14 # en UPPER_CASE simula una constante, aunque pueda reasignarse.


is_user_logged_in: bool = True
print(is_user_logged_in)


# Hace estáticos los tipos. Te avisa el IDE, pero lo ejecuta. Es polémico,  
# is_user_logged_in = 42
# print(is_user_logged_in)

# name: str = 'Monzzi'


