op = 0
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
while op != 5:
  print('=*'*20)
  print('OPERAÇÕES')
  print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS\n[5] SAIR DO PROGRAMA')
  print('=*'*20)
  op = int(input('>>>>>Qual operação você deseja realizar? '))
  if op == 1:
    soma = n1 + n2
    print(soma)
  elif op == 2:
    mult = n1 * n2
    print(mult)
  elif op == 3:
    if n1 > n2:
      print(n1)
    else:
      print(n2)
  elif op == 4:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
  elif op == 5:
    print('Fim do programa!')
    break
  else:
    print('Opção inválida. Tente novamente.')