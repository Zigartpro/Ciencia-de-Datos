def getTemperature (var):
    try:
        float(var)
        return True
    except:
        return False
temperature= input("Ingrese la temperatura: ")
if getTemperature(temperature):
    print("La temperatura es: ", temperature , "°C")
else:
    print("No puedes ingresar letras o caracteres especiales")
    