'''crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite o seu nome completo: ')
print('seu nome todo em maiúsculo fica {}'.format(nome.upper()))
print('seu nome todo em minísculo fica {}'.format(nome.lower()))
'''print('seu nome todo possui {} letras'.format(int(len(nome.replace(' ', '')))))'''
print('seu nome todo possui {} letras'.format(len(nome) - nome.count(' ')))
nome1 = nome.split()
print('seu primeiro nome é {} e possui {} letras'.format(nome1[0].title(), len(nome1[0])))
