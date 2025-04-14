nombre = "Monzzi"
edad = 50
es_en_practicas = True

tecnologias = ["HTML", "CSS", "JavaScript", "React", "Node", "Express", "PostgreSQL"]

perfil = {
    "nombre": nombre,
    "edad": edad,
    "en_practicas": es_en_practicas,
    "tecnologias": tecnologias
}

print("👩‍💻 Perfil de desarrolladora:")
print(f"Nombre: {perfil['nombre']}")
print(f"Edad: {perfil['edad']}")
print(f"¿Está en prácticas?: {perfil['en_practicas']}")
print("Tecnologías que domina:")
for tech in perfil["tecnologias"]:
    print(f" - {tech}")

def mostrar_tecnologias(lista):
    print("🚀 Estoy aprendiendo estas tecnologías:")
    for tech in lista:
        print(f"📘 {tech}")

mostrar_tecnologias(tecnologias)
