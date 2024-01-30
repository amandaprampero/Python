#sortear a ordem de apresentação do trabalho de alunos
#ler o nome de 4 alunos e mostrar a ordem sorteada
from random import shuffle
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))

lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
