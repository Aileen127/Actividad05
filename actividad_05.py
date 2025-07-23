# Menú
ventas = []
suma = 0
while True:
    print("\nBienvenido al menú")
    print("1. Ingresar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Clasificación de ventas (alta, media, baja")
    print("7. Salir")

    option = input("Ingresa una opción del menú por favor: ")

    # Inicio de match
    match option:

        # Ingreso de ventas
        case "1":
                n = int(input("Ingresa la cantidad de días dentro del listado de ventas (una venta por día): "))
                # Ciclo for dato de variables
                for i in range(0, n):
                    venta = int(input("Ingresa el dato de la venta (números enteros positivos) "))
                    if venta > 0:
                        ventas.append(venta)
                        print("Dato de venta ingresado correctamente.")
                    else:
                        print("El dato no es valido")


        # Mostrar el listado de ventas
        case "2":
            print("Listado de ventas ingresadas:")
            for i in ventas:
                print(f" - {i}")

        # Venta alta, baja
        case "3":
            print(f"Venta más alta: {max(ventas)}")
            print(f"Venta más baja: {min(ventas)}")

        # Promedio de ventas
        case "4":
            for i in ventas:
                suma = sum(ventas)
                promedio = sum(ventas) / len(ventas)

            print(f"Promedio de ventas: {promedio}")


        # Cuantos días superaron los 1000
        case "5":
            if ventas:
                dias = 0
                for i in ventas:

                    if i > 1000:
                        dias += 1
                print(f"La cantidad de días que superaron los Q1000 son {dias}")
            else:
                    print("No hay ventas ingresadas")
        # Clasificación de cada venta
        case "6":
            for venta in ventas:
                if venta > 1000:
                    print(f"Venta alta \n  {venta}")
                elif venta >= 500 and venta <= 1000:
                    print(f"Venta media \n  {venta}")
                elif venta < 500:
                    print(f"Venta baja \n  {venta}")
                else:
                    print("No hay ventas registradas.")
        case "7":
            print("Ha salido del menú de ventas, que tenga un buen día")
            break