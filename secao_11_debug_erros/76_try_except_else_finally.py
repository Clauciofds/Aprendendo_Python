"""
Try / Except / Else / Finally

Dica: Toda entrada de usuário ou qualquer outro tipo de entrada DEVE ser tratada.



"""
# num = None

# while num is None:
#     try:
#         num = int(input('Informe um número: '))
#         if num >= 0:
#             print(f'Você digitou {num}')
#     except ValueError:
#         print('Valor incorreto')

# num = None

# while num is None:
#     try:
#         num = int(input('Informe um número: '))
#     except ValueError:
#         print('Valor incorreto!')
#     # É executado somente se não ocorrer o erro.
#     else:
#         print('Finalmente você acertou. Parabéns!')
#     finally:
#         print(f'Você digitou {num}')


# Finally
# try:
#     num = int(input('Informe um número: '))
# except ValueError:
#     print('Valor inválido!')
# else:
#     print(f'Você digitou {num}')
# # O bloco sempre é executado independete do que ouve acima.
# # O finally, geramente é utilizado para fechar ou desalocar recursos.
# finally:
#     print('Parabens você acertou, finalmente!')


# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except ValueError:
#         return 'Valor incorreto!'
#     except ZeroDivisionError:
#         return 'Valor nao pode ser divido por zero!'
    
# num1 = input('Informe um numero: ')
# num2 = input('Inform outro numero: ')

# print(dividir(num1, num2))

num1 = None
num2 = None

def dividir(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError as err:
        return f'Valor invalido: {err}!'
    
while (num1 and num2) is None:
    try:
        num1 = int(input('Informe um numero: '))
        num2 = int(input('Informe outro numero: '))
    except ValueError as err:
        print(f'Valores incorreto: {err}')

print(dividir(num1, num2))