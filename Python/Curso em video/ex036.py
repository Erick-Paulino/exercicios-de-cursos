'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''

valor = int(input('qual o valor da casa? R$ '))
tempo = int(input('em quantos anos deseja pagar? '))
salario = float(input('qual o seu salário? R$ '))
if (valor / (tempo * 12)) < (salario * 12 / 100):
    print(f'seu financiamento foi \033[4;32mAPROVADO !\033[m')
else:
    print('infelizmente seu financiamento foi \033[1;31;40mREPROVADO!\033[m')
