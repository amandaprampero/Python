'''
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
    Guarde esses resultados em um dicionário em Python. No final, 
    coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []
jogadores["Jogador 1"] = randint(1,6)
jogadores["Jogador 2"] = randint(1,6)
jogadores["Jogador 3"] = randint(1,6)
jogadores["Jogador 4"] = randint(1,6)

print('\033[1;33m-=-\033[m'*10)
print(f'{"VALORES SORTEADOS":^30}')
print('\033[1;33m-=-\033[m'*10)

for k, v in jogadores.items():
  print(f'O {k} tirou {v} no dado.')
  sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('\033[1;33m-=-\033[m'*10)
print(f'{"RANKING DO JOGADORES":^30}')
print('\033[1;33m-=-\033[m'*10)

for i, j in enumerate(ranking):
  print(f'{i+1}º lugar: {j[0]} com {j[1]}')
  sleep(1)
  
print('\033[1;33m-=-\033[m'*10)
print(f'O ganhador foi o {ranking[0][0]} com {ranking[0][1]} no dado.')