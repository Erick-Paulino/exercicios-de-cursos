'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

v = float(input('qual a velocidade do carro? '))
if v <= 80:
    print('tenha um bom dia, dirija com segurança!')
else:
    v = (v - 80) * 7
    print(f'você está acima da velocidade permitida, sua multa será de R${v}')
