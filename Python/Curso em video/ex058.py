'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer'''

tentativas = 1
from random import randint
print('estou pensando em um número de 0 a 10, consegue adivinhar qual é?')
palpite = int(input('me diga seu palpite:'))
comp = randint(0, 10)
print(f'{palpite} {comp}')
while palpite != comp:
    if comp > palpite:
        palpite = int(input('pensei em um número maior... tente denovo: '))
        tentativas += 1
    elif comp < palpite:
        palpite = int(input('pensei em um número menor... tente mais uma vez: '))
        tentativas += 1
print(f'parabéns, na {tentativas}° tentativa você acertou!!!')
