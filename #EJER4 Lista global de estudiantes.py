estudiantes = []

# ==================== FUNCIONES DEL MENÚ ====================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    opcion = input("Seleccione una opción: ")
    if opcion.isnumeric() and 1 <= int(opcion) <= 6:
        return int(opcion)
    else:
        print("Opción no válida. Ingrese un número entre 1 y 6.")
        return 0

# ==================== FUNCIONES DE VALIDACIÓN ====================

def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_edad(edad):
    return edad.isnumeric() and int(edad) > 0

def validar_nota(nota):
    try:
        n = float(nota)
        return 1.0 <= n <= 7.0
    except:
        return False

# ==================== FUNCIONES DEL SISTEMA ====================

def agregar_estudiante(lista):
    print("\n--- AGREGAR ESTUDIANTE ---")

    nombre = input("Ingrese el nombre del estudiante: ")
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío.")
        return

    edad = input("Ingrese la edad del estudiante: ")
    if not validar_edad(edad):
        print("Error: la edad debe ser un número entero mayor a cero.")
        return

    nota = input("Ingrese la nota del estudiante (1.0 - 7.0): ")
    if not validar_nota(nota):
        print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    estudiante = {
        "nombre": nombre.strip(),
        "edad": int(edad),
        "nota": float(nota),
        "aprobado": False
    }

    lista.append(estudiante)
    print(f"Estudiante '{nombre.strip()}' agregado correctamente.")

def buscar_estudiante(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i
    return -1

def eliminar_estudiante(lista):
    print("\n--- ELIMINAR ESTUDIANTE ---")
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    posicion = buscar_estudiante(lista, nombre)

    if posicion != -1:
        lista.pop(posicion)
        print(f"Estudiante '{nombre}' eliminado correctamente.")
    else:
        print(f"El estudiante '{nombre}' no se encuentra registrado.")

def actualizar_estados(lista):
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False
    print("Estados actualizados correctamente.")

def mostrar_estudiantes(lista):
    print("\n=== LISTA DE ESTUDIANTES ===")

    if len(lista) == 0:
        print("No hay estudiantes registrados.")
        return

    actualizar_estados(lista)

    for estudiante in lista:
        if estudiante["aprobado"]:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad:   {estudiante['edad']}")
        print(f"Nota:   {estudiante['nota']}")
        print(f"Estado: {estado}")
        print("*" * 45)

# ==================== PROGRAMA PRINCIPAL ====================

opcion = 0

while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_estudiante(estudiantes)

    elif opcion == 2:
        print("\n--- BUSCAR ESTUDIANTE ---")
        nombre = input("Ingrese el nombre a buscar: ")
        posicion = buscar_estudiante(estudiantes, nombre)

        if posicion != -1:
            e = estudiantes[posicion]
            print(f"Estudiante encontrado en la posición {posicion}:")
            print(f"Nombre: {e['nombre']}")
            print(f"Edad:   {e['edad']}")
            print(f"Nota:   {e['nota']}")
            print(f"Aprobado: {e['aprobado']}")
        else:
            print(f"El estudiante '{nombre}' no se encuentra registrado.")

    elif opcion == 3:
        eliminar_estudiante(estudiantes)

    elif opcion == 4:
        actualizar_estados(estudiantes)

    elif opcion == 5:
        mostrar_estudiantes(estudiantes)

    elif opcion == 6:
        print("\nGracias por usar el sistema. Vuelva Pronto")