'''Crie um programa que faça o computador jogar Jokenpô com você.'''
print('''suas opções:
[0] pedra
[1] papel
[2] tesoura''')
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
jogador = int(input('qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 13)
print(f'o computador jogou {itens[comp]}')
print(f'o jogador jogou {itens[jogador]}')
print('-=' * 13)
if comp == 0:
    if jogador == 2:
        print('o COMPUTADOR venceu!')
    if jogador == 0:
        print('o jogo EMPATOU')
    if jogador == 1:
        print('o JOGADOR venceu!')
if comp == 1:
    if jogador == 0:
        print('o computador venceu!')
    if jogador == 1:
        print('o jogo empatou!')
    if jogador == 2:
        print('o Jogador Venceu!')
if comp == 2:
    if jogador == 0:
        print('o Joador Venceu!')
    if jogador == 1:
        print('o computador Venceu')
    if jogador == 2:
        print('o jogo empatou')
