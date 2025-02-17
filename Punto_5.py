def convertir_valor(valor, tipo_destino):
    
    tipos_validos = ['entero', 'decimal', 'cadena']
    
    if tipo_destino not in tipos_validos:
        raise TypeError(f"Tipo de destino no válido. Debe ser uno de {tipos_validos}")
    
    try:
        if tipo_destino == 'entero':
            if isinstance(valor, str):
                if '.' in valor:
                    resultado = int(float(valor))
                else:
                    resultado = int(valor)
            elif isinstance(valor, float):
                resultado = int(valor)
            else:
                resultado = int(valor)
                
        elif tipo_destino == 'decimal':
            resultado = float(valor)
                
        elif tipo_destino == 'cadena':
            resultado = str(valor)
                
        print(f"Conversión exitosa: {valor} ({type(valor).__name__}) -> {resultado} ({type(resultado).__name__})")
        return resultado
        
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error al convertir '{valor}' a {tipo_destino}: {str(e)}")

def main():

    while True:
        print("\nTipos de conversión disponibles:")
        print("1. De entero a decimal")
        print("2. De decimal a cadena")
        print("3. De cadena a entero")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '4':
            break
        
        if opcion not in ['1', '2', '3']:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        try:
            if opcion == '1':
                valor = input("Ingrese un número entero: ")
                resultado = convertir_valor(int(valor), 'decimal')
                
            elif opcion == '2':
                valor = input("Ingrese un número decimal: ")
                resultado = convertir_valor(float(valor), 'cadena')
                
            elif opcion == '3':
                valor = input("Ingrese una cadena: ")
                resultado = convertir_valor(valor, 'entero')
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()