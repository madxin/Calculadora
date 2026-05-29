import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '**':
        result = num1 ** num2
    elif operador == '%':
        result = num1 % num2

    return result

def calculadora_v2(num1: float, num2: float, operador: str) -> float:

    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '**': lambda a, b: a ** b,
        '%': lambda a, b: a % b
    }

    if operador in operacoes:
        return operacoes[operador](num1, num2)

    return float("nan")

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')

            num1 = float(input('Primeiro número: '))
            num2 = float(input('Segundo número: '))
            operador = input('Operador (+, -, *, /, **, %): ')

            opcao = input(
                'Escolha a funcao (1-calculadora / 2-calculadora_v2): '
            )

            if opcao == '2':
                resultado = calculadora_v2(num1, num2, operador)
            else:
                resultado = calculadora(num1, num2, operador)

            resultado = calculadora(num1, num2, operador)

            print(f'\nResultado: {resultado}')

            
            continuar = input(
                '\nDeseja efetuar outra operacao? (s/n): '
            ).lower()

            if continuar != 's':
                break    


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
