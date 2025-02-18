def mostrar_menu():
    print("\n--- Menú de la Lavandería ---")
    print("1. Registrar ingreso de ropa (Suma de números enteros)")
    print("2. Registrar entrega de ropa (Resta de números decimales)")
    print("3. Calcular costo del servicio (Multiplicación de un entero por un decimal)")
    print("4. Distribuir ropa en lavadoras (División de dos enteros)")
    print("5. Salir")

def opcion_1():
    print("\nHas seleccionado: Registrar ingreso de ropa.")
    cantidad_actual = int(input("Ingrese la cantidad de ropa ya registrada (número entero): "))
    nueva_carga = int(input("Ingrese la cantidad de ropa nueva (número entero): "))
    total = cantidad_actual + nueva_carga
    print(f"La cantidad total de ropa en la lavandería ahora es: {total} prendas.")

def opcion_2():
    print("\nHas seleccionado: Registrar entrega de ropa.")
    cantidad_actual = float(input("Ingrese la cantidad total de ropa en kg (número decimal): "))
    entregadas = float(input("Ingrese la cantidad de kg entregados (número decimal): "))
    
    if entregadas > cantidad_actual:
        print("Error: No puedes entregar más ropa de la que tienes registrada.")
    else:
        restante = cantidad_actual - entregadas
        print(f"La cantidad de ropa que aún queda en la lavandería es: {restante:.2f} kg.")

def opcion_3():
    print("\nHas seleccionado: Calcular costo del servicio.")
    cantidad_ropa = int(input("Ingrese la cantidad de ropa en prendas (número entero): "))
    precio_por_unidad = float(input("Ingrese el precio por prenda (número decimal): "))
    total_costo = cantidad_ropa * precio_por_unidad
    print(f"El costo total del servicio es: ${total_costo:.2f}")

def opcion_4():
    print("\nHas seleccionado: Distribuir ropa en lavadoras.")
    cantidad_ropa = int(input("Ingrese la cantidad total de ropa en prendas (número entero): "))
    num_lavadoras = int(input("Ingrese la cantidad de lavadoras disponibles (número entero): "))
    
    if num_lavadoras == 0:
        print("Error: No puedes dividir la ropa entre 0 lavadoras.")
    else:
        ropa_por_lavadora = cantidad_ropa / num_lavadoras
        restante = cantidad_ropa % num_lavadoras
        print(f"Cada lavadora recibirá aproximadamente {ropa_por_lavadora} prendas.")
        if restante > 0:
            print(f"Quedarán {restante} prendas sin asignar, que pueden ser distribuidas manualmente.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "5":
            print("Gracias por utilizar nuestro sistema de lavanderia. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

main()