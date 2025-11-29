import math
import numpy as np

def executar_trapezios():
    print("\nDigite a função (use 'x' como variável, ex: 'math.sin(x) / x'): ")
    f_str = input("f(x) = ")
    f = lambda x: eval(f_str, {'x': x, 'math': math, 'np': np}) 

    try:
        a = float(input("Limite inferior 'a': "))
        b = float(input("Limite superior 'b': "))
        n = int(input("Número de subintervalos 'n' (quanto maior, mais preciso): "))
        
        if n <= 0:
            print("O número de subintervalos deve ser positivo.")
            return
    except ValueError:
        print("Entrada inválida. Limites e n devem ser numéricos.")
        return

    try:
        integral_aproximada = regra_trapezios(f, a, b, n)
        
        print("\n--- Resultado ---")
        print(f"Integral de f(x) no intervalo [{a}, {b}] com n={n} subintervalos:")
        print(f"Valor Aproximado: {integral_aproximada:.8f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método (Verifique a função digitada): {e}")

def regra_trapezios(f, a, b, n):
    h = (b - a) / n
    pontos_x = np.linspace(a, b, n + 1)
    pontos_y = [f(x) for x in pontos_x]
    soma_extremos = pontos_y[0] + pontos_y[-1]
    soma_interna = np.sum(pontos_y[1:-1]) * 2
    integral = (h / 2) * (soma_extremos + soma_interna)
    return integral

executar_trapezios()