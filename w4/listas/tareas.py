'''
Gestor de tareas (TODO list)
[
    [false, "Titulo1", "Descripcion1"],
    [false, "Titulo2", "Descripcion2"],
    [true, "Titulo3", "Descripcion3"],
]
'''

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
        if tarea[0] is True:
            estado = "[x]"
        else:
            estado = "[ ]"
            
        print(f"- {estado} {tarea[1]}\n{tarea[2]}")
        print("\n")

def pedir_tarea() -> list:
    titulo = input("Indique el titulo de la tarea: ")
    descripcion = input("Indique la descripcion de la tarea: ")
    return [False, titulo, descripcion]


def agregar(tareas: list):
    tarea = pedir_tarea()
    tareas.append(tarea)    


def completar(tareas: list):
    try:
        posicion = int(input("Indique la posicion de la tarea: "))

        if posicion < 0:
            raise IndexError
        
        tareas[posicion][0] = True
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
    [False, "Examen", "Realizar cuestionario 1.2"],
    [False, "Cocinar", "Cocinar la cena hoy"],
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