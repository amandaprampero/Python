peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
  print('Abaixo do peso')
elif imc < 25 and imc >= 18.5:
  print('Peso ideal')
elif imc >= 25 and imc <= 30:
  print('Sobrepeso')
elif imc > 30 and imc <= 40:
  print('Obesidade')
else:
  print('Obesidade morbida')
print('Seu IMC é: {:.1f}'.format(imc))
