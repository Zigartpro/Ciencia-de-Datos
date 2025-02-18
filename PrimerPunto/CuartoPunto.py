def getPhoneNumber(var):
    try:
        int(var)
        if len(var) == 10:
            return True
        else:
            return False
    except:
        return False
phoneNumber = input("Ingrese su numero de telefono: ")
if getPhoneNumber(phoneNumber):
    print("Su numero de telefono es: ", phoneNumber)
else:
    print("No puedes ingresar letras o caracteres especiales o el numero de telefono no tiene 10 digitos")