import json
import sys
import tkinter as tk


def cotizador(debug, debug2, ubicacion, gestion, ages, tarjeta, pool, comercial, continuidad, aporte, monotributo_ind, preexistencia, mes):
    mensaje = ""

    def calcular_aportes(aporte):
        if aporte == 0:
            aporte_real = 0
            return aporte_real
        else:
            aporte_real = (aporte / 0.03) * 0.06885
            return aporte_real

    def descuentos(gestion, ages, ubicacion, reporte, debug):
        capitas = len(ages)
        tarjeta = 10
        continuidad_PP = 10
        comercial_cba = [25, 15, 10, 5]
        comercial_larioja = [35, 25, 20, 15]
        pool_cba = [10, 15, 20]
        pool_larioja = [20, 25, 30]
        aplica_tarjeta = None  # Inicialmente, no se ha aplicado la tarjeta
        # Reporte 1_tarjeta, 2_pool, 3_comercial, 4_continuidad
        descuento = 0

        if reporte[1] == "s" and reporte[2] == "s" and gestion != 3:
            duality = input(
                "Ingresa:\n1- Para Dto. Comercial.\n2- Para Pool:\n>")
            if duality == '1':
                reporte[2] = "s"
                reporte[1] = "n"
            elif duality == '2':
                reporte[2] = "n"
                reporte[1] = "s"
            else:
                print("Dato inválido")

        elif gestion == 1 and reporte[1] == "s":
            if capitas == 1:
                pool_cba = [pool_cba[0]]
                pool_larioja = [pool_larioja[0]]
            elif capitas == 2:
                pool_cba = [pool_cba[1]]
                pool_larioja = [pool_larioja[1]]
            else:
                pool_cba = [pool_cba[2]]
                pool_larioja = [pool_larioja[2]]

            if ubicacion == "C":
                if reporte[0] == "s":
                    if debug:
                        print("Cordoba, Pool, Tarjeta, gestión 1")
                    for i in range(len(pool_cba)):
                        pool_cba[i] += tarjeta
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = pool_cba
                else:
                    descuento = pool_cba
                    if debug:
                        print("Cordoba, pool, gestión 1")
            elif ubicacion == "R":
                if reporte[0] == "s":
                    if debug:
                        print("pool_larioja, Tarjeta, gestión 1")
                    for i in range(len(pool_larioja)):
                        pool_larioja[i] += tarjeta
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = pool_larioja
                else:
                    descuento = pool_larioja
                    if debug:
                        print("pool_larioja, pool, gestión 1")
        elif (gestion == 1 or gestion == 2) and reporte[1] != "s":
            if ubicacion == "C":
                if reporte[0] == "s":
                    if debug:
                        print("Cordoba, Tarjeta, gestión 1 or 2")
                    for i in range(len(comercial_cba)):
                        comercial_cba[i] += tarjeta
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = comercial_cba
                else:
                    descuento = comercial_cba
                    if debug:
                        print("Cordoba, gestión 1 or 2")
            elif ubicacion == "R":
                if reporte[0] == "s":
                    if debug:
                        print("LaRioja, Tarjeta, gestión 1 or 2")
                    for i in range(len(comercial_larioja)):
                        comercial_larioja[i] += tarjeta
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = comercial_larioja
                else:
                    if debug:
                        print("LaRioja, Tarjeta, gestión 1 or 2")
                    descuento = comercial_larioja
        elif gestion == 1 and reporte[1] == "s":
            if ubicacion == "C":
                if debug:
                    # You need to specify what to print here
                    print("Gestion 1, Cordoba Pool")
                descuento = pool_cba
            elif ubicacion == "R":
                if debug:
                    # You need to specify what to print here
                    print("Gestion 1, LaRioja Pool")
                descuento = pool_larioja
        elif gestion == 3 and capitas >= 3:
            if ubicacion == "C":
                if reporte[3] == "s":
                    if debug:
                        print("Cordoba, Continuidad and Comercial, gestión 3_PP")
                    for i in range(len(comercial_cba)):
                        comercial_cba[i] += continuidad_PP
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = comercial_cba
                else:
                    if debug:
                        print("Cordoba, Comercial, gestión 3_PP")
                    descuento = comercial_cba
            elif ubicacion == "R":
                if reporte[3] == "s":
                    if debug:
                        print("La Rioja, Gestion 3, Desc. comercial and continuidad")
                    for i in range(len(comercial_larioja)):
                        comercial_larioja[i] += continuidad_PP
                    aplica_tarjeta = True  # Se aplica la tarjeta

                    descuento = comercial_larioja
        elif gestion == 3 and capitas < 3 and reporte[3] == "s":
            if debug:
                print("Gestión 3, Continuidad")
            descuento = [continuidad_PP]

        elif gestion == 3 and capitas < 3 and reporte[3] != "s":
            if debug:
                print("Gestión 3, Sin descuento")
            descuento = 0
        else:
            print("Situacion desconocida 140")

        if debug:
            print("\nDescuentos: ", descuento)
        else:
            pass

        tarjeta_num = tarjeta

        return descuento, aplica_tarjeta, tarjeta_num

    def bd_cotizacion(lugar, gestion):
        if lugar == "C":
            ubicacion = "Cordoba"
        elif lugar == "R":
            ubicacion = "LaRioja"
        else:
            print("Ubicación inválida")
            sys.exit()
        if gestion == 1:
            name_gestion = "RD"
        elif gestion == 2:
            name_gestion = "Monotributo"
        elif gestion == 3:
            name_gestion = "Prepago"
        else:
            print("Gestión inválida")
            sys.exit()

        file_name = f"{ubicacion}_{name_gestion}_2023-{mes}.json"
        with open(file_name, "r") as file:
            data = json.load(file)
        location = file_name.split("_")[0]
        tipo = file_name.split("_")[1]
        return data, location, tipo, name_gestion, ubicacion

    def cotizacion_base(ages, data, gestion):
        group_size = len(ages)
        planes = ['B200', 'B300', 'N200', 'N400', 'N500']
        coty = {}  # Crear un diccionario para almacenar los resultados

        if gestion == 3:
            planes = ['B200', 'N200', 'N400', 'N500']

        for plan in planes:
            total_cost = 0
            individual_costs = {}

            for age in ages:
                age_range = None
                if age >= 0 and age <= 20:
                    age_range = "0 a 20"
                elif age >= 21 and age <= 45:
                    age_range = "21 a 45"
                elif age >= 46 and age <= 55:
                    age_range = "46 a 55"
                elif age >= 56 and age <= 65:
                    age_range = "56 a 65"
                elif age > 65:
                    age_range = "mas de 66"

                if age_range:
                    if group_size == 1:
                        cost = data[plan][age_range]["IND."] + 1
                    elif group_size >= 5:
                        cost = data[plan][age_range]["5 o mas"] + 1
                    else:
                        cost = data[plan][age_range][str(
                            group_size) + " PERS."] + 1

                    if cost is not None:
                        total_cost += cost
                        individual_costs[age] = cost

            # Almacenar los resultados en el diccionario coty
            coty[plan] = [total_cost, individual_costs]

        return coty, planes

    aporte_real = calcular_aportes(aporte)

    monotributo_total = len(ages) * monotributo_ind

    if gestion == 2:
        pool = "n"
        if monotributo_ind == 0:
            print("Falta agregar aportes del Monotributo")
        else:
            aporte_real = monotributo_total
    elif gestion == 3:
        aporte_real = 0

    data, location, tipo, name_gestion, lugar = bd_cotizacion(
        ubicacion, gestion)
    coty, planes = cotizacion_base(ages, data, gestion)

    if debug2:
        print(lugar)
        print(name_gestion)
        if aporte_real > 0:
            print("aporte real: ", aporte_real)
        else:
            pass
        print("Preexistencias: ", preexistencia)
        print("Edades: ", ages)
        if len(ages) > 2:
            print("Capitas: ", len(ages))
        else:
            pass
    else:
        pass

    reporte = [tarjeta, pool, comercial, continuidad]

    tarjeta_desc = False
    descuento, aplica_tarjeta, tarjeta_num = descuentos(
        gestion, ages, ubicacion, reporte, debug)

    if isinstance(descuento, list) and tarjeta_desc in descuento:
        tarjeta_desc = True
    else:
        tarjeta_desc = False

    if debug:
        for plan in coty:
            print(f"\n🔆Plan {plan}: ${int(coty[plan][0])}")

        print(ubicacion)
        print("gestion: ", gestion)
        print("aporte real: ", aporte_real)
        print("Preexistencias: ", preexistencia)
        print(ages)
        print("tarjeta, pool, comercial, continuidad")
        print(reporte)
        print(descuento)

    costo_plan_por_aportes = []

    if gestion == 1 or gestion == 2:
        if debug:
            print("Se restan aportes")
        else:
            pass
        for plan in coty:
            proceso_aportes = coty[plan][0] - aporte_real
            proceso_aportes += preexistencia
            if proceso_aportes < 10:
                proceso_aportes = 0
            else:
                pass
            costo_plan_por_aportes.append(proceso_aportes)

    elif gestion == 3:
        if debug:
            print("Sobrecuota por preexistencias")
        else:
            pass
        for plan in coty:
            proceso_aportes = coty[plan][0] + preexistencia
            costo_plan_por_aportes.append(round(proceso_aportes, 2))

    else:
        print("Descuento desconocido")
    if debug2:
        debug = True

    else:
        pass
    if descuento == 0:
        if debug:
            print("Descuento tipo 0")
        else:
            pass
        for i, plan in enumerate(coty):
            print(f"\n🔆Plan {plan}: ${costo_plan_por_aportes[i]}")
            mensaje += f"\nPlan {plan}: ${costo_plan_por_aportes[i]}"

    else:
        num_desc = len(descuento)
        if num_desc == 1:
            if debug:
                print("Descuento tipo 1")
            else:
                pass
            for i, plan in enumerate(coty):

                print(f"🔆Plan {plan}: ${costo_plan_por_aportes[i]}")
                mensaje += f"\nPlan {plan}: ${costo_plan_por_aportes[i]}\n"
                cuota = round(
                    int(coty[plan][0]) * (1 - descuento[0] / 100)-aporte_real+preexistencia, 2)
                cuota = max(0, cuota)
                if cuota < 10:
                    cuota = 0
                else:
                    pass
                print(f"Cuota con descuentos incluidos: ${cuota}")
                mensaje += f"Cuota con descuentos incluidos: ${cuota}\n"
            print(f"\n> Descuento incluido del {descuento[0]} %")
            mensaje += f"\n> Descuento incluido del {descuento[0]} %"

        elif num_desc == 4:
            if debug:
                print("Descuento tipo 4")
            else:
                pass
            for i, plan in enumerate(coty):
                if debug:
                    print(f"\nDEBUG: 🔆Plan {plan}: ${int(coty[plan][0])}")
                    mensaje += f"\nDEBUG: Plan {plan}: ${int(coty[plan][0])}"
                else:
                    print("\n")
                print(f"🔆Plan {plan}: ${round(costo_plan_por_aportes[i],2)}")
                mensaje += f"\nPlan {plan}: ${costo_plan_por_aportes[i]}\n"

                for i in range(4):
                    cuota_descuento = descuento[i]
                    cuota_range = f"Cuota {i * 3 + 1} a {i * 3 + 3}"
                    cuota_costo = round(
                        int(coty[plan][0]) * (1 - cuota_descuento / 100)-aporte_real+preexistencia, 2)
                    cuota_costo = max(0, cuota_costo)
                    print(f"{cuota_range}: ${cuota_costo}")
                    mensaje += f"{cuota_range}: ${cuota_costo}\n"

            print(f"\n> Cuota 1 a 3 descuento del {descuento[0]} %")
            print(f"> Cuota 4 a 6 descuento del {descuento[1]} %")
            print(f"> Cuota 7 a 9 descuento del {descuento[2]} %")
            print(f"> Cuota 10 a 12 descuento del {descuento[3]} %")
            mensaje += f"\n> Cuota 1 a 3 descuento del {descuento[0]} %\n> Cuota 4 a 6 descuento del {descuento[1]} %\n> Cuota 7 a 9 descuento del {descuento[2]} %\n> Cuota 10 a 12 descuento del {descuento[3]} %"
    if aplica_tarjeta:
        # Esto es el valor del descuento de la tarjeta aplicado
        valor_descuento_tarjeta = tarjeta_num
        print(
            f"*Se incluye descuento por tarjeta del: {valor_descuento_tarjeta}%")
        mensaje += f"\n*Se incluye descuento por tarjeta del: {valor_descuento_tarjeta}%"
    return mensaje
