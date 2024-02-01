'''Crie um programa onde o usuário possa digitar cinco 
    valores numéricos e cadastre-os em uma lista, já na 
    posição correta de inserção (sem usar o sort()). 
    No final, mostre a lista ordenada na tela.
'''
numeros = []

for i in range(0, 5):
  valor = int(input("Informe um valor: "))
  if i == 0 or valor > numeros[-1]:
    numeros.append(valor)
  else:
    j = 0
    while j < len(numeros):
      if valor <= numeros[j]:
        numeros.insert(j,valor)
        break
      j += 1
print(f'Lista ordenada: {numeros}')
