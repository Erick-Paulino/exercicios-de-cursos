'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('qual o seu salario? '))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 / 100)
print(f'seu novo salario será de R${salario:.2f}')
