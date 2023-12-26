'''
Funções com Parâmetro Padrão (Default Paramters)

'''

def quadrado(num):
    return print(f'\n{num ** 2}')

quadrado(5)
# quadrado() -> A função exige que haja um parâmetro, se não irá havar um TypeError:

def exponencial(nume=0, pontencial=2): # Se determinado um valor padrão não haverá TypeError
    return print(f'\n{nume ** pontencial}')

exponencial(2, 3)
exponencial(3, 4)

exponencial(10)
exponencial()

exponencial(pontencial=3)

def mostrae_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return print('\nBem-vindo instrutor Geek')
    elif nome == 'Geek':
        return print('\nEu pensei que voce era instrutor')
    return print(f'\nOla {nome}')

mostrae_informacao()
mostrae_informacao(instrutor=True)
mostrae_informacao(True)
mostrae_informacao('Ozzy')
mostrae_informacao(nome='Stephany')

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2 , fun=soma):
    return print(f'\n{fun(num1, num2)}')

def subtracao(num1, num2):
    return num1 - num2

mat(2, 3)
mat(2, 2, subtracao)

# Escopo

# Variáveis globais
# Variáveis locais

instrutor = 'Claucio'

def diz_oi():
    instrutor = 'Pythont' # Variável local sempre terá prioridade de uso
    return print(f'\nOi {instrutor}')

diz_oi()


def diz_oi1():
    prof = 'Claucio' # variavel local
    return print(f'\nOla {prof}')

diz_oi1()
# print(prof)


# ATENÇÃO com variáveis globais (Se puder evitar, evite)

total = 0

def incrementa():
    global total
    total += 1
    return print(f'\n{total}')

incrementa()
incrementa()
incrementa()

# Podemos ter funcoes que s'ao delcaradas dentro de funcoes, e tambem tem uma forma especial de escopo de vairavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return print(f'\n{dentro()}')

fora()
fora()
fora()