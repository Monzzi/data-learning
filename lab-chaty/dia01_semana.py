semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
tecnologias = ["HTML", "CSS", "JavaScript", "React", "Node", "Express", "PostgreSQL"]

# mi propuesta ayuda copilot o codeium

def mostrar_planSemanal(lista):
    for dia in semana:
        print(f"El {dia} voy a estudiar {tecnologias[semana.index(dia)]}")


# propuesta 2
for i, dia in enumerate(semana):
    print(f"El {dia} voy a estudiar {tecnologias[i]}")


# propuesta 3
plan_semanal = zip(semana, tecnologias)

for dia, tech in plan_semanal:
    print(f"El {dia} voy a estudiar {tech}")

mostrar_planSemanal(semana)
