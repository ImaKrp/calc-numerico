from sympy import symbols, diff, lambdify, cos, sin, exp, log, tan, pi
import math

def executar_newton():
    print("\nDigite a função (use 'x' como variável, ex: 'x**3 - 9*x + 3'): ")
    f_str = input("f(x) = ")

    print("\nChute Inicial (x0): ")
    try:
        x0 = float(input("x0 = "))
    except ValueError:
        print("Erro: O chute inicial deve ser numérico.")
        return
        
    try:
        x = symbols('x')

        symbolic_functions = {
            'x': x, 
            'cos': cos, 'sin': sin, 'tan': tan,
            'exp': exp, 'log': log, 'pi': pi,
            'math': {'cos': cos, 'sin': sin, 'exp': exp, 'log': log} 
        }
        
        f_simbolica = eval(f_str, {}, symbolic_functions)
        
        df_simbolica = diff(f_simbolica, x)

        f = lambdify(x, f_simbolica, 'math')
        df = lambdify(x, df_simbolica, 'math')
        
        print(f"\nDerivada automática: f'(x) = {df_simbolica}")
        
    except Exception as e:
        print(f"\nErro ao processar a função: {e}")
        return

    print("\nCalcular por:")
    print("1. Tolerância")
    print("2. Número de iterações")
    print("3. Geral (1e-6, 100)")

    try:
        op = int(input())
    except:
        print("Opção inválida.")
        return

    if op == 1:
        calcular_por_tolerancia_newton(f, df, x0)
    elif op == 2:
        calcular_por_numero_de_iteracoes_newton(f, df, x0)
    elif op == 3:
        newton(f, df, x0)
    else:
        print("Opção inválida.")    


def calcular_por_tolerancia_newton(f, df, x0):
    tolerancia = float(input("Tolerância = "))
    newton(f, df, x0, tolerancia=tolerancia, max_iteracoes=1000)


def calcular_por_numero_de_iteracoes_newton(f, df, x0):
    it = int(input("Número de iterações = "))
    newton(f, df, x0, tolerancia=1e-8, max_iteracoes=it)


def newton(f, df, x0, tolerancia=1e-6, max_iteracoes=100):
    x_k = x0
    erro = "N/A"

    for i in range(max_iteracoes):
        try:
            f_xk = f(x_k)
            df_xk = df(x_k)
        except:
            print("\nErro ao avaliar função. Verifique se o chute inicial é válido para o domínio da função.")
            return None

        if abs(df_xk) < 1e-12:
            print("\nDerivada próxima de zero. Método falhou.")
            return None

        x_k1 = x_k - f_xk / df_xk
        erro = abs(x_k1 - x_k)

        if erro < tolerancia:
            break

        x_k = x_k1

    print("\n--- Resultado ---")
    print(f"Raiz aproximada: {x_k1}")
    print(f"Iterações: {i+1}")
    print(f"Erro: {erro}")

    return x_k1


executar_newton()