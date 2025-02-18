def mostrar_menu():
    print("\n--- Menú de Operaciones con Cadenas en la Lavandería ---")
    print("1. Concatenar nombre del cliente y servicio")
    print("2. Extraer un carácter del código de pedido")
    print("3. Convertir el nombre del cliente a mayúsculas")
    print("4. Calcular la longitud de la descripción del servicio")
    print("5. Salir")

def opcion_1():
    print("\nHas seleccionado: Concatenar nombre del cliente y servicio.")
    nombre = input("Ingrese el nombre del cliente: ")
    servicio = input("Ingrese el servicio solicitado (Lavado, Planchado, Tintura.): ")
    print("Registro de servicio:", nombre + " - " + servicio)

def opcion_2():
    print("\nHas seleccionado: Extraer un carácter del código de pedido.")
    codigo = input("Ingrese el código del pedido: ")
    indice = int(input("Ingrese el índice del carácter a extraer: "))
    
    if 0 <= indice < len(codigo):
        print(f"El carácter extraído es: {codigo[indice]}")
    else:
        print("Índice fuera de rango.")

def opcion_3():
    print("\nHas seleccionado: Convertir el nombre del cliente a mayúsculas.")
    nombre = input("Ingrese el nombre del cliente: ")
    print("Nombre en mayúsculas:", nombre.upper())

def opcion_4():
    print("\nHas seleccionado: Calcular la longitud de la descripción del servicio.")
    descripcion = input("Ingrese la descripción del servicio: ")
    print(f"La longitud de la descripción es: {len(descripcion)} caracteres.")

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
            print("Gracias por utilizar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()