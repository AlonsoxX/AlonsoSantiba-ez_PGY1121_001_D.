from os import system
system("cls")

import datetime

entradas_platinum = [0] * 20
entradas_gold = [0] * 30
entradas_silver = [0] * 50
asistentes = []

def mostrar_menu():
    print("bienvenido, a continuacion le muestro el menu de interaccion")
    
    print("======= Menú =======")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprar_entradas():
    cantidad = int(input("ingrese la cantidad de entradas que desea comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("la cantidad es incorrecta, por favor vuelva a ingresar la cantidad correctamente.")
        return

    asientos_disponibles = obtener_asientos_disponibles()
    for i in range(cantidad):
        print(f"Asiento {i + 1}:")
        mostrar_ubicaciones_disponibles()
        asiento = int(input("Seleccione un asiento: "))
        if asiento < 1 or asiento > 100:
            print("Asiento no valido.")
            return
        
        if asientos_disponibles[asiento - 1]:
            print("EL Asiento no esta disponible.")
        else:
            asientos_disponibles[asiento - 1] = True
            tipo_entrada = obtener_tipo_entrada(asiento)
            precio = obtener_precio_entrada(tipo_entrada)
            asistente = input("Ingrese el run del asistente porfavor (sin guiones ni puntos, para un mejor servicio): ")
            asistentes.append((asiento, tipo_entrada, asistente))
            print(" La operacion fue realizada correctamente.")

def obtener_asientos_disponibles():
    asientos_disponibles = [False] * 100
    for asiento in asistentes:
        asientos_disponibles[asiento[0] - 1] = True
    return asientos_disponibles

def mostrar_ubicaciones_disponibles():
    asientos_disponibles = obtener_asientos_disponibles()
    print("===== Lugares disponibles ======")
    for i in range(100):
        if asientos_disponibles[i]:
            print(f"Asiento {i + 1}: Vendido")
        else:
            print(f"Asiento {i + 1}: Disponible")

def obtener_tipo_entrada(asiento):
    if asiento <= 20:
        return "Platinum"
    elif asiento <= 50:
        return "Gold"
    else:
        return "Silver"

def obtener_precio_entrada(tipo_entrada):
    if tipo_entrada == "Platinum":
        return 120000
    elif tipo_entrada == "Gold":
        return 80000
    else:
        return 50000

def ver_listado_asistentes():
    asistentes_ordenados = sorted(asistentes, key=lambda x: x[2])
    print("======== Listado de asistentes ========")
    for asistente in asistentes_ordenados:
        print(f"run: {asistente[2]}, Asiento: {asistente[0]}, Tipo: {asistente[1]}")

def mostrar_ganancias_totales():
    total_platinum = sum([obtener_precio_entrada("Platinum") for _ in entradas_platinum])
    total_gold = sum([obtener_precio_entrada("Gold") for _ in entradas_gold])
    total_silver = sum([obtener_precio_entrada("Silver") for _ in entradas_silver])
    total = total_platinum + total_gold + total_silver

    print("========= Ganancias totales ==========")
    print("Tipo Entrada   Cantidad   Total")
    print(f"Platinum       {entradas_platinum.count(1):<10} {total_platinum:<10}")
    print(f"Gold           {entradas_gold.count(1):<10} {total_gold:<10}")
    print(f"Silver         {entradas_silver.count(1):<10} {total_silver:<10}")
    print(f"TOTAL          {entradas_platinum.count(1) + entradas_gold.count(1) + entradas_silver.count(1):<10} {total:<10}")

def salir():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"\n¡Hasta pronto ('・ω・'), {nombre} {apellido}! usted salio del sistema el dia {fecha_actual}.")
while True:
    mostrar_menu()
    opcion = input("Seleccione una de estas: ")

    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        ver_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        salir()
        break
    else:
        print("Opcion no correcta. Por favor, ingrese una opcion del menu correctamente.")
