from statistics import mean as md

# Definir uma lista global para armazenar os cadastros da pesquisa
inf_pesquisa = []

def dados_pesquisa(sexo, cor_dos_olhos, idade):
    """
    A função monta o banco de dados da pesquisa através de um dicionário onde guarda um biblioteca com
    a seguinte classificação:

    :param sexo: deve entra com uma string unica 'M' ou 'F';
    :param cor_dos_olhos: descreve com uma unica string, exemplo: 'verde';
    :param idade: um número interio int()
    :return: Verifica se o código tem a saída correta, pode ser ignorada opcionalmente.
    """

    # Definir a quantidade de cadastro serão processados
    quant_pesquisado = int(input('Qual tamanho da pesquisa?\n'
                                 'Digite a quantidade: '))

    chaves = ['sexo', 'cor_dos_olhos', 'idade']
    banco = []

    # Entrada do usuário com os informações
    for loops in range(quant_pesquisado):
        dados = []

        # Inserindo e manipulando os dados da pesquisa
        dado = input('\nSexo (Feminino = F / Masculino = M / Outro = O):'
                           '\nOpção: ')
        dado = dado.upper()
        dados.append(dado)

        dado = input('Cor dos  olhos (Azuis = A / Verdes = V / Castanhos = C):'
                                    '\nOpção: ')
        dado = dado.upper()
        dados.append(dado)

        dado = int(input('Idade: '))
        dados.append(dado)

        banco.append(dados)

    # Transformado os dados cadastrados em um dicionário usando dictionary comprehension (BD (Banco de Dados))
    inf_pesquisa = [{chaves[i]: dado[i] for i in range(len(chaves))} for dado in banco]

    media_idade(inf_pesquisa)
    faixa_etaria_feminina(inf_pesquisa)
    return inf_pesquisa

def media_idade(inf_pesquisa):
    somatoria = [dado['idade'] for dado in inf_pesquisa]
    resultado = md(somatoria)
    return print(f"\nA média de idade dos pesquisados é: {int(resultado)}"
                 f"\nA pessoa mais velha na região tem {max(dado['idade'] for dado in inf_pesquisa)} anos.")

# Função que determina o número de mulher entre 18 e 35 anos com olhos azuis.
def faixa_etaria_feminina(inf_pesquisa):
   # Lista com o numero de mulheres seguindo a regra determinada através da função if e o for.
   faixa_etaria = [
       dado['idade'] for dado in inf_pesquisa
       if dado['sexo'] == 'F' and 18 <= dado['idade'] <= 35 and dado['cor_dos_olhos'] == 'A'
   ]

   # Contando o resultado
   count_feminino = len(faixa_etaria)
   return print(f'\nA pesquisa detectou {count_feminino} entre 18 a 35 anos e olhos azuis.')

# Chamando a função para iniciar o cadastro e compilar a pesquisa
dados_pesquisa(sexo='M', cor_dos_olhos='Verde', idade=1)