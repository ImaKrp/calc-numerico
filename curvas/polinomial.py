import numpy as np

def executar_ajuste_polinomial():
    try:
        n = int(input("\nDigite o número de pontos de dados (observações): "))
        if n < 2:
            print("São necessários pelo menos 2 pontos.")
            return
            
        m = int(input("Digite o grau (m) do polinômio de ajuste (Ex: 2 para parábola): "))
        
        if m < 1 or m >= n:
            print(f"O grau do polinômio (m={m}) deve ser menor que o número de pontos ({n}) e maior que zero.")
            return
            
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    X_entrada = []
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
                
                X_entrada.append(x_val)
                Y.append(y_val)
                break
            except ValueError:
                print("Erro: Ambos os valores devem ser numéricos. Tente novamente.")

    try:
        X_entrada = np.array(X_entrada, dtype=float)
        Y = np.array(Y, dtype=float).reshape(n, 1)
        
        X = np.zeros((n, m + 1), dtype=float)
        for j in range(m + 1):
            X[:, j] = X_entrada**j
        
        coeficientes = minimos_quadrados_polinomial(X, Y)
        
        print("\n--- Resultado do Ajuste ---")
        
        equacao = f"P(x) = {coeficientes[0, 0]:.6f}"
        
        for i in range(1, m + 1):
            print(f"Coeficiente a{i} (x^{i}): {coeficientes[i, 0]:.6f}")
            equacao += f" + {coeficientes[i, 0]:.6f}x^{i}"
            
        print(f"\nPolinômio de Melhor Ajuste (Grau {m}):\n{equacao}")
        
    except np.linalg.LinAlgError:
        print("\nErro de Álgebra Linear: A matriz (X^T * X) é singular (não invertível). O sistema é mal condicionado.")
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

def minimos_quadrados_polinomial(X, Y):
    XT = X.T 
    XTX = np.dot(XT, X)
    XTX_inv = np.linalg.inv(XTX)
    XTY = np.dot(XT, Y)
    A = np.dot(XTX_inv, XTY)
    return A

executar_ajuste_polinomial()