# Dictionary to store the weights of clothes washed per day
week = {
    "Lunes": [],
    "Martes": [],
    "Miércoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sábado": [],
    "Domingo": []
}

# Function to register order on a specific day
def register_order():
    print("\n Días de la semana:")
    days = list(week.keys())
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")
    
    try:
        option = int(input("Seleccione el día (1-7) segun el día de la semana "))
        if option < 1 or option > 7:
            print("Por favor seleccione un número válido (1-7).")
            return
        
        selected_day = days[option - 1]
        weight = float(input(f"Ingrese el peso (kg) del pedido para {selected_day}: "))
        
        if weight <= 0:
            print("Por favor digite un numero valido. El peso debe ser un número positivo.")
            return

        week[selected_day].append(weight)
        print(f" Pedido registrado con {weight:.2f} kg de ropa en {selected_day}.")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Function to check the total of clothes washed per day
def check_total_day():
    print("\n Días de la semana:")
    days = list(week.keys())
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")
    
    try:
        option = int(input("Seleccione el día a consultar (1-7): "))
        if option < 1 or option > 7:
            print("Por favor seleccione un número válido (1-7).")
            return

        selected_day = days[option - 1]
        total_weight = sum(week[selected_day])
        
        print(f" Total de ropa lavada el {selected_day}: {total_weight:.2f} kg")
    except ValueError:
        print("Por favor ingrese un número válido.")

# Function to check the total of clothes washed in the week
def check_total_week():
    total_weekly = sum(sum(weights) for weights in week.values())
    print(f"\n Total de ropa lavada en la semana: {total_weekly:.2f} kg")

# Function to calculate the daily average of clothes washed
def daily_average():
    daily_totals = [sum(weights) for weights in week.values()]
    total_weekly = sum(daily_totals)
    
    average = total_weekly / 7  
    
    print(f" Promedio de ropa lavada por día: {average:.2f} kg")

# Function to show the history of the week with all orders
def show_history():
    print("\n Historial de la semana:")

    total_weekly = 0

    for day, weights in week.items():
        print(f"\n🔹 {day}:")
        
        if weights:
            for i, order in enumerate(weights, 1):
                print(f" Pedido {i}: {order:.2f} kg")
            
            total_day = sum(weights)
            print(f"  Total lavada en {day}: {total_day:.2f} kg")
            total_weekly += total_day
        else:
            print("❌ No hay registros.")

    print(f"\n Total de ropa lavada en la semana: {total_weekly:.2f} kg")

# Main Menu
while True:
    print("----- Menú -----")
    print("1. Registrar un nuevo pedido")
    print("2. Consultar total de ropa lavada por día")
    print("3. Consultar total de ropa lavada en la semana")
    print("4. Mostrar promedio de ropa lavada por día")
    print("5. Mostrar historial de la semana")
    print("6. Salir")
    
    option = input("Seleccione una de las siguientes opciones: ")

    if option == "1":
        register_order()
    elif option == "2":
        check_total_day()
    elif option == "3":
        check_total_week()
    elif option == "4":
        daily_average()
    elif option == "5":
        show_history()
    elif option == "6":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida. Por favor intente de nuevo.")