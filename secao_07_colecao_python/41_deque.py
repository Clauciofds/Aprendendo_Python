'''
Módulo Collections - Deque

Um lista de alta performace
'''

from collections import deque

deq = deque('Claucio')

print(deq)

print('')

deq.append('F')
print(deq)

print('')
deq.appendleft('Dr')
print(deq)

print('')
print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)