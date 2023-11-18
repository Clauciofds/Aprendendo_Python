def media_aritimetica(valores):
    return sum(valores) / len(valores)

def media_ponderada(valores, pesos):
    soma_produto = sum(valores[i] * pesos[i] for i in range(len(valores)))
    soma_pesos = sum(pesos)
    return soma_produto / soma_pesos

def definir_nota():
    valores = []
    pesos = []
    definicao = input('Como calcular a média do Aluno:\n'
                      '\nA = média Aritimética'
                      '\nP = média Ponderada\n'
                      '\nDigite sua opção: ')
    definicao = definicao.upper()
    avaliacoes = int(input('Quantas notas serão avaliadas: '))

    for i in range(avaliacoes):
        nota = float(input('\nDigite a nota do aluno: '))
        valores.append(nota)

        if definicao == 'A':
            resultado = media_aritimetica(valores)
        elif definicao == 'P':
            peso = float(input(f'Digite o peso da nota {i+1}: '))
            pesos.append(peso)
            resultado = media_ponderada(valores, pesos)
        else:
            print('Opção inválida.')
            return

        print(f'A média é: {resultado:.1f}')


definir_nota()