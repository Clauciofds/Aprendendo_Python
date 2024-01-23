"""
Manipulando Data e hora.

O python tem um módulo bult-in de data hora:
-> datetime

import tkinter as tk
from time import strftime

def atualizar_relogio():
    tempo_str = strftime('%H:%M:%S %p')  # Formato da hora
    label_relogio.config(text=tempo_str)
    root.after(1000, atualizar_relogio)  # Atualizar a cada 1000 milissegundos (1 segundo)

# Criar janela principal
root = tk.Tk()
root.title("Relógio Digital")

# Configurar label para exibir o relógio
label_relogio = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_relogio.pack(anchor='center')

# Iniciar o relógio
atualizar_relogio()

# Executar a aplicação
root.mainloop()

while True:
    clock = time.strftime('%H:%M:%S')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Relógio: {clock}')
    time.sleep(1)




"""

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)  # 9999
print(datetime.MINYEAR)  # 1

# Retorna data e hora conrrente
print(datetime.datetime.now())  # 2024-01-14 12:54:45.397406

print(repr(datetime.datetime.now()))  # datetime.datetime(2024, 1, 14, 12, 56, 56, 948619)

# replace() para fazer ajustes na data/hora
start = datetime.datetime.now()

print(start)

# Alterando o horário para 16 horas, o min, 0 s, 0 ms
start = start.replace(year=2025, hour=16, minute=0, second=0, microsecond=0)
print(start)

evento = datetime.datetime(2024, 1, 1, 0)
print(evento)

print(type(evento))
print(type('31/12/2018'))

# nascimento = input('Data (dd/mm/aaaa): ')
#
# nascimento = nascimento.split('/')
#
# nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

# print(nascimento)

evento = datetime.datetime.now()

print(evento.year)
print(evento.microsecond)

print(dir(evento))