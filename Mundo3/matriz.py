'''
    Crie um programa que declare uma matriz de dimensão 3×3 
    e preencha com valores lidos pelo teclado. No final, 
    mostre a matriz na tela, com a formatação correta.
'''
matrix = [[0,0,0], [0,0,0], [0,0,0]]

print('\033[35m**\033[m' * 20)
print('\t\tMATRIZ')
print('\033[35m**\033[m' * 20)

for linha in range(0,3):
    for coluna in range(0,3):
        matrix[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))

print('\033[35m**\033[m' * 20)
for linha in range(0, 3):
  for coluna in range(0, 3):
    print(f'[{matrix[linha][coluna]:^5}]', end='')
  print()
