'''
    Faça um programa que leia nome e peso de várias pessoas,
    guardando tudo em uma lista. No final mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''

pessoas = []
dado = []

while True:
  dado.append(str(input('Nome: ')))
  dado.append(float(input('Peso: ')))

  if len(pessoas) == 0:
    min = max = dado[1]
  else:
    if dado[1] > max:
      max = dado[1]
    if dado[1] < min:
      min = dado[1]
  pessoas.append(dado[:])
  dado.clear()

  resp = str(input('Quer continuar? [S/N] '))
  if resp in 'Nn':
    break

print('\033[35m*\033[m' * 40)
print(f'Foram cadastradas \033[31m{len(pessoas)}\033[m pessoas')
print('\033[35m*\033[m' * 40)
print('\033[34mLista de pessoas com peso acima de 100kg:\033[m')
for p in pessoas:
  if p[1] >= 100:
    print(f'- {p[0]} com {p[1]}kg')
print('A pessoa mais pesada é ', end = '')
for p in pessoas:
  if p[1] == max:
    print(f'{p[0]} com {max}kg')

print('\033[35m*\033[m' * 40)
print('\033[34mLista de pessoas com peso abaixo de 50kg:\033[m')
for p in pessoas:
  if p[1] <= 50:
    print(f'- {p[0]} com {p[1]}kg')
print('A pessoa mais leve é ', end = '')
for p in pessoas:
  if p[1] == min:
    print(f'{p[0]} com {min}kg')