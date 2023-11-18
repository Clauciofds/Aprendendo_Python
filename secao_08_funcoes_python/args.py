"""
Entendendo o *args

-  O *args é um parâmetro, como outro qualquer. Isso significa que
   você poderá definir qualquer nome, desde que começe com o asterisco.

*xis

Mos o que é o *args?

O parâmetro *args utilizao em um função, coloca os valores extras informados como
entrada em um tupla. Então desde já lembre-se que tuplas são imtáveis.

"""

# Exemplo

def soma_todos_numero(num1, num2, num3):
    return print(num1 + num2 + num3)

# soma_todos_numero() # Desta for irá dar TypeError

soma_todos_numero(1, 2, 3)

print("")

# Utilizando *args

def soma_numeros(*args):
    print(f'\n{args}')
    # total = 0
    # for num in args:
    #     total += num
    # return print(f'\n{total}')
    return print(f'{sum(args)}')

soma_numeros()
soma_numeros(1)
soma_numeros(1, 2)
soma_numeros(1, 2, 3)

# Exemplo

def cadastro(nome, email, *args):
    print(" ")
    print(nome, email)
    return print(f'{sum(args)}')

cadastro('Claucio', 'clauci@htomial.com')
cadastro('Cleiton', 'cleito@hotmail.com', 1, 2, 3, 4)

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return print('\nBem-vindo Geek')
    return print('\nEu nao tenho certeza...')

verifica_info()
verifica_info(1, True, 'University', 'Geek')
verifica_info(1, 'University', 4.333)

# Desepacotamente com uso do asterisco


numeros = (1, 2, 3, 4, 5, 6, 7)

# soma_numeros(numeros) # não soma porque a lista é um unico objeto

soma_numeros(*numeros)

