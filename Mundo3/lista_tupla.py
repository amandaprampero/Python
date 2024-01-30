'''Crie um programa que tenha uma tupla única
    com nomes de produtos e seus respectivos preços.
    No final mostre uma listagem de preços,
    organizando os dados em forma tabular.'''

listagem = ('Gloss', 5.90,
            'Lip tint', 4.50,
            'Corretivo', 20.30,
            'Base', 67.99,
            'Bronzer', 21.70,
            'Blush', 13.50,
            'Máscara de cílios', 34.99)

print('\033[35m=\033[m' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('\033[35m=\033[m' * 40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
         print(f'{listagem[i]:.<30}', end = '')
    else:
         print(f'R${listagem[i]:>7.2f}')

print('\033[35m=\033[m' * 40)
