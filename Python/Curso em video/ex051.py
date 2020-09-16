''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

'''final = 0
primeiro = int(input('qual o primeiro termo da progressão? '))
razao = int(input('e qual a razão? '))
for c in range(1, 11):
    final = primeiro + razao
    primeiro = final
    print(f'{final}.', end=" ")'''

primeiro = int(input('qual o primeiro termo da progressão? '))
razao = int(input('e qual a razão? '))
decimo = primeiro + 9 * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}.', end=" ")
