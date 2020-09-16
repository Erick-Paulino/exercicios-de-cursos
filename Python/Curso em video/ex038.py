'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = float(input('digite um valor: '))
n2 = float(input('digite outro valor:'))
if n1 > n2:
    print(' o Primeiro valor é maior!')
elif n2 > n1:
    print('o Segundo valor é maior!')
else:
    print('não existe valor maior, os dois são iguais!')
