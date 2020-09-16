'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

frase = str(input('digite algo: ')).strip().replace(' ', '')
print(f'o inverso de {frase.lower()} é {frase[::-1].lower()}')
if frase == frase[::-1]:
    print('temos um palíndromo')
else:
    print('não temos um palíndromo')
