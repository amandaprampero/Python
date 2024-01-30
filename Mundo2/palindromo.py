frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
  print('A frase é um palíndromo')
else:
  print('A frase não é um palíndromo')
