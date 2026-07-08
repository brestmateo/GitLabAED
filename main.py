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
                archivo.write("103,Análisis Matemático I,30,0\n")
                archivo.write("104,Ingeniería y Sociedad,25,0\n")
                archivo.write("105,Inglés Avanzado,20,0\n")
                archivo.write("106,Arquitectura de Computadoras,25,0\n")
    except FileNotFoundError:
        print("¡Alerta! El archivo de cursos no existe aún. Se inicializará pronto.")

# Funciones de la Fase 2
def registrar_estudiante():
    """Registra un nuevo estudiante validando todos los datos."""
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    
    # 1. Validación de DNI: ciclo hasta que sea válido
    dni = input("Ingrese DNI (8 números): ")
    while len(dni) != 8 or not dni.isdigit():
        print("¡Error! El DNI debe contener exactamente 8 caracteres numéricos.")
        dni = input("Ingrese DNI (8 números): ")

    # 2. Validación extra: que no exista ya ese DNI registrado
    ya_existe = False
    if os.path.exists("estudiantes.txt"):
        with open("estudiantes.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) > 0 and datos[0] == dni:
                    ya_existe = True
                    break # Rompemos el ciclo porque ya lo encontramos
    
    if ya_existe:
        print("¡Alerta! Ese DNI ya se encuentra registrado en el sistema.")
        return # Cortamos la ejecución

    # 3. Validaciones de que los textos no estén vacíos con ciclos while
    nombre = input("Ingrese Nombre: ")
    while len(nombre) == 0:
        print("¡Error! El nombre es obligatorio.")
        nombre = input("Ingrese Nombre: ")

    apellido = input("Ingrese Apellido: ")
    while len(apellido) == 0:
        print("¡Error! El apellido es obligatorio.")
        apellido = input("Ingrese Apellido: ")

    email = input("Ingrese Email: ")
    while len(email) == 0:
        print("¡Error! El email es obligatorio.")
        email = input("Ingrese Email: ")
    
    # Persistencia en archivo
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
                print("¡Alerta! Aún no hay cursos cargados.")
            else:
                print("ID  | Curso | Cupo Total | Inscriptos")
                print("-" * 55)
                # Estructura repetitiva para recorrer las líneas
                for linea in lineas:
                    datos = linea.strip().split(",")
                    print(f"{datos[0]} | {datos[1]} | {datos[2]} | {datos[3]}")
                    
    except FileNotFoundError:
        print("¡Error crítico!: El archivo de cursos no se encuentra.")

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
    
    # Validación del DNI
    dni = input("Ingrese el DNI del estudiante (8 números): ")
    while len(dni) != 8 or not dni.isdigit():
        print("¡Error! El DNI debe contener exactamente 8 caracteres numéricos.")
        dni = input("Ingrese el DNI del estudiante (8 números): ")

    # 1. Verificar que el estudiante esté registrado primero
    estudiante_registrado = False
    if os.path.exists("estudiantes.txt"):
        with open("estudiantes.txt", "r") as f:
            for linea in f:
                datos_estudiante = linea.strip().split(",")
                if len(datos_estudiante) > 0 and datos_estudiante[0] == dni:
                    estudiante_registrado = True
                    break
    
    if not estudiante_registrado:
        print("¡Alerta! El estudiante con ese DNI no está registrado en el sistema. Vaya a la opción 2 primero.")
        return # Si no está, no lo dejamos avanzar

    # Validación del ID del curso
    id_curso = input("Ingrese el ID del curso: ")
    while len(id_curso) == 0:
        print("¡Error! El ID del curso no puede estar vacío.")
        id_curso = input("Ingrese el ID del curso: ")

    # 2. Verificar que no esté inscripto ya en ESE curso para evitar duplicados
    ya_inscripto = False
    if os.path.exists("inscripciones.txt"):
        with open("inscripciones.txt", "r") as f:
            for linea in f:
                datos_inscripcion = linea.strip().split(",")
                if len(datos_inscripcion) >= 2:
                    if datos_inscripcion[0] == dni and datos_inscripcion[1] == id_curso:
                        ya_inscripto = True
                        break

    if ya_inscripto:
        print("¡Alerta! Este estudiante ya se encuentra inscripto en este curso.")
        return

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
                
                # Actualizamos cupo actual
                curso[3] = str(cupo_actual + 1)
                print(f"¡Inscripción exitosa en {curso[1]}!")
            else:
                print("¡Alerta! Lo siento, el curso está lleno. No hay cupos disponibles.")
            break
            
    if not curso_encontrado:
        print("¡Alerta! Curso no encontrado. Verifique el ID ingresado.")
    else:
        # Guardamos los cambios en cursos.txt (reescribimos todo el archivo solo si se encontró el curso)
        with open("cursos.txt", "w") as f:
            for c in cursos:
                f.write(f"{c[0]},{c[1]},{c[2]},{c[3]}\n")      

def mostrar_estadisticas():
    """Calcula y muestra estadísticas de inscriptos."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    cursos = obtener_cursos()
    
    if not cursos:
        print("¡Alerta! No hay cursos cargados para analizar.")
        return

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
        print("\n¡Alerta! Aún no hay inscriptos en ningún curso.")          

def ver_estudiantes_por_curso():
    """Cruza datos de estudiantes e inscripciones para listar quién está en cada curso."""
    print("\n--- LISTADO DE INSCRIPTOS POR CURSO ---")
    
    # 1. Cargamos todos los estudiantes en un diccionario para poder buscar su nombre rápido
    estudiantes = {}
    if os.path.exists("estudiantes.txt"):
        with open("estudiantes.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) >= 3:
                    # Guardamos el DNI como clave y "Nombre Apellido" como valor
                    estudiantes[datos[0]] = f"{datos[1]} {datos[2]}"
    
    # 2. Leemos las inscripciones
    if not os.path.exists("inscripciones.txt"):
        print("¡Alerta! No hay inscripciones registradas.")
        return

    with open("inscripciones.txt", "r") as f:
        inscripciones = f.readlines()
        
    if not inscripciones:
        print("¡Alerta! No hay alumnos inscriptos aún.")
        return

    # 3. Recorremos las inscripciones y cruzamos la información
    for linea in inscripciones:
        datos_inscripcion = linea.strip().split(",")
        if len(datos_inscripcion) >= 2:
            dni = datos_inscripcion[0]
            id_curso = datos_inscripcion[1]
            # Buscamos el nombre en el diccionario, si no existe ponemos "Desconocido"
            nombre_alumno = estudiantes.get(dni, "Estudiante Desconocido")
            print(f"Curso ID: {id_curso} | Estudiante: {nombre_alumno} (DNI: {dni})")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- SISTEMA DE INSCRIPCIÓN ---")
    print("1. Ver Cursos")
    print("2. Registrar Estudiante")
    print("3. Inscribir Estudiante")
    print("4. Ver Estadísticas")
    print("5. Ver Inscriptos por Curso")
    print("6. Salir")
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
            ver_estudiantes_por_curso()
        elif opcion == "6":
            print("Saliendo del sistema...")
            ejecutando = False
        else:
            print("¡Error! Opción no válida, intente de nuevo con un número del 1 al 6.")

if __name__ == "__main__":
    main()