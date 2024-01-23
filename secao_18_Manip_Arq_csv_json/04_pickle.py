"""
Conhecendo o Pickle

A função do Pickle:

Objeto Python .> Binarização

Binarização -> Objeto Python

Processos chamado serialização/deserialização

== OBS: O módulo Pickle não é seguro contra dados maliciosos e deste forma
não é recomendado trabalhor com arquivos pickle vindos de outra pessaos
que você não conheça ou de fontes desconhecidas.

# ESCRITA DE ARQUIVOS PICKLES
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as file:
    pickle.dump((felix, pluto), file)



"""
import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

# LENDO PICKLE
with open('animais.pickle', 'rb') as file:
    gato, cachorro = pickle.load(file)
    print(f'O gata chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {typ
    
    e(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
