'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('qual o sexo da pessoa? [M / F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input(f'opção inválida, tente novamente')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso.')
