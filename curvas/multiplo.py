import numpy as np

def executar_minimos_quadrados_multiplo():
    try:
        n = int(input("\nDigite o número de pontos de dados (observações): "))
        if n < 2:
            print("São necessários pelo menos 2 pontos.")
            return
            
        m = int(input("Digite o número de variáveis independentes (m): "))
        if m < 1:
            print("É necessária pelo menos 1 variável independente.")
            return
            
        if n <= m:
            print(f"O número de observações ({n}) deve ser maior que o número de variáveis ({m}).")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return

    Y = []
    X_data = []
    
    print("\n--- Entrada de Dados ---")
    
    for i in range(n):
        while True:
            try:
                entrada = input(f"Observação {i + 1} - Digite {m} valores X e o valor Y (Ex: x1 x2 ... xm y): ").split()
                if len(entrada) != m + 1:
                    print(f"Erro: Forneça exatamente {m+1} valores.")
                    continue
                
                valores = [float(val) for val in entrada]
                X_data.append(valores[:m])
                Y.append(valores[m])
                break
            except ValueError:
                print("Erro: Todos os valores devem ser numéricos. Tente novamente.")

    try:
        X_data = np.array(X_data, dtype=float)
        Y = np.array(Y, dtype=float).reshape(n, 1)
        
        coluna_uns = np.ones((n, 1), dtype=float)
        X = np.hstack((coluna_uns, X_data))
        
        coeficientes = minimos_quadrados_multiplo(X, Y)
        
        print("\n--- Resultado do Ajuste ---")
        print(f"Coeficiente a0 (Intercepto): {coeficientes[0, 0]:.6f}")
        
        equacao = f"y = {coeficientes[0, 0]:.6f}"
        for i in range(1, m + 1):
            print(f"Coeficiente a{i} (Variável x{i}): {coeficientes[i, 0]:.6f}")
            equacao += f" + {coeficientes[i, 0]:.6f}x{i}"
            
        print(f"\nModelo de Regressão: {equacao}")
        
    except np.linalg.LinAlgError:
        print("\nErro: A matriz (X^T X) é singular e não pode ser invertida. Há dependência linear entre as variáveis.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

def minimos_quadrados_multiplo(X, Y):
    XT = X.T
    XTX = np.dot(XT, X)
    XTX_inv = np.linalg.inv(XTX)
    XTY = np.dot(XT, Y)
    A = np.dot(XTX_inv, XTY)
    return A

executar_minimos_quadrados_multiplo()