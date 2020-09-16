'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Os segmentos digitados podem formar um triângulo')
else:
    print('Os segmentos digitados não podem formar um triângulo')
