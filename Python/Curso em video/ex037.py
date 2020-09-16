'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('digite um número inteiro: '))
base = int(input('''escolha uma das bases para conversão:
[1] converter para \033[1;31mBINARIO\033[m
[2] converter para \033[1;31mOCTAL\033[m
[3] converter para \033[1;31mHEXADECIMAL\033[m\n'''))
if base == 1:
    print(f'o número {num}, em binario será: \033[1;31m{bin(num)[2:]}\033[m')
elif base == 2:
    print(f'o número {num}, em OCTAL será: \033[7;31;40m{oct(num)[2:]}\033[m')
elif base == 3:
    print(f'o número {num}, em HEXADECIMAL será: \033[1;34m{hex(num)[2:]}\033[m')
else:
    print('comando invalido, tente novamente!')
