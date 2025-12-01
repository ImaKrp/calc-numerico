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

        if matriz_aumentada[i, i] == 0:
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