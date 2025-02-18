def getAge(var):
    try:
        int(var)
        return True
    except:
        return False
age= input("Ingrese su edad: ")
if getAge(age):
    if int(age) >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:  
    print("No puedes tener una edad con decimales o letras")


