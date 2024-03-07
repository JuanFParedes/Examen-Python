import os
import json

def ClearScreen():
    os.system("cls")

def CheckFile():
    app_files = (os.path.isfile("Ejercicio4/data/Empleados.json") and os.path.isfile("Ejercicio4/data/Pagos.json") )
    if os.path.isdir("Ejercicio4/data") and app_files:
        pass
    else:
        os.system("mkdir Ejercicio4/data/")
        with open("Ejercicio4/data/Empleados.json", "w") as file:
            json.dump({}, file, indent=4)
        with open("Ejercicio4/data/Pagos.json", "w") as file:
            json.dump({}, file, indent=4)

def LoadFile(Archivo:str):
    with open("Ejercicio4/data/"+ Archivo, "r") as file:
        return json.load(file)

def UpdateFile(data:dict, Archivo:str):
    with open("Ejercicio4/data/"+Archivo, "w+") as file:
        json.dump(data, file, indent=4)