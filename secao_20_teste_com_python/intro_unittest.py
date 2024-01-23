"""
Introduçao ao módulo Unittest

Unittest -> Teste Unitários

O que são teste unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais pode ser: funções, métodos, classes, módulos etc.

#  OBS.: Teste unitário não é especificco da linguagem Python.

Para criar nossos testes, criamos classes que pherdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

link para assetions: https://docs.python.org/3/library/unittest.html

Method                      Checks that             New in

assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b                  3.1
assertIsNot(a, b)           a is not b              3.1
assertIsNone(x)             x is None               3.1
assertIsNotNone(x)          x is not None           3.1
assertIn(a, b)              a in b                  3.1
assertNotIn(a, b)           a not in b              3.1
assertIsInstance(a, b)      isinstance(a, b)        3.2
assertNotIsInstance(a, b)   not isinstance(a, b)    3.2

IMPORTANTE:
    -> Por convenção, todos os teste em um test case, deve ter seu nome
    iniciado com test_

"""

# Utilizando a aobordade TDD