from math import gcd as mdc

def determina_fracao(numerador, denominador):
    # Entrada dos termos da fração
    numerador = int(input('Digite o numerador da fração: '))
    denominador = int(input('Digite o denominador da fração: '))

    # Imprimi o resultado do MDC da fração
    if numerador > 0 and denominador > 0:
        mdc_numerador, mdc_denominador = mdc_fracao(numerador, denominador)
        return print(f'\nO MDC da fração é {mdc_numerador}'
                     f'\nA fração simplificada é: {int(numerador / mdc_numerador)}/{int(denominador / mdc_denominador)}')
    else:
        print('Valores inválidos')

    # Irá imprimir a soma, subtração, o produto e o quociente entre as fraçóes lidas.
    print(resultado_da_fracao())


# Calculando o MDC
def mdc_fracao(p, q):
    # Calcula o MDC dos numeradores e denominadores
    mdc_numerador = mdc(p, q)
    mdc_denominador = mdc(q, p)

    # Retorna o MDC dos numeradores e denominadores
    resultado_da_fracao(numerador=1, denominador=2)
    return (mdc_numerador, mdc_denominador)

def resultado_da_fracao(numerador, denominador):
    print(
          f'\nA soma do numerador e denominador é: {numerador + denominador}'
          f'\nA subtração do numerador e denominador é: {numerador - denominador}'
          f'\nO produto da fração é: {numerador * denominador}'
          f'\nO cociente da fração é: {numerador / denominador}'
          )

determina_fracao(numerador=1, denominador=2)