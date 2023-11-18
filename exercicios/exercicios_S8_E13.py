from functools import reduce

def definir_valores(*args):
    amostra = []

    quantidade = int(input('Quantos números serão processados? '))
    for i in range(quantidade):
        valor = float(input('Digite um número: '))
        amostra.append(valor)

    operacao = input('\n- Qual operção será executada com os valores?'
                     '\n>> Soma          = So.'
                     '\n>> Subtração     = Su.'
                     '\n>> Multiplicação = Mu.'
                     '\n>> Divisão       = Di.\n'
                     '\n>> Digite sua opção: ')
    operacao = operacao.title()

    if operacao == 'So':
        amostra = tuple(amostra)
        return print(f'>> A soma dos números é: {soma_num(*amostra)}')
    elif operacao == 'Su':
        return print(f'>> O resultado da subtração é: {subtracao(args)}')
    elif operacao == 'Mu':
        return print(f'>> O resultado da multiplicação é: {multiplica(*amostra)}')
    elif operacao == 'Di':
        return print(f'>> O resultado da divisão é: {divisao(amostra)}')

def soma_num(*amostra):
    return sum(amostra)

def subtracao(*amostra):
    resultado = 1
    for numero in amostra:
        resultado *= numero
    return resultado

def multiplica(*amostra):
    resultado = reduce(lambda x, y: x * y, amostra)
    return resultado

def divisao(amostra):
    return amostra[0] / amostra[1]


definir_valores()

