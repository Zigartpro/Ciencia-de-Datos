def operaciones_logicas_basicas(entrada1, entrada2):
    
    if entrada1 in ['true', '1', 't']:
        valor1 = True
    else:
        valor1 = False
    
    if entrada2 in ['true', '1', 't']:
        valor2 = True
    else:
        valor2 = False
    
    print(f"\nValor 1: {valor1}")
    print(f"Valor 2: {valor2}")
    
    print("\nResultados de las operaciones lógicas:")
    print(f"AND (valor1 AND valor2): {valor1 and valor2}")
    print(f"OR (valor1 OR valor2): {valor1 or valor2}")
    print(f"NOT valor1: {not valor1}")
    print(f"NOT valor2: {not valor2}")


Valor1 = input("\nIngrese el primer valor (True/False): ").strip().lower()
Valor2 = input("\nIngrese el primer valor (True/False): ").strip().lower()

operaciones_logicas_basicas(entrada1 = Valor1, entrada2 = Valor2)