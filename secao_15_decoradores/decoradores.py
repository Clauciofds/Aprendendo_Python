"""
Decoradores (Decorators)

- Decorators são funções
- Envolvem outras funções e aprimoram seus comportamentos
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)


-----------------------------------------------------
-            Function Decorator                     -
-----------------------------------------------------

-----------------------------------------------------
-----------------------------------------------------
--                  Função                         --
-----------------------------------------------------
-----------------------------------------------------


"""
from colorama import Fore


# Sintaxa não recomendade
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer voce")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo

def saudacao():
    print('Seja bem-vindo(a)')

# Testando 01
teste = seja_educado(saudacao)

teste()

# saudacao()


print(Fore.LIGHTGREEN_EX)

# Teste 02

def raiva():
    print('EU TI ODEIO')

raiva()


# Decorators com Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

print(Fore.LIGHTRED_EX)
# Testando 03

apresentando()


print(Fore.LIGHTCYAN_EX)


@seja_educado_mesmo
def vergonha():
    print('Que vergonha')

vergonha()


print(Fore.LIGHTYELLOW_EX)


