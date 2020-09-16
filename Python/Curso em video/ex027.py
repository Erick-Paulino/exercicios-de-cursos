nome = str(input('digite seu nome completo: ')).strip().title()
print(f'seu primeiro nome é {nome.split()[0]}')
print(f'seu ultimo nome é {nome.rsplit()[-1]}')
