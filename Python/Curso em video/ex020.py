'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''

from random import shuffle
n1 = str(input('qual o nome do aluno? '))
n2 = str(input('qual o nome do aluno? '))
n3 = str(input('qual o nome do aluno? '))
n4 = str(input('qual o nome do aluno? '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)
