'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'qual o {c}° ano de nascimento? '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'''ao todo tivemos {maior} pessoas maior de idade,
e {menor} pessoas menor de idade.''')
