#jokenpô
from random import randint
itens = ('pedra', 'papel', 'tesoura')
print('=-'*20)
print('\t\033[1;35mBem vindo ao jokenpô!\033[m')
print('=-'*20)
print('\033[1;34mOpções:\033[m')
print('\033[1;36m[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura\033[m')
j = int(input('Sua jogada: '))
c = randint(0,2)

if c == j:
  print('\nEMPATE! Ninguém ganhou.')
elif (c == 1 and j == 2) or (c == 2 and j == 0) or (c == 0 and j == 1):
  print('\nJogador ganhou!')
elif (c == 1 and j == 0) or (c == 0 and j == 2) or (c == 2 and j == 1):
  print('\nComputador ganhou!')
print('\nComputador jogou {}'.format(itens[c]))
print(f'Jogador jogou {itens[j]}')
