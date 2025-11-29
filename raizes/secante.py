import math 

def executar_secante():
    print("\nDigite a função (use 'x' como variável, ex: 'x**3 - 9*x + 3'): ")
    f_str = input("f(x) = ")
    f = lambda x: eval(f_str, {'x': x, 'math': math}) 

    print("\nPrimeiro Chute Inicial (x0): ")
    try:
        x0 = float(input("x0 = "))
    except ValueError:
        print("Erro: O chute inicial deve ser numérico.")
        return

    print("\nSegundo Chute Inicial (x1): ")
    try:
        x1 = float(input("x1 = "))
    except ValueError:
        print("Erro: O chute inicial deve ser numérico.")
        return
        
    print("\nCalcular por:")
    print("1. Tolerância (Erro entre Aproximações)")
    print("2. Número de iterações")
    print("3. Geral (Tolerância padrão 1e-6, Máx. 100)")

    try:
        op = int(input())
    except:
        print("Opção inválida.")
        return

    if op == 1:
        calcular_por_tolerancia_secante(f, x0, x1)
    elif op == 2:
        calcular_por_numero_de_iteracoes_secante(f, x0, x1)
    elif op == 3:
        secante(f, x0, x1)
    else:
        print("Opção inválida.")    

    return

def calcular_por_tolerancia_secante(f, x0, x1):
    tolerancia = float(input("Tolerância = "))
    secante(f, x0, x1, tolerancia=tolerancia, max_iteracoes=1000)
    return


def calcular_por_numero_de_iteracoes_secante(f, x0, x1):
    it = int(input("Número de iterações = "))
    secante(f, x0, x1, tolerancia=1e-8, max_iteracoes=it)
    return

def secante(f, x_k_menos_1, x_k, tolerancia=1e-6, max_iteracoes=100):
    x_anterior = x_k_menos_1
    x_atual = x_k
    erro = "N/A"

    for i in range(max_iteracoes):
        try:
            f_x_atual = f(x_atual)
            f_x_anterior = f(x_anterior)
        except Exception:
            print("\nErro ao avaliar função. Verifique o domínio.")
            return None

        if abs(f_x_atual - f_x_anterior) < 1e-12:
            print("\nDenominador (f(x_k) - f(x_{k-1})) próximo de zero. O método falhou ou a tolerância é muito alta.")
            return None

        x_proximo = x_atual - f_x_atual * ((x_atual - x_anterior) / (f_x_atual - f_x_anterior))
        
        erro = abs(x_proximo - x_atual)

        if erro < tolerancia:
            break

        x_anterior = x_atual
        x_atual = x_proximo

    if i == max_iteracoes - 1 and erro >= tolerancia:
        print(f"\nNúmero máximo de iterações ({max_iteracoes}) atingido sem atingir a tolerância.")
        
    print("\n--- Resultado ---")
    print(f"Raiz aproximada: {x_proximo}")
    print(f"Iterações: {i + 1}")
    print(f"Erro: {erro}")
    
    return x_proximo

executar_secante()