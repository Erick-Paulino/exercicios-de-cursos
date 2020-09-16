'''Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import sin, cos, tan, radians
ang = float(input('digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('com o Ângulo de {}º, temos o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(ang, sen, cos, tang))
