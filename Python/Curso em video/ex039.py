'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('em qual ano voce nasceu? '))
idade = date.today().year - ano
if idade < 18:
    print(f'você deverá se alistar no ano de {ano + 18}.')
elif idade == 18:
    print('esta é a hora certa para realizar o seu alistamento.')
else:
    print(f'o seu alistamento foi ha {date.today().year - (ano + 18)} ano(s) atrás.')
