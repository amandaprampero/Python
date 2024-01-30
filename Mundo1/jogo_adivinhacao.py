from random import randint
from time import sleep

n = int(input('Adivinhe um número entre 0 e 5: '))
m = randint(0,5)
print('Processando...')
sleep(1)
if m == n:
  print(f'Você acertou! Pensei no número {m}.')
else: 
  print(f'Errou :( Pensei no número {m}.')