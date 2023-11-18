'''
Conjuntos

- Mesma regras de conjuntos Matemático

No Python os conjuntos são chamados de sets.

* sets não possuem valores duplicados;
* sets não possuem valores ordenados;
* elementos não são acessados via índice, ou seja , conjuntos não são indexados;

Conjuntos são nonspara se utilizar quandoprecisamos armazenar eleementos mas não nos importamos
com a ordenação deles. Quando não precismos se preocupar com chaves, valores e itens duplicados.

Os Conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjuntos (set) e mapas (dicionários) em python:
    - Dicionário tem chave/valor;
    - Um conjunnto tem apenas valor;
'''

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# sera ignorado sem gerar error e nao fara parte conjunto.
print('')

s = {1, 2, 3, 4, 4, 5, 2}
print(s)
print(type(s))

print('')

# Podemos interar com conjuntos
if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

print('')

# Important lembra que, nao temos valores duplicados e nao temos ordenacao
dados = 99, 2, 34, 12, 1, 44, 5, 2, 34
print(f'Tipo da variável "dados": {type(dados)}')

lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} com elementos')

conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} com elementos')

print('')

s = {1, 'b', True, 34.33, 44}
print(s, type(s))

for valor in s:
    print(valor)

print('')

# Formulário de cadastro de visitantes de um museu

cadastro = 'São Paulo', 'Catanduva', 'São João', 'São Paulo', 'Araras', 'São Paulo',
print(cadastro,
      len(cadastro),
      type(cadastro))
print('')

# Contar quantas cidades visitaram o museu.

print(len(cadastro),
      len(set(cadastro)))
print('')

# Acrescentando um elemnto no conjunto:
s = {1, 2, 3}

s.add(4)
s.add(4)
print(s)
print('')

# Removendo elemento do conjunto:
# FORMA I
print('')

s.remove(4)
print(s)
# s.remove(4) gera erro keyerror
print('')

# FORMA II
s.add(4)
s.discard(5)
print(s)
s.discard(2)
print(s)
print('')

# Copiando conjuntos
# FORMA I - Deep Copy
novo = s.copy()
novo.add(2)
print(s,
      novo
)

# FORMA II - Shallow Copy
novo = s

novo.add(2)

print(s,
      novo)
print('')

# Limpar os conjuntos com comando clear
s.clear()
print(s)
print('')

# Método matemáticos de Conjuntos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme', 'Claucio'}
estudantes_java = {'Fernando', 'Gustava', 'Julia', 'Ana', 'Patricia', 'Guilherme'}

# Verificando interceções
# FORMA I - Utilizndo o comando union
estudantes_ucademy = estudantes_python.union(estudantes_java)

print(f'{estudantes_python}', len(estudantes_python),
      f'\n{estudantes_java}', len(estudantes_java),
      f'\n{estudantes_ucademy}', len(estudantes_ucademy))
print('')

# FORMA II - Utilizando o caractere pipe

estudantes_ucademy_1 = estudantes_python | estudantes_java

print(estudantes_ucademy_1, len(estudantes_ucademy_1))
print('')

# Gerar um conjunto com as interseções dos conjuntos

# FORMA I - Comando intersection
ambos_ucadmy = estudantes_python.intersection(estudantes_java)
print(ambos_ucadmy, len(ambos_ucadmy))

# FORMA II - Comando &
ambos_ucadmy = estudantes_python & estudantes_java
print(ambos_ucadmy, len(ambos_ucadmy))
print('')

# Gerar um conjuno de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python, len(so_python))

so_java = estudantes_java.difference(estudantes_python)
print(so_java, len(so_java))