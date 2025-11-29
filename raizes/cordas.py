import math

def executar_cordas():
    print("Digite a função (use 'x' como variável, ex: 'x**3 - 9*x + 3'): ")
    
    f_str = input("f(x) = ")

    f = lambda x: eval(f_str, {'x': x, 'math': math})

    print("\nIntervalo: ")
    a = float(input("a = "))
    b = float(input("b = "))

    print("\nCalcular por:")
    print("1. Tolerância (Erro do Intervalo)")
    print("2. Número de iterações")
    print("3. Geral (Tolerância padrão 1e-6, Máx. 100)")

    try:
        opcao = int(input())
    except ValueError:
        print("Opção inválida. Digite um número.")
        return

    if opcao == 1:
        calcular_por_tolerancia(f, a, b)

    elif opcao == 2:
        calcular_por_numero_de_iteracoes(f, a, b)

    elif opcao == 3:
        regula_falsi(f, a, b) 

    else:
        print("Opção inválida")
        return

    return


def calcular_por_tolerancia(f, a, b):
    tolerancia = float(input("Tolerância = "))

    regula_falsi(f, a, b, tolerancia=tolerancia, max_iteracoes=1000)


    return


def calcular_por_numero_de_iteracoes(f, a, b):
    iteracoes = int(input("Número de iterações = "))

    regula_falsi(f, a, b, tolerancia=1e-8, max_iteracoes=iteracoes)

    return


def regula_falsi(f, a, b, tolerancia=1e-6, max_iteracoes=100):
    if f(a) * f(b) >= 0:
        print("\nNão é possível garantir a existência de raiz no intervalo informado, pois f(a) * f(b) >= 0.")
        return None

    c_anterior = a 
    
    for i in range(max_iteracoes):
        try:
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        except ZeroDivisionError:
            print("\nDivisão por zero: f(b) - f(a) = 0. O método falhou (intervalo inválido ou tolerância muito baixa).")
            return None

        if abs(b - a) < tolerancia:
            break
        
        if abs(c - c_anterior) < tolerancia:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        c_anterior = c 

    if i == max_iteracoes - 1:
        print(f"\nNúmero máximo de iterações ({max_iteracoes}) atingido.")
    else:
        pass 
        
    print("\n--- Resultado ---")
    print(f"Raiz aproximada: {c}")
    print(f"Iterações: {i+1}")
    print(f"Erro no c: {abs(c - c_anterior) if i > 0 else 'N/A'}")
    
    return c

executar_cordas()