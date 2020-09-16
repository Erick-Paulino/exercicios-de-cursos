'''Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input('qual o seu nome? ')).strip()
print(' silva' in '{}'.format(nome.lower()))
