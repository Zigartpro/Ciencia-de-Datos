'''
Taller Ciencia de Datos punto 8
Integrantes
Beltrán Chavez Mateo
Caro Alarcón Gennier
Sarmiento Duvan
'''

#Function to calculate work table area (triangular)
def calculate_table_area():
    
    try:
        base_length = float(input("Ingrese la base de la mesa de trabajo en metros (m): "))
        height = float(input("Ingrese la altura de la mesa de trabajo en metros (m): "))
        area = (base_length * height) / 2
        print(f" El área de la mesa de trabajo es de {area:.2f} metros cuadrados m²")
    except ValueError:
        print("Por favor ingrese números válidos.")

#Function to determine the number of garments is even or odd
def is_even_or_odd():
    
    try:
        quantity = int(input("Ingrese la cantidad de prendas en la tanda: "))
        if quantity % 2 == 0:
            result = "Par"
        else:
            result = "Impar"
        print(f" La cantidad de prendas ({quantity}) es una cantidad {result}.")
    except ValueError:
        print("Por favor ingrese un número de prendas válido (entero).")

# Function to find the heaviest garment
def heaviest_clothing():
    
    try:
        input_data = input("Ingrese los pesos de las prendas (kg) separados por espacio: ")
        if not input_data.strip():
            print("No se ingresaron pesos")
            return
        
        weights = [float(weight) for weight in input_data.split()]
        
        # Encontrar el valor máximo sin usar max()
        heaviest = weights[0]
        index = 0
        for i, weight in enumerate(weights):
            if weight > heaviest:
                heaviest = weight
                index = i
        
        print(f"La prenda #{index + 1} es la prenda más pesada con un peso total de {heaviest:.2f} kg")
    except ValueError:
        print("Por favor ingrese números válidos")

# Main Menu
while True:
    print("----- Menú -----")
    print("1. Calcular el área de la mesa de trabajo")
    print("2. Determinar si la cantidad de prendas es par o impar")
    print("3. Encontrar la prenda más pesada")
    print("4. Salir")

    option = input("Seleccione una opción (1-5): ")

    if option == "1":
        calculate_table_area()
    elif option == "2":
        is_even_or_odd()
    elif option == "3":
        heaviest_clothing()
    elif option == "4":
        print("Gracias por usar el programa")
        break
    else:
        print("La opcion no es válida. Por favor intente de nuevo.\n")