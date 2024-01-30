from random import randint

palpite = -1
resposta = randint(0,10)
tentativas = 0

print('\033[1;34m-=-\033[m' * 12)
print('\t\033[1;31mJOGO DA ADIVINHAÇÃO\033[m')
print('\033[1;34m-=-\033[m' * 12)
while palpite != resposta:
  palpite = int(input('Digite um número entre 0 e 10: '))
  tentativas += 1
  if palpite == resposta:
    print('\033[32mPARABÉNS!\033[m Você acertou!')
    print(f'Você pensou em \033[33m{palpite}\033[m e o computador pensou em \033[33m{resposta}\033[m.')
    print('Você precisou de {} tentativas para acertar.'.format(tentativas))
  else:
    print('Você \033[31mERROU!\033[m Tente novamente!')
    if palpite < resposta:
      print('Dica: o número é \033[33mMAIOR\033[m que o seu palpite.')
    else:
      print('Dica: o número é \033[33mMENOR\033[m que o seu palpite.')
