'''
Definindo Funções

- Pequenos trechos de códigos que realizam tarefas específicas
- Pode ou não receber entradas de dados e retornar um saída de dados
- Executa varias vezes a mesma tarefa chamando essa função

'''

# Exemplo de utilização de funçoes:

# cores = ['verde', 'amaelo', 'azul', 'branco']
#
# print(cores)
#
# curso = 'Programação em Python Essecia'
# print(curso)
#
# print('')
# cores.append('roxo')
# print(cores)
#
# print('')
# curso.append('Mais dados') AttributeError

'''
DEFININDO FUNÇÕES

def - nome da função(parâmetro_de_entrada):
    bloco_da_função
    
nome_da_funcao -> SEMPRE com letras minúsculas e separadas por undeline (Snake Case)

bloco_da_funcao -> Corpo da Funcao ou implementacao, onde é feito o processamento da função com ou sem retorno.

'''

def diz_oi():
    print('\nOi')

diz_oi()

for i in range(5):
    diz_oi()

