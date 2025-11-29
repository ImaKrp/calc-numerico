import math
import numpy as np

def executar_rk2():
    print("\nDigite a função f(x, y) da EDO dy/dx = f(x, y):")
    f_str = input("f(x, y) = ")
    f = lambda x, y: eval(f_str, {'x': x, 'y': y, 'math': math, 'np': np}) 

    try:
        x0 = float(input("Condição inicial x0: "))
        y0 = float(input("Condição inicial y0: "))
        x_fim = float(input("Valor final de x (x_fim): "))
        n = int(input("Número de passos (n): "))
        
        if n <= 0:
            print("O número de passos deve ser positivo.")
            return
    except ValueError:
        print("Entrada inválida. Todos os valores devem ser numéricos.")
        return

    try:
        X, Y = metodo_runge_kutta_2(f, x0, y0, x_fim, n)
        
        h = (x_fim - x0) / n
        print("\n--- Resultado ---")
        print(f"Número de passos (n): {n}")
        print(f"Tamanho do passo (h): {h:.6f}")
        
        print("\nPontos da Solução Numérica:")
        print(" i |    x_i    |    y_i (aprox.)")
        print("---|-----------|------------------")
        
        for i in range(len(X)):
            print(f"{i:2} | {X[i]:.6f} | {Y[i]:.6f}")
            
        print(f"\nValor aproximado de y({x_fim:.6f}) = {Y[-1]:.6f}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução do método: {e}")

def metodo_runge_kutta_2(f, x0, y0, x_fim, n):
    h = (x_fim - x0) / n
    X = [x0]
    Y = [y0]
    
    x_i = x0
    y_i = y0
    
    for _ in range(n):
        k1 = h * f(x_i, y_i)
        k2 = h * f(x_i + h / 2, y_i + k1 / 2)
        
        y_novo = y_i + k2
        x_novo = x_i + h
        
        x_i = x_novo
        y_i = y_novo
        
        X.append(x_i)
        Y.append(y_i)
        
    return X, Y

executar_rk2()