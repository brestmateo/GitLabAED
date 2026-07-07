import os

# Función para asegurar que existan los archivos necesarios
def inicializar_archivos():
    archivos = ["cursos.txt", "estudiantes.txt", "inscripciones.txt"]
    for archivo in archivos:
        if not os.path.exists(archivo):
            with open(archivo, "w") as f:
                pass # Crea el archivo vacío si no existe

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- SISTEMA DE INSCRIPCIÓN ---")
    print("1. Ver Cursos")
    print("2. Registrar Estudiante")
    print("3. Salir")
    return input("Seleccione una opción: ")

# Bloque principal
def main():
    inicializar_archivos()
    ejecutando = True
    
    while ejecutando:
        opcion = mostrar_menu()
        
        if opcion == "1":
            print("Mostrando cursos...")
            # Aquí llamaremos a la función listar_cursos() en la Fase 2
        elif opcion == "2":
            print("Registrando estudiante...")
            # Aquí llamaremos a la función registrar_estudiante() en la Fase 2
        elif opcion == "3":
            print("Saliendo del sistema...")
            ejecutando = False
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()