'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''
cidade = str(input('em qual cidade você nasceu? ')).strip()
print('santo' in '{}'.format(cidade[:5].lower()))
