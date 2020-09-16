'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
n = int(input('digite um número entre 0 e 5: '))
n2 = randint(0, 5)
print('provessando...')
sleep(3)
if n == n2:
    print(f'o numero sorteado foi {n2}, você ganhou!!!')
else:
    print(f'o número sorteado foi {n2}, o computador ganhou!!!')
