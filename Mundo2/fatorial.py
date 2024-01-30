'''
from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''
n = int(input('Digite um número para calcular seu fatorial: '))
fat = n
res = 1
print(f'{n}! = ', end='')
while fat > 0:
  print(f'{fat}', end = '')
  print(' x ' if fat > 1 else ' = ', end='')
  res *= fat
  fat -= 1
print(f'{res}')