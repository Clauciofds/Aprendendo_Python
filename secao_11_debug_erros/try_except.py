"""
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Preveindo assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperados.

A forma geral mais simples é:

try:
    //execução problemática
except:
    // o que deve ser feiro em caso de falha da primeira tentativa.

"""
from colorama import Fore
# Exemplo 1 = Tratando um erro genérico.

try:
    geek()
except:
    print("Deu algum problema")

# Tratar erros de forma genérica não é a melhor ação. O ideal é sempre tratar de forma especifica.

# Exemplo 2 - Tratando um erro específico.

try:
    len(5)
except TypeError:
    print("Você esta utilizando um função inexistente")


try:
    len(5)
except TypeError as err: # nomeando uma vareável para os erros.
    print(f"A aplicação gerou o seguinte erro: {err}")

"""
Exercício.
try:
    input(int(input("Digite um número: ")))
except ValueError as err:
    print(f"Digite um número inteiro: {err}")
"""

try:
    # print("Geek"[9])
    # Geek()
    len(5)
except NameError as errName:
    print(f"Deu NameError: {errName}")
except TypeError as errType:
    print(f"Deu TypeError: {errType}")
except:
    print("Deu um erro difente")

print(f'\n{Fore.LIGHTBLUE_EX}')
      
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except TypeError:
        return None
    except KeyError:
        return None
    except NameError:
        return None

dic = {'nome': 'Geek'}
       
print(pega_valor(dic, 'Geek'))