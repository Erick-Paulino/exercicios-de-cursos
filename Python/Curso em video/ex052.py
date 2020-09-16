'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
tot = 0
num = int(input('digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print(f'\033[1;31m{c}\033[m', end=' ')
    else:
        print(f'{c}', end=' ')
if tot > 2:
    primo = 'não é primo'
else:
    primo = 'é primo'
print(f'''\no número {num} foi divisível {tot} vezes,
e por isso ele {primo}''')
