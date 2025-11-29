import numpy as np
from sympy import symbols, expand

def executar_lagrange():
    try:
        n = int(input("\nDigite o número de pontos (n+1) que você possui: "))
        if n < 2:
            print("São necessários pelo menos 2 pontos para a interpolação.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    X = []
    Y = []
    print("\n--- Entrada dos Pontos (x, y) ---")
    
    for i in range(n):
        while True:
            try:
                entrada = input(f"Ponto {i + 1} - Digite x{i} e y{i} (Ex: 1.0 2.5): ").split()
                if len(entrada) != 2:
                    print("Erro: Forneça exatamente 2 valores (x e y).")
                    continue
                
                x_val = float(entrada[0])
                y_val = float(entrada[1])
                
                X.append(x_val)
                Y.append(y_val)
                break
            except ValueError:
                print("Erro: Ambos os valores devem ser numéricos. Tente novamente.")

    try:
        x_interpolar = float(input("\nDigite o ponto x onde você deseja interpolar o valor: "))
    except ValueError:
        print("Entrada inválida. Digite um valor numérico para x.")
        return

    try:
        y_interpolado = lagrange_interpolacao(X, Y, x_interpolar, n)
        P = gerar_polinomio_lagrange(X, Y)
        
        print("\n--- Resultado ---")
        print(f"P(x) = {P}")
        print(f"Valor interpolado em x = {x_interpolar:.4f}: P(x) = {y_interpolado:.6f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

    return

def lagrange_interpolacao(X, Y, x_interpolar, n):
    y_interpolado = 0.0
    
    for i in range(n):
        L_i = 1.0
        
        for j in range(n):
            if i != j:
                if X[i] == X[j]:
                    raise ValueError(f"Os pontos x_i devem ser distintos. X[{i}] é igual a X[{j}].")
                termo = (x_interpolar - X[j]) / (X[i] - X[j])
                L_i *= termo
        
        y_interpolado += Y[i] * L_i
        
    return y_interpolado

def gerar_polinomio_lagrange(X, Y):
    x = symbols('x')
    n = len(X)
    P = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - X[j]) / (X[i] - X[j])
        P += Y[i] * L_i

    return expand(P)

executar_lagrange()