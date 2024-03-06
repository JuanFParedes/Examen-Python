import os
import json
BASE_DATA="Ejercicio4/data/"
ruta = "Ejercicio4/data/Empleados.json"

def checkFile(Archivo,diccionario):
    if(not(os.path.isfile(BASE_DATA+Archivo))):
        with open (BASE_DATA+Archivo, "w+") as CreateFile:
            json.dump(diccionario, CreateFile, indent=4)
