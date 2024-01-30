a = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
mais = 10
t = 0
while mais != 0:
  t += mais
  while c <= t:
    print(a, end=' -> ')
    a += r
    c += 1
  print('PAUSA')
  mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'PA com {t} termos')