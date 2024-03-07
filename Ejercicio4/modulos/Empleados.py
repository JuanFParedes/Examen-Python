from tabulate import tabulate
from modulos.corefiles import ClearScreen, UpdateFile


def Posicion():
    ClearScreen()
    Cargo = ""
    ClearScreen()
    cargos = [["1. Almacenista"],["2. Jefe It"],["3. Administrador"],["4. Mensajero"],["5 Gerente"]]
    print(tabulate(cargos, tablefmt="fancy_grid"))
    position = input("Seleccione el cargo: ")
    if position == "1":
        Cargo = "Almacenista"
    elif position == "2":
        Cargo = "Jefe It"
    elif position == "3":
        Cargo = "Administrador"
    elif position == "4":
        Cargo = "Mensajero"
    elif position == "5":
        Cargo = "Gerente"
    else:
        Posicion()
    return Cargo

def AñadirEmpleado(data:dict):
    try:
        print(data)
        id = int(input("Ingrese el id que se le asignara al empleado: "))
        if str(id) in data.keys():
            input("El id ya esta registrado")
        Nombre = str(input("Ingrese el nombre completo del trabajador: ")).capitalize()
        PrimerNombre = Nombre.split(" ")[0]
        Cargo = Posicion()
        PagoMensual = float(input(f"Cual es el pago mensual de {PrimerNombre}: "))
        dicc = {
            "Id": id,
            "Nombre": Nombre,
            "Posicion": Cargo,
            "Pago Mensual": PagoMensual
        }
        data.update({id: dicc})
        UpdateFile(data, "Empleados.json")
    except ValueError:
        input("Esta incorrecto")