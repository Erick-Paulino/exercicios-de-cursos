'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n = int(input('digite um número: '))
if n % 2 == 0:
    print(f'o número {n} é par.')
else:
    print(f'o número {n} é impar.')
