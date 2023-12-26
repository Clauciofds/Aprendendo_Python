'''
Módulo Collections - Counter (Contador)

Conta as ocorrências de de um elemento criando um objeto do tipo Collections Counter
'''

from collections import Counter

# LISTA
lista = [1, 1, 2, 3, 4, 4, 3, 1, 2, 4, 4, 5, 1, 6, 6, 1]

res = Counter(lista)
print(res, type(res))

print('')

# STRING
print(Counter('Claucio Fernando Donizete dos Santos'))

print('')

# TEXTO

texto = ''' 
A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na 
internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, 
que todos possam editar e melhorar. O projeto é definido pelos princípios fundadores e o conteúdo é disponibilizado 
sob a licença Creative Commons BY-SA e pode ser reutilizado sob a mesma licença, desde que respeitando os termos de 
uso. Todos podem publicar conteúdo on-line desde que criem uma conta e sigam as regras básicas, como verificabilidade 
ou notoriedade.
'''

palavras = texto.split()

res = Counter(palavras)
print(res)

print('')

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
print(len(res))