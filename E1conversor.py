import sys

print("""
    +++++++++++++++++++++++++++++++++
    ++    CONVERSOR DE DIVISAS     ++
    +++++++++++++++++++++++++++++++++
    
    1. Pesos(COP) a Dolares(USD)
    2. Pesos(COP) a Euros(EUR)
    3. Euros(EUR) a Pesos(COP) 
    4. Pesos(COP) a Yenes(JPY)
    
    """)

opcion = input("Seleccione una opcion del menu: ")
Valor = int(input("Ingrese la cantidad a convertir: "))

if opcion == "1":
    print(Valor)
    PesoADolares = Valor/3944
    print(f"El total de Dolares es de {PesoADolares}")
elif opcion == "2":
    print(Valor)
    PesoAEuros = Valor/4279
    print(f"El total de Euros es de {PesoAEuros}")
elif opcion == "3":
    print(Valor)
    EurosAPesos = Valor*4279
    print(f"El total de Pesos es de {EurosAPesos}")
elif opcion == "4":
    print(Valor)
    PesosAYenes = Valor/26.30
    print(f"El total de Yenes es de {PesosAYenes}")
else:
    sys.exit
    
      
    
    
    
    
