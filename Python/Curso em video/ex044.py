'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
compra = float(input('qual o valor da compra? R$ '))
pag = int(input('''e qual a forma de pagamento?
[1] à vista dinheiro ou cheque
[2] a vista no cartão
[3] em até 2X no cartão
[4] 3X ou mais no cartão\n'''))
if pag == 1:
    final = compra - (compra * 10 / 100)
    print(f'a compra de R${compra:.2f}, com desconto ficará R${final:.2f}.')
elif pag == 2:
    final = compra - (compra * 5 / 100)
    print(f'com o desconto a compra de {compra:.2f} passará para {final:.2f}.')
elif pag == 3:
    print(f'o valor da compra é de R${compra:.2f}.')
elif pag == 4:
    final = compra + (compra * 20 / 100)
    print(f'o valor passará de R${compra:.2f}, para R${final:.2f}.')
else:
    print('comando inválido, tente novamente!')
