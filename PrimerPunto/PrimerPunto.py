def entero (var):
    try:
        int(var)
        return True
    except:
        return False

var = input("Ingrese su edad: ")
if entero(var):
    print("tu edad es: ", var , " años")
else:
    print("No puedes tener una edad con decimales o letras")


