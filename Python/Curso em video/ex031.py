'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

dist = float(input('qual a distância da viagem? '))
print(f'você está prestes a fazer uma viagem de {dist:.2f}km.')
if dist <= 200:
    dist = dist * 0.5
    print(f'o preço da viagem será de R${dist:.2f}')
else:
    dist = dist * 0.45
    print(f'o preço da passagem será de R${dist:.2f}')
