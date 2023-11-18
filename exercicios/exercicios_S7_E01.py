a = []
alteracao = ('')

for i in range(6):
    valor = int(input('Digite um valor inteiro: '))
    a.append(valor)

print(f'ÍNDICE | VALOR')
for indice, num in enumerate(a):
    print(f'{indice:>3}.......{num:>3}')

while True:
    alteracao = input('\nOs valores estão correto (S/N): ')
    alteracao = alteracao.upper()
    if alteracao == 'N':
        print(f'ÍNDICE | VALOR')
        for indice, num in enumerate(a):
            print(f'{indice:>3}.......{num:>3}')
        opcao = int(input('Escolha a posição no índice: '))
        valor_correcao = int(input('Digite o valor: '))
        a.pop(opcao)
        a.insert(opcao, valor_correcao)
        print(f'ÍNDICE | VALOR')
        for indice, num in enumerate(a):
            print(f'{indice:>3}.......{num:>3}')
    else:
        break
