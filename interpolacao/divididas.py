import numpy as np
from sympy import symbols, expand

def executar_newton_dd():
    try:
        n = int(input("\nDigite o número de pontos (n+1) que você possui: "))
        if n < 2:
            print("São necessários pelo menos 2 pontos para a interpolação.")
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
                print("Valores inválidos. Tente novamente.")

    try:
        x_interpolar = float(input("\nDigite o ponto x onde você deseja interpolar: "))
    except ValueError:
        print("Entrada inválida.")
        return

    try:
        y_interpolado, coeficientes = newton_diferencas_divididas(X, Y, x_interpolar, n)
        P = gerar_polinomio_newton(X, coeficientes)

        print("\n--- Resultado ---")
        print(f"Coeficientes: {coeficientes}")
        print(f"P(x) = {P}")
        print(f"Valor interpolado em x = {x_interpolar:.4f}: P(x) = {y_interpolado:.6f}")

    except Exception as e:
        print(f"\nErro: {e}")

def newton_diferencas_divididas(X, Y, x_interpolar, n):
    T = np.zeros((n, n), dtype=float)
    T[:, 0] = Y 
    
    for k in range(1, n):
        for i in range(n - k):
            if X[i + k] - X[i] == 0:
                raise ValueError("Os pontos x_i devem ser distintos.")
            T[i, k] = (T[i + 1, k - 1] - T[i, k - 1]) / (X[i + k] - X[i])

    coeficientes = T[0, :]
    
    y_interpolado = coeficientes[0]
    termo = 1.0
    
    for k in range(1, n):
        termo *= (x_interpolar - X[k - 1])
        y_interpolado += coeficientes[k] * termo
        
    return y_interpolado, coeficientes

def gerar_polinomio_newton(X, coef):
    x = symbols('x')
    n = len(coef)

    P = 0
    termo = 1

    for k in range(n):
        P += coef[k] * termo
        termo *= (x - X[k]) if k < n - 1 else 1

    return expand(P)

executar_newton_dd()