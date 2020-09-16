'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'com a média {media}, o aluno foi \033[7;34;40mAPROVADO\033[m.')
elif (media <= 6.9) and (media >= 5):
    print(f'com a média {media},o aluno está em \033[1;30;43mRECUPERAÇÃO!\033[m')
else:
    print(f'com a media {media}, o aluno foi \033[1;30;41mREPROVADO\033[m')
