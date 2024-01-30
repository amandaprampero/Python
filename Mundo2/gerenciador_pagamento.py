print('= ' * 30)
print('\t\t\t\033[1;34mLOJINHA\033[m')
print('= ' * 30)
preco = float(input('Informe o preço do produto: '))
print('\n1 - À vista em dinheiro ou cheque (\033[;32m10% de desconto\033[m)')
print('2 - À vista no cartão de crédito (\033[;32m15% de desconto\033[m)')
print('3 - Em 2x no cartão (\033[;32mSEM JUROS\033[m)')
print('4 - Em 3x no cartão (\033[;31mJUROS DE 20%\033[m)')
while True:
  op = int(input('\nForma de pagamento: '))
  if 1<=op<=4:
    break
  else:
    print('Opção inválida!')

if op == 1:
  print('\n\033[1;34mPagamento à vista em dinheiro ou cheque\033[m')
  print('\n\033[1;34mPreço final: R$ {:.2f}\033[m'.format(preco * 0.9))
elif op == 2:
  print('\n\033[1;34mPagamento à vista no cartão de crédito\033[m')
  print('\n\033[1;34mPreço final: R$ {:.2f}\033[m'.format(preco * 0.85))
elif op == 3:
  print('\n\033[1;34mPagamento em 2x no cartão\033[m')
  print('\n\033[1;34mPreço final: R$ {:.2f}\033[m'.format(preco))
  print(f'\n\033[1;34mPreço da parcela: R$ {preco/2}\033[m')
elif op == 4:
  print('\n\033[1;34mPagamento em 3x no cartão\033[m')
  print('\n\033[1;34mPreço final: R$ {:.2f}\033[m'.format(preco * 1.2))
  print(f'\n\033[1;34mPreço da parcela (3x): R$ {preco * 1.2/3:.2f}\033[m')
