'''
    - Desafio 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida.
    No final, tudo isso será guardado em um dicionário,
    incluindo o total de gols feitos durante o campeonato.
    - Desafio 95: Aprimore o desafio 93 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

time = []
gols = []
jogador = {}

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f'Gols na {i+1} partida: ')))
    jogador['Total'] = sum(gols)
    jogador['Gols'] = gols[:]
    time.append(jogador.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if op == 'N':
        break

print('\033[34m*\033[m' * 40)
print(f'{"cod":<4}{"Nome":<10}{"Gols":<10}{"Total":<10}')
print('--' * 20)
for k, v in enumerate(time):
    print(f'{k:<4} ', end = '')
    for d in v.values():
        print(f'{str(d):<10}', end = '')
    print()
print('\033[34m*\033[m' * 40)   

while True:
    j = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if j == 999:
        break
    if j >= len(time):
        print('ERRO! Não existe jogador com esse código.')
    else:
        print(f'-- LEVANTAMENTO DO JOGO DE {time[j]["Nome"]}')
        for i, g in enumerate(time[j]['Gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< ENCERRANDO... >>>')