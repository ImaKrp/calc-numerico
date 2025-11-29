import math
import numpy as np

def executar_simpson():
    print("\nDigite a função (use 'x' como variável, ex: 'math.exp(-x**2)'): ")
    f_str = input("f(x) = ")
    f = lambda x: eval(f_str, {'x': x, 'math': math, 'np': np}) 

    try:
        a = float(input("Limite inferior 'a': "))
        b = float(input("Limite superior 'b': "))
        n = int(input("Número de subintervalos 'n' (deve ser PAR e > 0): "))
        
        if n <= 0 or n % 2 != 0:
            print("O número de subintervalos 'n' deve ser um número PAR e positivo.")
            return
    except ValueError:
        print("Entrada inválida. Limites e n devem ser numéricos.")
        return

    try:
        integral_aproximada = regra_simpson_1_3(f, a, b, n)
        
        print("\n--- Resultado ---")
        print(f"Integral de f(x) no intervalo [{a}, {b}] com n={n} subintervalos:")
        print(f"Valor Aproximado: {integral_aproximada:.8f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

def regra_simpson_1_3(f, a, b, n):
    h = (b - a) / n
    pontos_x = np.linspace(a, b, n + 1)
    pontos_y = [f(x) for x in pontos_x]

    soma_total = pontos_y[0] + pontos_y[-1]

    soma_impares = 0.0
    for i in range(1, n, 2):
        soma_impares += pontos_y[i]
    soma_total += 4 * soma_impares

    soma_pares = 0.0
    for i in range(2, n - 1, 2):
        soma_pares += pontos_y[i]
    soma_total += 2 * soma_pares

    return (h / 3) * soma_total

executar_simpson()