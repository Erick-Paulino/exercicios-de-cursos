'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

tot = 0
soma = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        soma = soma + c
        tot = tot + 1
print(f'a soma ded todos os {tot} valores foi de {soma}.')
