'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice

n1 = str(input('qual o nome do aluno? '))
n2 = str(input('qual o nome do aluno? '))
n3 = str(input('qual o nome do aluno? '))
n4 = str(input('qual o nome do aluno? '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(escolhido)
