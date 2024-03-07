from modulos.corefiles import CheckFile, ClearScreen, LoadFile
from modulos.Empleados import AñadirEmpleado
from modulos.Pagos import AñadirPago, ReportePagos
from tabulate import tabulate
import sys

def mainMenu():
    ClearScreen()
    CheckFile()
    Empleados = LoadFile("Empleados.json")
    Pagos = LoadFile("Pagos.json")
    Titulo = """
    ++++++++++++++++++++++++
    +  JHOLVER ENTERPRISE  +
    ++++++++++++++++++++++++
    """
    print(Titulo)
    menu = [["1. Registrar empleado"],["2. Registrar pago"],["3. Colilla de pago"],["4. Salir"]]
    print(tabulate(menu, tablefmt="fancy_grid"))
    option = input("\n>> ")
    if option == "1":
        AñadirEmpleado(Empleados)
        mainMenu()
    elif option == "2":
        AñadirPago(Empleados, Pagos)
        mainMenu()
    elif option == "3":
        ReportePagos(Pagos)
        mainMenu()
    elif option == "4":
        sys.exit("Bye Bye")
    else:
        mainMenu()