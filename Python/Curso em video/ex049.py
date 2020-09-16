'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

n = int(input('deseja saber a tabuda de qual número? '))
for c in range(1, 11):
    r = (c * n)
    print(f'{c} x {n} = {r}')
