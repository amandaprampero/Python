'''Deselvolva um programa que leia 4 valores pelo teclado
    e guarde-os em uma tupla. No final mostre:
    A) Quantas vezes apareceu o valor 9
    B) Em que posição foi digitado o primeiro valor 3
    C) Quais foram os números pares'''

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores: ', end = '')
for n in numeros:
    print(f'{n} ', end = '')
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end = '')
