'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor= 1000
for c in range(1, 6):
    peso = int(input(f'digite o {c}° peso: (kg) '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'''o maior peso foi de {maior},
e o menor peso foi de {menor}.''')
