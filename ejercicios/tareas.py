"""
Gestor de tareas (TODO list)
[
    {"estado": false, "titulo": "Titulo1", "descripcion": "Descripcion1"},
    {"estado": false, "titulo": "Titulo2", "descripcion": "Descripcion2"},
    {"estado": false, "titulo": "Titulo3", "descripcion": "Descripcion3"},
]
"""


def menu() -> str:
    print("Gestor de Tareas")
    print("1. Listar")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Completar tarea")
    print("5. Salir")
    opcion = input("Elija una opcion:")
    return opcion


def listar(tareas: list):
    if not tareas:
        print("** No hay tareas**\n\n")
        return

    for tarea in tareas:
        if tarea["estado"] is True:
            estado = "[x]"
        else:
            estado = "[ ]"

        print(f"- {estado} {tarea["titulo"]}\n{tarea["descripcion"]}")
        print("\n")


def pedir_tarea() -> list:
    titulo = input("Indique el titulo de la tarea: ")
    descripcion = input("Indique la descripcion de la tarea: ")

    # Forma 1
    # return {
    #     "estado": False,
    #     "titulo": titulo,
    #     "descripcion": descripcion,
    # }

    # Forma 2
    res = {}
    res["estado"] = False
    res["titulo"] = titulo
    res["descripcion"] = descripcion
    return res


def agregar(tareas: list):
    tarea = pedir_tarea()
    tareas.append(tarea)


def completar(tareas: list):
    try:
        palabra = input("Escriba una frase del titulo: ")
        # recorrer todas las tareas con un palabra similar en el titulo

        encontrados = [
            tarea["titulo"]
            for tarea in tareas
            if palabra.lower() in str(tarea["titulo"]).lower()
        ]

        print("Los titulos hallados son:")
        for pos, item in enumerate(encontrados):
            print(f"[{pos}] Titulo: {item}")

        posicion = int(input("Indique la posicion de la tarea: "))

        if posicion < 0:
            raise IndexError

        # En este punto deberiamos de tener el titulo de la tarea a completar
        titulo_a_completar = encontrados[posicion]

        for item in tareas:
            if item["titulo"] == titulo_a_completar:
                item["estado"] = True

    except (ValueError, IndexError):
        print("** Posicion invalida **\n\n")


def eliminar(tareas: list):
    try:
        posicion = int(input("Indique la posicion de la tarea: "))

        if posicion < 0:
            raise IndexError

        tareas.pop(posicion)
    except (ValueError, IndexError):
        print("** Posicion invalida **\n\n")


# Ejecucion principal

tareas = [
    {"estado": False, "titulo": "Examen", "descripcion": "Realizar cuestionario 1.2"},
    {"estado": False, "titulo": "Cocinar", "descripcion": "Cocinar la cena hoy"},
]
while True:
    opt = menu()

    match opt:
        case "1":
            listar(tareas)
        case "2":
            agregar(tareas)
        case "3":
            eliminar(tareas)
        case "4":
            completar(tareas)
    if opt == "5":
        break
