import math

def executar_bisseccao():
    print("\nDigite a função (use 'x' como variável): ")
    f_str = input("f(x) = ")

    f = lambda x: eval(f_str, {'x': x, 'math': math})

    print("\nIntervalo: ")
    a = float(input("a = "))
    b = float(input("b = "))

    print("\nCalcular por:")
    print("1. Tolerância")
    print("2. Número de iterações")
    print("3. Geral")

    opcao = int(input())

    if opcao == 1:
        calcular_por_tolerancia(f, a, b)

    elif opcao == 2:
        calcular_por_numero_de_iteracoes(f, a, b)

    elif opcao == 3:
        bisseccao(f, a, b)

    else:
        print("Opção inválida")
        return

    return


def calcular_por_tolerancia(f, a, b):
    tolerancia = float(input("Tolerância = "))

    bisseccao(f, a, b, tolerancia=tolerancia, max_iteracoes=1000)

    return


def calcular_por_numero_de_iteracoes(f, a, b):
    iteracoes = int(input("Número de iterações = "))

    bisseccao(f, a, b, tolerancia=1e-6, max_iteracoes=iteracoes)

    return


def bisseccao(f, a, b, tolerancia=1e-6, max_iteracoes=100):
    for i in range(max_iteracoes):
        c = (a + b) / 2

        if abs(b - a) < tolerancia:
            break
        
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    

    print("\nRaiz aproximada: " + str((a+b)/2) + " (em " + str(i+1) + " iterações)")
    
    return (a+b)/2

executar_bisseccao()