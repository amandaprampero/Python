print('\033[;34m= \033[m' * 20)
print('\t\tTABUADA')
print('\033[;34m= \033[m' * 20)

n = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
  print('{} X {} = {}'.format(i, n, i*n))
print('FIM')