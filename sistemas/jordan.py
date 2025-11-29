import numpy as np

def executar_gauss_jordan():
    try:
        n = int(input("\nDigite o número de variáveis (e equações) do sistema: "))
        if n <= 0:
            print("O número de variáveis deve ser positivo.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    A = []
    b = []
    
    print("\n--- Entrada de Dados ---")
    for i in range(n):
        while True:
            try:
                entrada = input(f"Equação {i + 1} - Digite os {n} coeficientes e o termo independente (Ex: 1 2 3 10): ").split()
                if len(entrada) != n + 1:
                    print(f"Erro: Você deve fornecer {n+1} valores. Tente novamente.")
                    continue
                
                valores = [float(val) for val in entrada]
                
                A.append(valores[:n])
                b.append(valores[n])
                break
            except ValueError:
                print("Erro: Todos os valores devem ser numéricos. Tente novamente.")

    try:
        solucoes = gauss_jordan_eliminacao(A, b, n)
        
        print("\n--- Resultado ---")
        if solucoes is not None:
            for i in range(n):
                print(f"x{i + 1} = {solucoes[i]:.6f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

    return

def gauss_jordan_eliminacao(A, b, n):
    M = np.array(A, dtype=float)
    vector_b = np.array(b, dtype=float).reshape(n, 1)
    matriz_aumentada = np.hstack((M, vector_b))

    for i in range(n):
        pivot_row = i
        for k in range(i + 1, n):
            if abs(matriz_aumentada[k, i]) > abs(matriz_aumentada[pivot_row, i]):
                pivot_row = k
        matriz_aumentada[[i, pivot_row]] = matriz_aumentada[[pivot_row, i]]

        if matriz_aumentada[i, i] == 0:aimport numpy as np

def executar_lagrange():
    print("\n\n〰️ Interpolação Polinomial de Lagrange 〰️")
    
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
        
        print("\n--- Resultado ---")
        print(f"O polinômio de grau {n-1} é: P(x)")
        print(f"Valor interpolado em x = {x_interpolar:.4f} é P(x) = {y_interpolado:.6f}")
        
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

executar_lagrange()
            print("\nO sistema não tem solução única (pivô zero).")
            return None
        
        pivot_valor = matriz_aumentada[i, i]
        matriz_aumentada[i, i:] = matriz_aumentada[i, i:] / pivot_valor
        
        for k in range(n):
            if k != i:
                fator = matriz_aumentada[k, i]
                matriz_aumentada[k, i:] = matriz_aumentada[k, i:] - fator * matriz_aumentada[i, i:]
    
    solucoes = matriz_aumentada[:, n]
    return solucoes

executar_gauss_jordan()