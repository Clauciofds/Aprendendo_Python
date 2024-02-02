"""
Unittest - Antes e após hooks

----
hooks - são os teste em si. Ou seja, a execução dos testes.
----

setup() -> é executado antes de cada método de teste. É utila para criarmos instâncias de objetos e outros dados:

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexão com
bancos de dados.


"""

import unittest

class ModuloTes(unittest.TestCase):
    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setup vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def terDown(self):
        # Configurações do tearDown()
        pass