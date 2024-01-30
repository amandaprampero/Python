print('=='*20)
print('\t\t\033[35mBANCO CEV\033[m')
print('=='*20)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
  if total >= ced:
    total -= ced
    totced += 1
  else:
    if totced > 0:
      print(f'Total de {totced} cédulas de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totced = 0
    if total == 0:
      break
print('=='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
