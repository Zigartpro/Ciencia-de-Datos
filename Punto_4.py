# Escribe un programa que compare dos valores (números o cadenas) y determine si son iguales, diferentes, mayores o menores. 

def Comparar_valores(valor1, valor2):
    
    TV1 = len(valor1)
    TV2 = len(valor2)

    if TV1 == TV2:
        for i in range(len(valor1)):
            if valor1[i] != valor2[i]:
                print(f"Las palabras difieren en el caracter {i + 1}: '{valor1[i]}' y '{valor2[i]}'")
                valores = False
                break
            else:
                 valores = True
        
        if valor1.isnumeric() and valor2.isnumeric():
                if valor1 == valor2:
                     print("Los dos numeros son iguales")
                elif valor1 > valor2:
                    print("El numero mayor es " + valor1)
                else:
                    print("El numero mayor es " + valor2)

        if valores == True:
            print("Los dos valores son iguales.")

    elif TV1 != TV2:
        print("Los valores son diferentes")

Valor1 = input("Ingrese el segundo valor: ")

Valor2 = input("Ingrese el primer valor: ")

Comparar_valores(valor1=Valor1, valor2=Valor2)