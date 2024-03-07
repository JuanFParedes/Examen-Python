from modulos.corefiles import UpdateFile
import json

def ObtenerEmpleado(data_empleado:dict):
    try:
        id = input("Ingrese el id del empleado a pagar: ")
        for key, value in data_empleado.items():
            if key == id:
                return value
    except:
        input("El id ingresado no es valido")

def AñadirPago(data_empleado:dict, data_pagos:dict):
    try:
        Mes = input("En que mes se esta generando el pago? ")
        Fecha = input("Cual es la fecha en la que se  esta generando el pago? Dia, Mes, Año ")
        Empleado = ObtenerEmpleado(data_empleado)
        DiasTrabajo = int(input("Ingrese los días de trabajo: "))
        HorasExtra = int(input("Ingrese las horas extras realizadas: "))
        TotalDia = Empleado["Pago Mensual"]/26
        DescuentoCafeteria = float(input("Hubo descuento por cafetería? "))
        if not isinstance(DescuentoCafeteria, float):
            DescuentoCafeteria = 0
        CuotaPrestamo = float(input("Ingrese la cuota del prestamo: "))
        if not isinstance(CuotaPrestamo, float):
            CuotaPrestamo = 0
        Total = ((TotalDia * DiasTrabajo) + (HorasExtra * 5500)) - DescuentoCafeteria - CuotaPrestamo
        Datos = {
            "Mes": Mes,
            "Fecha": Fecha,
            "TotalDia": Empleado["Pago Mensual"],
            "HorasExtra": HorasExtra * 5500,
            "CuotaPrestamo": CuotaPrestamo,
            "Descuentocafeteria": DescuentoCafeteria,
            "Total": f"{Total:.2f}"
        }
        ticket = dict({Mes:Datos})

        if str(Empleado["Id"]) in data_pagos.keys():
            data_pagos[str(Empleado["Id"])].append(ticket)
        else:
            data_pagos.update({Empleado["Id"]: [ticket]})
        UpdateFile(data_pagos, "Pagos.json")
        input(f"El pago de {Total:.2f} fue realizado con exito")
    except ValueError:
        input("Ha ingresado los datos incorrecto, volvera al menu principal por seguridad")

def ReportePagos(Pagos):
    try:
        Total = 0
        id = input("Ingrese el id del empleado a revisar: ")
        for key, value in Pagos.items():
            if key == id:
                for _, value2 in enumerate(value):
                    input(json.dumps(value2, indent=2))
                    for value3 in value2.values():
                        total += float(value3["Total a pagar"])
                input(f"El total pagado es: {Total:.2f}")
    except:
        input("")