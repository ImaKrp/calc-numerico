import numpy as np

def executar_minimos_quadrados():
    try:
        n = int(input("\nDigite o número de pontos (n) que você possui: "))
        if n < 2:
            print("São necessários pelo menos 2 pontos para o ajuste linear.")
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
        a0, a1 = minimos_quadrados_linear(X, Y, n)
        
        print("\n--- Resultado do Ajuste ---")
        print(f"Coeficiente Angular (Inclinação): a1 = {a1:.6f}")
        print(f"Coeficiente Linear (Intercepto): a0 = {a0:.6f}")
        print(f"\nReta de Melhor Ajuste: y = {a0:.6f} + {a1:.6f}x")
        
    except ValueError as e:
        print(f"\nErro de cálculo: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

def minimos_quadrados_linear(X, Y, n):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    soma_x = np.sum(X)
    soma_y = np.sum(Y)
    soma_x2 = np.sum(X**2)
    soma_xy = np.sum(X * Y)

    denominador = n * soma_x2 - soma_x**2
    if denominador == 0:
        raise ValueError("Todos os valores de X são iguais. Não é possível realizar regressão linear.")
    
    numerador_a1 = n * soma_xy - soma_x * soma_y
    a1 = numerador_a1 / denominador

    media_x = soma_x / n
    media_y = soma_y / n
    
    a0 = media_y - a1 * media_x
    
    return a0, a1

executar_minimos_quadrados()