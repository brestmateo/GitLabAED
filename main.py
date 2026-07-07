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
    print("3. Inscribir Estudiante")
    print("4. Ver Estadísticas")
    print("5. Salir")
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
            inscribir_estudiante()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            print("Saliendo del sistema...")
            ejecutando = False
        else:
            print("Opción no válida, intente de nuevo.")
def obtener_cursos():
    """Retorna una lista de cursos cargados desde el archivo."""
    cursos = []
    if os.path.exists("cursos.txt"):
        with open("cursos.txt", "r") as f:
            for linea in f:
                cursos.append(linea.strip().split(","))
    return cursos

def inscribir_estudiante():
    """Lógica para inscribir a un estudiante en un curso."""
    print("\n--- INSCRIPCIÓN A CURSO ---")
    dni = input("Ingrese el DNI del estudiante: ")
    id_curso = input("Ingrese el ID del curso: ")
    
    cursos = obtener_cursos()
    curso_encontrado = False
    
    # Buscamos el curso
    for curso in cursos:
        if curso[0] == id_curso:
            curso_encontrado = True
            cupo_total = int(curso[2])
            cupo_actual = int(curso[3])
            
            if cupo_actual < cupo_total:
                # Inscribimos: Guardamos en inscripciones.txt
                with open("inscripciones.txt", "a") as f:
                    f.write(f"{dni},{id_curso},Inscripto\n")
                
                # Actualizamos cupo actual (esto requiere reescribir el archivo)
                curso[3] = str(cupo_actual + 1)
                print(f"Inscripción exitosa en {curso[1]}.")
            else:
                print("Lo siento, el curso está lleno.")
            break
            
    if not curso_encontrado:
        print("Curso no encontrado.")

    # Guardamos los cambios en cursos.txt (reescribimos todo el archivo)
    with open("cursos.txt", "w") as f:
        for c in cursos:
            f.write(f"{c[0]},{c[1]},{c[2]},{c[3]}\n")      
def mostrar_estadisticas():
    """Calcula y muestra estadísticas de inscriptos."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    cursos = obtener_cursos()
    
    if not cursos:
        print("No hay cursos para analizar.")
        return

    # Variables para control de alta demanda
    max_inscriptos = -1
    curso_estrella = ""
    
    print("Reporte de Inscriptos:")
    for curso in cursos:
        nombre = curso[1]
        inscriptos = int(curso[3])
        print(f"- {nombre}: {inscriptos} inscriptos.")
        
        # Lógica de acumulador/comparación para hallar el máximo
        if inscriptos > max_inscriptos:
            max_inscriptos = inscriptos
            curso_estrella = nombre
            
    if max_inscriptos > 0:
        print(f"\nCurso con mayor demanda: {curso_estrella} ({max_inscriptos} inscriptos)")
    else:
        print("\nAún no hay inscriptos en ningún curso.")          

if __name__ == "__main__":
    main()