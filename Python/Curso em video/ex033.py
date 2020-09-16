'''faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
n3 = float(input('digite o terceiro valor: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'o menor valor digitado foi {menor:.0f}, e o maior foi {maior:.0f}')
