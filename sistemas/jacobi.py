import numpy as np

def executar_jacobi():
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

    print("\n--- Parâmetros do Método ---")
    while True:
        try:
            x0_str = input(f"Digite o chute inicial (Ex: 0 0 0): ").split()
            if len(x0_str) != n:
                print(f"Erro: O chute inicial deve ter {n} valores. Tente novamente.")
                continue
            x0 = np.array([float(val) for val in x0_str])
            break
        except ValueError:
            print("Erro: Os valores do chute inicial devem ser numéricos. Tente novamente.")

    try:
        tolerancia = float(input("Digite a Tolerância (Ex: 0.0001): "))
        max_iteracoes = int(input("Digite o número máximo de iterações (Ex: 50): "))
    except ValueError:
        print("Entrada inválida para tolerância ou iterações.")
        return

    try:
        solucoes = jacobi(A, b, x0, n, tolerancia, max_iteracoes)
        
        print("\n--- Resultado ---")
        if solucoes is not None:
            for i in range(n):
                print(f"x{i + 1} = {solucoes[i]:.6f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

    return

def jacobi(A, b, x0, n, tolerancia, max_iteracoes):
    M = np.array(A, dtype=float)
    vector_b = np.array(b, dtype=float)
    
    x_k = np.copy(x0) 
    
    for k in range(max_iteracoes):
        
        x_k_mais_1 = np.zeros(n)
        
        for i in range(n):
            
            if M[i, i] == 0:
                print("\nDivisão por zero: O elemento diagonal é zero. O método falhou.")
                return None
            
            soma = 0.0
            
            for j in range(n):
                if i != j:
                    soma += M[i, j] * x_k[j] 
            x_k_mais_1[i] = (vector_b[i] - soma) / M[i, i]
            
        erro = np.linalg.norm(x_k_mais_1 - x_k, ord=np.inf)
        
        x_k = x_k_mais_1
        
        if erro < tolerancia:
            print(f"\nConvergência alcançada em {k + 1} iterações.")
            print(f"Erro final (norma ∞): {erro:.8f}")
            return x_k_mais_1
    
    print(f"\nMáximo de iterações ({max_iteracoes}) atingido. Solução pode não ter convergido.")
    print(f"Erro na última iteração: {erro:.8f}")
    return x_k_mais_1

executar_jacobi()