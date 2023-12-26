'''
Documentando funções com Docstring

OBS: Podemos ter acesso à documentação de um função em Python utilizando
a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()
'''

# Exemplo:

def diz_oi():
    """Uma função simple sem parâmetro que retorna 'Oi!'"""
    return 'Oi!'

help(diz_oi)

def exponencial(numero, potencia=2):
    """
    Funçãoque retorna por padrão o quadrado de um 'numero' ou 'numero' informado.
    :param numero:
    :param potencia:
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

help(exponencial)