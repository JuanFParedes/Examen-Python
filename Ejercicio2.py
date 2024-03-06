import sys

print("""
      INGRESE SU INFORMACION PERSONAL
      1. id
      2. nombres
      3. apellidos
      4. ubicación:
            dirección
            ciudad
            longitud
            latitud
      5. email
      6. edad
      7. ocupación
      """)
info = {}
Id = int(input("Ingrese su indetificacion: "))
nombres = str(input("Ingrese sus nombre/s: "))
apellidos = str(input("Ingrese sus apellidos: "))
print("Ingrese si ubicacion, esta se conforma de la direccion, ciudad, longitud y latitud: ")
direccion = str(input("Ingrese la direccion de su casa: "))
ciudad = str(input("Ingrese la ciudad de su residencia: "))
longitud = input("Ingrese la longitud de la ubicacion: ")
latitud = input("Ingrese la latitud de la ubicacion: ")


info = {
    "Id":Id,
    "nombres":nombres,
    "apellidos":apellidos,
    "ubicacion":{
        "direccion":direccion,
        "ciudad":ciudad,
        "longitud":longitud,
        "latitud":latitud
    }
}
info.update({id:info})
print(info)
