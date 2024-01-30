maiores = homens = mulheres = 0
sexo = 'X'

while True:
  idade = int(input('Digite a idade: '))
  if idade >= 18:
    maiores += 1
  while sexo not in 'FfMm':
    sexo = input('Digite o sexo [F/M]: ').upper().strip()[0]
    if sexo in 'Mm':
      homens += 1
    if sexo in 'Ff' and idade < 20:
      mulheres += 1
  sexo = 'X'
  resp = input('Deseja continuar? [S/N]').upper().strip()[0]
  if resp in 'Nn':
    break
print(f'Foram cadastradas {maiores} pessoas maiores de idade.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos.')