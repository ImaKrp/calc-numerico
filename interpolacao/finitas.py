import numpy as np
from sympy import symbols, expand

def executar_gregory_newton():
    try:
        n = int(input("\nDigite o número de pontos (n+1) que você possui: "))
        if n < 2:
            print("São necessários pelo menos 2 pontos.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    X = []
    Y = []

    print("\n--- Entrada dos Pontos (x, y) ---")
    for i in range(n):
        while True:
            try:
                entrada = input(f"Ponto {i + 1} - Digite x{i} e y{i}: ").split()
                if len(entrada) != 2:
                    print("Forneça exatamente 2 valores.")
                    continue

                X.append(float(entrada[0]))
                Y.append(float(entrada[1]))
                break
            except ValueError:
                print("Erro: valores inválidos.")

    try:
        x_interpolar = float(input("\nDigite o ponto x onde deseja interpolar: "))
    except ValueError:
        print("Entrada inválida.")
        return

    try:
        y_interpolado, coeficientes, H = gregory_newton_progressiva(X, Y, x_interpolar, n)
        P = gerar_polinomio_gregory(X, coeficientes, H)

        print("\n--- Resultado ---")
        print(f"Coeficientes Δ: {coeficientes}")
        print(f"P(x) = {P}")
        print(f"Valor interpolado em x = {x_interpolar:.4f}: P(x) = {y_interpolado:.6f}")

    except Exception as e:
        print(f"\nErro: {e}")

def fatorial(k):
    if k < 0:
        return 0
    if k == 0:
        return 1
    res = 1
    for i in range(1, k + 1):
        res *= i
    return res

def gregory_newton_progressiva(X, Y, x_interpolar, n):
    H = X[1] - X[0]
    for i in range(2, n):
        if abs((X[i] - X[i - 1]) - H) > 1e-9:
            raise ValueError("Os pontos x_i devem ser equidistantes.")

    T = np.zeros((n, n), dtype=float)
    T[:, 0] = Y
    
    for k in range(1, n):
        for i in range(n - k):
            T[i, k] = T[i + 1, k - 1] - T[i, k - 1]

    coef = T[0, :]
    x0 = X[0]
    u = (x_interpolar - x0) / H

    y_interpolado = coef[0]
    termo = 1.0
    
    for k in range(1, n):
        termo *= (u - (k - 1))
        y_interpolado += (coef[k] / fatorial(k)) * termo
        
    return y_interpolado, coef, H

def gerar_polinomio_gregory(X, coef, H):
    x = symbols('x')
    x0 = X[0]
    u = (x - x0) / H

    P = coef[0]
    termo = 1
    
    for k in range(1, len(coef)):
        termo *= (u - (k - 1))
        P += coef[k] * termo / fatorial(k)

    return expand(P)

executar_gregory_newton()