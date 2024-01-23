"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviçõs oferecidos pro empresas tais como:
  - Twitter, Facebook, ...)
  A comunicação a terceiros são os desenvolvedores

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))

print(ret)


print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)



"""

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')

ret = jsonpickle.encode(felix)

print(ret)

# ESCREVENDO UM ARQUIVO JSON/PICKLE
with open('felix.json', 'w') as file:
    ret = jsonpickle.encode(felix)
    file.write(ret)

# LENDO UM ARQUIVO JSON/PICKLE
with open('felix.json', 'r') as file:
    contend = file.read()
    ret = jsonpickle.decode(contend)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)