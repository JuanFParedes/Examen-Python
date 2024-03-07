from corefiles import CheckFile, UpdateFile, ReadFile 
import sys

Producto={}
CheckFile("productos.json",Producto)
ReadFile("productos.json") 


Titulo="""
++++++++++++++++++++++++++++++
+  REGISTRO DE LOS PRODUCTOS +
++++++++++++++++++++++++++++++
    """
print(Titulo)


Tienda=True
while Tienda:
    id=float(input("Ingrese el id del producto "))
    Nombre=input("Ingrese el nombre del producto ")
    ValorUnitario=float(input("Ingrese el valor unitario del producto "))
    StockMin=float(input("Ingrese el stock minimo del producto "))
    StockMax=float(input(" Ingrese el stock maximo del producto "))

    Productos={
        'id':id,
        'Nombre':Nombre,
        'ValorUnitario':ValorUnitario,
        'Stockmin':StockMin,
        'Stockmax':StockMax,
        
    }
    Producto.update({id:Productos})
    UpdateFile("Ejercicio3/data/productos.json",Producto)
    Tienda=str(input('¿Desea agregar mas productos? S(si) ENTER(no)'))
if Tienda == "S":
    Tienda()
else:
    sys.exit    

    
print(Productos)