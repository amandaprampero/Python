'''
    Crie um programa que tenha uma função fatorial() 
    que receba dois parâmetros: o primeiro que indique 
    o número a calcular e outro chamado show, que será um 
    valor lógico (opcional) indicando se será mostrado ou não
    na tela o processo de cálculo do fatorial.
'''


def fatorial(n, show=False):
  """
  -> Calcula o fatorial de um número.
  :param n: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do fatorial de um número n.
  """
  f = 1
  for i in range(n, 0, -1):
    f *= i
    if show:
      print(i, end='')
      if i > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
        print(f)
  return f


print('\033[34m^~\033[m' * 20)
print(f'{"FATORIAL" :^40}')
print('\033[34m^~\033[m' * 20)
n = int(input('Digite um número: '))
fat = fatorial(n, show=True)
print(f'O fatorial de {n} é {fat}')
#help(fatorial)
