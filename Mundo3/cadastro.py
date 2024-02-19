'''
    Crie um programa que leia nome, sexo e idade de várias pessoas, 
    guardando os dados de cada pessoa em um dicionário e todos os 
    dicionários em uma lista. No final, mostre: 
    A) Quantas pessoas foram cadastradas 
    B) A média de idade 
    C) Uma lista com as mulheres 
    D) Uma lista de pessoas com idade acima da média
'''

dados = {}
pessoas = []
soma = media = 0

while True:
  nome = str(input('Nome: '))
  idade = int(input('Idade: '))
  while True:
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo not in 'FM':
      print('ERRO! Por favor, digite apenas F ou M.')
    else:
      break
      
  dados['nome'] = nome
  dados['idade'] = idade
  dados['sexo'] = sexo
  pessoas.append(dados.copy())

  while True: 
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op not in 'SN':
      print('Opção inválida. Tente novamente.')
    else:
      break

  if op == 'N':
    break

print('\033[34m=-\033[m' * 20)
print('Foram cadastradas', len(pessoas), 'pessoas.')
print('\033[34m=-\033[m' * 20)
print(f'{"LISTA DE MULHERES":^30}')

for p in pessoas:
  soma += p['idade']
  media = soma / len(pessoas)
  if p['sexo'] == 'F':
    print(f'- {p["nome"]}')

print('\033[34m=-\033[m' * 20)
print(f'A média de idade é {media:.2f}')
for p in pessoas:
  if p['idade'] > media:
    print(f'{p["nome"]} está acima da média, com {p["idade"]} anos.')