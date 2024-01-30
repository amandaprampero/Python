from random import randint

vitorias = 0
perdeu = False
while perdeu is not True:
  print('=-' * 15)
  print('VAMOS JOGAR PAR OU IMPAR')
  print('=-' * 15)
  computador = randint(0, 10)
  n = int(input('Digite um valor: '))
  pi = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
  res = (n + computador) % 2
  if (res == 0 and pi == 'P') or (res != 0 and pi == 'I'):
    print('VOCE VENCEU!')
    vitorias += 1
  else:
    print('VOCE PERDEU!')
    perdeu = True
  print('-' * 45)
  print(f'Você jogou {n} e o computador {computador}. ', end='')
  print(f'Total de {n + computador} deu ', end='')
  print('PAR' if res == 0 else 'IMPAR')
  print('-' * 45)
print(f'Voce ganhou {vitorias} vezes')
print('GAME OVER')
