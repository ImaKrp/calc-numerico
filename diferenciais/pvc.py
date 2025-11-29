import numpy as np
import math

def executar_pvc_diferencas_finitas():
    print("Modelo: y'' + P(x)y' + Q(x)y = R(x)")
    
    print("\n--- Definição da EDO (Ex: '2*x' para P(x)) ---")
    P_str = input("P(x) = ")
    Q_str = input("Q(x) = ")
    R_str = input("R(x) = ")
    
    P = lambda x: eval(P_str, {'x': x, 'math': math, 'np': np})
    Q = lambda x: eval(Q_str, {'x': x, 'math': math, 'np': np})
    R = lambda x: eval(R_str, {'x': x, 'math': math, 'np': np})
    
    try:
        a = float(input("\nLimite inferior (a): "))
        b = float(input("Limite superior (b): "))
        alpha = float(input("Condição de Contorno y(a) = alpha: "))
        beta = float(input("Condição de Contorno y(b) = beta: "))
        n_pontos = int(input("Número de pontos internos (n-1) para discretização: "))
        
        if n_pontos < 2:
            print("O número de pontos internos deve ser pelo menos 2.")
            return
    except ValueError:
        print("Entrada inválida. Limites, condições e pontos devem ser numéricos.")
        return

    try:
        X, Y = metodo_pvc_diferencas_finitas(P, Q, R, a, b, alpha, beta, n_pontos)
        
        print("\n--- Resultado ---")
        print(f"Número de Pontos Internos: {n_pontos}")
        
        print("\nSolução (Incluindo Contornos):")
        print(" i |    x_i    |    y_i (aprox.)")
        print("---|-----------|------------------")
        
        for i in range(len(X)):
            print(f"{i:2} | {X[i]:.6f} | {Y[i]:.6f}")
            
    except np.linalg.LinAlgError:
        print("\nErro: O sistema de equações é singular. Verifique as funções P, Q e R.")
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

def metodo_pvc_diferencas_finitas(P, Q, R, a, b, alpha, beta, n_pontos):
    N = n_pontos
    h = (b - a) / (N + 1)
    h2 = h * h
    X = np.linspace(a, b, N + 2)
    
    A = np.zeros((N, N))
    B = np.zeros(N)
    
    for i in range(N):
        x_i = X[i + 1]
        P_i = P(x_i)
        Q_i = Q(x_i)
        R_i = R(x_i)
        
        L = (1 / h2) - (P_i / (2 * h))
        D = Q_i - (2 / h2)
        U = (1 / h2) + (P_i / (2 * h))
        
        A[i, i] = D
        if i > 0:
            A[i, i - 1] = L
        if i < N - 1:
            A[i, i + 1] = U
        
        B[i] = R_i
        
        if i == 0:
            B[i] -= L * alpha
        if i == N - 1:
            B[i] -= U * beta
    
    Y_interno = np.linalg.solve(A, B)
    Y = np.concatenate(([alpha], Y_interno, [beta]))
    
    return X, Y

executar_pvc_diferencas_finitas()