"""
Para usar o sistema de navegação em um sistema operacional precisamos importar o mesmo

import os

# Retorna o caminho absoluto ou abs path
print(os.getcwd()) # get to current work directory


os.chdir("..")
print(os.getcwd())

os.chdir("./secao_13_Leitura_escrita_arquivos")
print(os.getcwd())

print(os.path.isabs("C:/Users/clauc/PycharmProjects/guppe/secao_13_Leitura_escrita_arquivos"))
print(os.path.isabs("../secao_13_Leitura_escrita_arquivos"))
print(os.path.isabs("/secao_13_Leitura_escrita_arquivos"))

import sys

print(dir(sys))
print(os.name)
print(sys.platform)
print(sys.int_info)

os.mkdir("modificado/templates/bin/sistem")



"""

import os

print(os.getcwd())

# os.chdir(os.path.join(os.getcwd(), "modificado")) # o join irá acrescentar a pasta existente no caminho atual.
os.chdir("modificado/templates")
# print(os.getcwd())

print(os.getcwd())

os.chdir("..")
print(os.getcwd())

os.chdir(os.path.join(os.getcwd(), "templates", "bin"))
print(os.getcwd())

print(os.listdir())


os.chdir(os.path.join(os.getcwd(), "..", "..",".."))
print(os.getcwd())

print(os.listdir())
print(os.listdir()[0])
