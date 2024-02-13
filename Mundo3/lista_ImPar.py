'''
    Crie um programa onde o usuário possa digitar sete valores numéricos e 
    cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
    No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[],[]] #0 = PARES e 1 = ÍMPARES
for i in range(0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print('\033[35m**\033[m' * 13)
print(numeros)
print(f'Os \033[35mPARES\033[m digitados foram: {sorted(numeros[0])}')
print(f'Os \033[35mÍMPARES\033[m digitados foram: {sorted(numeros[1])}')
