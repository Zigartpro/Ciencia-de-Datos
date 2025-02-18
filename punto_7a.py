'''
Taller Ciencia de Datos punto 7
Integrantes
Beltrán Chavez Mateo
Caro Alarcón Gennier
Sarmiento Duvan
'''
from tabulate import tabulate

#Create a client list
clients = []

# Function Client Register
def client_register():
    try:
        name_client = input("Ingrese el nombre completo del cliente de la lavanderia: ")
        if not name_client:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        
        age = int(input("Ingrese la edad del cliente: "))
        if age < 18:
            raise ValueError("El cliente debe ser mayor de edad: ")
        
        document = int(input("Ingrese el numero de documento del cliente: "))
        if document <= 0:
            raise ValueError("El número de documento debe ser un número positivo.")
        
        garment_quantity = int(input("Ingrese la cantidad de prendas del cliente: "))
        if garment_quantity < 0:
            raise ValueError("La cantidad de prendas no puede ser negativa ni nula")
        
        client = {"name": name_client, "age": age, "garment": garment_quantity, "document_id": document}  # Create a client dictionary
        clients.append(client)
        print(f"Cliente '{name_client}' registrado exitosamente.\n")
        
    except ValueError as e:
        print(f"Error: {e}. Por favor intentelo de nuevo de nuevo.\n")

# Function to search client
def search_client():
    search = input("Ingrese el nombre o documento del cliente: ")
    
    if not search:
        print("Por favor digita un dato para buscar\n")
        return
    
    coincidences = [i for i in clients if search.lower() in i["name"].lower() or search == str(i["document_id"])]  # Buscar coincidencias

    if coincidences:
        print("\nCoincidencias encontradas:")
        table = [[i["name"], i["document_id"], i["age"], i["garment"]] for i in coincidences]
        headers = ["Nombre", "Documento Identidad", "Edad", "Cantidad Prendas"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print(f"No se encontraron coincidencias para '{search}'.")
    print()

def show_all_clients():
    if not clients:
        print("No hay clientes registrados.\n")
        return
    
    print("\n Lista de todos los clientes de la Lavanderia")
    table = [[i["name"], i["document_id"], i["age"], i["garment"]] for i in clients]
    headers = ["Nombre", "Documento Identidad", "Edad", "Cantidad Prendas"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()

# Main Menu
def menu():
    while True:
        print("----- Menú -----")
        print("1. Registrar un Cliente")
        print("2. Buscar una Cliente")
        print("3. Mostrar todos los Clientes")
        print("4. Salir")
        option = input("Por favor seleccione una de las siguiente opciones: ")

        if option == "1":
            client_register()
        elif option == "2":
            search_client()
        elif option == "3":
            show_all_clients()
        elif option == "4":
            print("Gracias por usar el programa")
            break
        else:
            print("La opcion no es válida. Por favor intente de nuevo.\n")

# Start the menu
menu()