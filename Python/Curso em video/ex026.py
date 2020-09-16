'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre
 quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição
 ela aparece a última vez.'''

frase = str(input('digite uma frase:')).upper().strip()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('a letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A') + 1))
