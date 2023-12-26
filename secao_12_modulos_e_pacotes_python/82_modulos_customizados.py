"""
Módulos Customizados

São nada mais que arquivos Python que escrevemos e podemos utilizar em outros códigos

"""
import sys
sys.path.append("/Users/clauc/PycharmProjects/guppe")


from secao_08_funcoes_python.funcoes_com_parametro import soma_impares

dados =  [1, 2, 3, 4, 5, 6]

print(soma_impares([1, 2, 3, 4, 5]))
