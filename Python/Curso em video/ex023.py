'''n = int((10000) + (int(input('Digite um número entre 0 e 9999: '))))
n = str(n)
print('O número {} possui, {} milhares.'.format(n, n[1]))
print('O número {} possui, {} centenas. '.format(n, n[2]))
print('O número {} possui, {} dezenas. '.format(n, n[3]))
print('O número {} possui, {} unidades.'.format(n, n[4]))'''

num = int(input('informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
