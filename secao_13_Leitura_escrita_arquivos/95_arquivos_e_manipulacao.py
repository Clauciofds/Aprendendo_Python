"""
print(os.getcwd())
# Verifica a existencia de arquivos -- path relativo
print(os.path.exists('arquivo.txt'))
print(os.path.exists('texto.txt'))
print(os.path.exists('modificado\\arquivo.txt'))

# -- path absoluto para o windows
print(os. path.exists(
    'C:\\Users\clauc\PycharmProjects\guppe\secao_13_Leitura_escrita_arquivos\\arquivo1.txt')
)

# Criando arquivos
open('modificado\\teste.txt', 'a').close() # pode-se usar o mod 'a' ou 'w'

# se a possibilidade de um arquivo já existir o ideal e usar o código desta forma.
with open('modificado\\teste.txt', 'w') as arquivo:
    pass

# os.mknod('modificado\\templates\\texto.txt') Está função só funciona no linux

# Criando diretórios
os.mkdir('modificado\\templates')

# Criando um estrutura de diretórios.
os.makedirs('modificado\\templates\sistema\\bin', exist_ok=True)
os.makedirs('modificado\\templates\system', exist_ok=True)

#renomeando pastas
os.rename('modificado\\templates\\system', 'modificado\\templates\\sys')
os.rename('modificado\\templates\\sistema\\bin', 'modificado\\templates\\sistema\\bin1')
os.rename('arquivo.txt', 'aquivos_modificado.txt')

# Apagar arquivos de um subpasta
diretorio = os.path.abspath('modificado\\templates')
print(diretorio)

for arquivo in os.scandir(diretorio):
    os.remove(arquivo.path)

import shutil
# Removendo subpastas e arquivos de um estrutura.
for arquivo in os.scandir(os.path.abspath('modificado')): # Verifica se há arquivos na raiz.
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file(): # Veririfica se há subpastas
        shutil.rmtree(arquivo.path) # ATENÇÃO: Exclui todas as subpasta e seus conteúdos recurcivamente

# Removendo diretórios
os.rmdir('modificado\\templates\\sys')

direct = os.path.abspath("modificado\\templates")
print(direct)

for arquivo in os.scandir(os.path.abspath("modificado\\templates")): # Verifica a estrutura e cria o caminha absoluto
    if arquivo.is_file(): # Verifia se há arquivo no caminho e apaga os arquivos da pasta especificada
        os.remove(arquivo.path)
    if arquivo.is_dir(): # Verifica se há pastas no caminho especificado
        try:
            os.rmdir(arquivo.path) # Se as pastas estiverem vazias são removidas
        except OSError as err: # Se não estiverem vazias, deve se confirmar a remoção das mesma
            print(err)
            confirmacao = input("Confirme limpeza da estrutura (S ou N)\n")
            confirmacao = confirmacao.upper()
            if confirmacao == "S":
                if not arquivo.is_file(): # ATENÇÃO: A função shutil remove todo conteúdo da estrutura de forma recusiva
                    shutil.rmtree(arquivo.path)
                    print("Pastas e Arquivos Excluídos!")

from send2trash import send2trash

send2trash("modificado\\templates\\bin\\system")

# Diretório e arquivos temporários
with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretorio temporario em {tmp}")
    with open(os.path.join(tmp, "arquivo_temporario.txt"), "w") as arquivo:
        arquivo.write("Geek Univesity\n")
    input()

import tempfile

# Criando arquivos temporários binários
with tempfile.TemporaryFile() as tmp:
    tmp.write(b"Claucio Santos")
    tmp.seek(0)
    print(tmp.read())

https://docs.python.org/3/library/os.html?highlight=os#module-os

"""

import os
import sys
