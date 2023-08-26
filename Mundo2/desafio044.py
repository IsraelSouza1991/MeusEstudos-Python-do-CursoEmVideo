#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
price = float(input('Preço das compras: R$ '))
print('''Informe a forma de pagamento:
      
      [1] à vista dinheiro/cheque.
      [2] à vista no cartão.
      [3] em até 2x no cartão.
      [4] 3x ou mais no cartão.
      ''')
escolha = int(input('Informe o digito referente a forma de pagamento: '))
if escolha == 1:
    price = price * 0.9
    print('Você recebeu um desconto. O preço passou a ser R$ {:.2f}'.format(price))
elif escolha == 2:
    price = price * 0.95
    print('Você recebeu um desconto. O preço passou a ser R$ {:.2f}'.format(price))
elif escolha == 3:
    print('O preço a ser pago será de R$ {:.2f}'.format(price))
elif escolha == 4:
    price = price * 1.2
    print('O preço final será de R$ {:.2f}'.format(price))
else:
    print('Número digitado está incorreto!')