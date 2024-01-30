print('=-' * 20)
print('\t\t\033[;32mCONVERSOR DE BASES\033[m')
print('=-' * 20)
print('Converter para:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n')
while True:
  op = int(input('\nDigite a opção: '))
  if 1<=op<=3:
    break
  else:
    print('Opção inválida. Tente novamente.')
    
n = int(input('Digite um número inteiro: '))
#[2:] tira a base da string
if op == 1:
  print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}') #0b
elif op == 2:
  print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}') #0o
elif op == 3:
  print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:].upper()}') #0x
