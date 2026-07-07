import os

# Función para asegurar que existan los archivos necesarios
def inicializar_archivos():
    archivos = ["cursos.txt", "estudiantes.txt", "inscripciones.txt"]
    for archivo in archivos:
        if not os.path.exists(archivo):
            with open(archivo, "w") as f:
                pass # Crea el archivo vacío si no existe

# Carga de cursos de prueba para no arrancar con el archivo vacío
def cargar_cursos_prueba():
    try:
        with open("cursos.txt", "r") as archivo:
            contenido = archivo.read()
        
        # Si no hay contenido, agregamos cursos usando el modo 'a' (append)
        if len(contenido) == 0:
            with open("cursos.txt", "a") as archivo:
                archivo.write("101,Python para Sistemas de Información,20,0\n")
                archivo.write("102,Lógica y Algoritmos,15,0\n")
    except FileNotFoundError:
        print("El archivo no existe aún.")

# Funciones de la Fase 2
def registrar_estudiante():
    """Registra un nuevo estudiante validando que los datos no estén vacíos."""
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    dni = input("Ingrese DNI: ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    email = input("Ingrese Email: ")
    
    # Validación básica (Estructura condicional)
    if len(dni) == 0 or len(nombre) == 0:
        print("¡Error! El DNI y el Nombre son obligatorios.")
        return # Cortamos la ejecución de la función anticipadamente

    # Persistencia en archivo (modo 'a' para no borrar lo anterior)
    with open("estudiantes.txt", "a") as archivo:
        archivo.write(f"{dni},{nombre},{apellido},{email}\n")
    
    print("¡Estudiante registrado con éxito!")

def listar_cursos():
    """Lee el archivo de cursos y muestra su contenido formateado."""
    print("\n--- LISTADO DE CURSOS ---")
    try:
        with open("cursos.txt", "r") as archivo:
            lineas = archivo.readlines()
            
            if len(lineas) == 0:
                print("Aún no hay cursos cargados.")
            else:
                print("ID  | Curso | Cupo Total | Inscriptos")
                print("-" * 45)
                # Estructura repetitiva para recorrer las líneas
                for linea in lineas:
                    datos = linea.strip().split(",")
                    print(f"{datos[0]} | {datos[1]} | {datos[2]} | {datos[3]}")
                    
    except FileNotFoundError:
        print("Error: El archivo de cursos no existe.")

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
    cargar_cursos_prueba() # Llamamos a la carga de prueba al iniciar
    ejecutando = True
    
    while ejecutando:
        opcion = mostrar_menu()
        
        if opcion == "1":
            listar_cursos()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            print("Saliendo del sistema...")
            ejecutando = False
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()