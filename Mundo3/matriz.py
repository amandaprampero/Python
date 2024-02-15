'''
    Crie um programa que declare uma matriz de dimensão 3×3 
    e preencha com valores lidos pelo teclado. No final, 
    mostre a matriz na tela, com a formatação correta.
'''
matrix = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = soma_coluna = 0

print('\033[35m**\033[m' * 20)
print('\t\tMATRIZ')
print('\033[35m**\033[m' * 20)

for linha in range(0,3):
    for coluna in range(0,3):
        matrix[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))

print('\033[35m**\033[m' * 20)
for linha in range(0, 3):
  for coluna in range(0, 3):
    if matrix[linha][coluna] % 2 == 0:
      soma_pares += matrix[linha][coluna]
    if coluna == 2:
      soma_coluna += matrix[linha][coluna]
    print(f'[{matrix[linha][coluna]:^5}]', end='')
  print()

'''
    Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
'''
print('\033[35m**\033[m' * 20)
maior = max(matrix[1])
print(f'Soma doa valores pares digitados: {soma_pares}')
print(f'A soma dos valores da terceira coluna: {soma_coluna}')
print(f'O maior valor da segunda linha: {maior}')