# Menú
ventas = []
while True:
    print("\nBienvenido al menú")
    print("1. Inrgesar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Clasificar cada venta: alta (>1000), memdia (500-1000), baja (<500)")
    print("7. Salir")

    option = input("Ingresa una opción del menú por favor: ")

    # Inicio de match
    match option:
        case 1:
            n = int(input("Ingresa la cantidad de datos dentro del listado de ventas"))
            # Ciclo for dato de variables
            for i in range(0, n+1):
                venta = input("Ingresa el dato de la venta (números enteros positivos)")
                if venta > '0':
                    ventas.append(venta)
                    print("Dat de venta ingresado correctamente.")
                else:
                    print("El dato no es valido")

        case 2:
