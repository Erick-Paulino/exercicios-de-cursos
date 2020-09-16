'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
hmaisvelho = '' #homem mais velho
menos20 = 0 #mulheres com menos de 20 anos
idadetot = 0 #idade total
maisidade = 0 #idade do homem mais velho
for c in range(1, 5):
    nome = str(input(f'qual o nome da {c}° pessoa? ')).capitalize()
    idade = int(input('qual a idade? '))
    sexo = str(input(f'e qual o sexo de {nome}? [M / F] ')).upper()
    idadetot = idadetot + idade
    if sexo == 'M' and idade > maisidade:
        maisidade = idade
        hmaisvelho = nome
    if sexo == 'F' and idade < 20:
        menos20 += 1
media = (idadetot / 4)
print(f'''a média de idade do grupo é de {media} anos,
o homem mais velho se chama {hmaisvelho}, e tem {maisidade} anos,
ao todo são {menos20} mulheres com menos de 20 anos.''')
