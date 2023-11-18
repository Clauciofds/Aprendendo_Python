'''
OrderedDict -> É um dicionário que nos garante a ordem de inserçõo dos elementos.
'''
from collections import OrderedDict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True por que o ordem nao e considerada

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False por que neste caso a ordem importa

