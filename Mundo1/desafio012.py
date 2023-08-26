#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Olá, temos disponível aqui em nossa loja os seguintes serviços:'
                '\n 1 - Limpeza de pele = R$ 200,00'
                '\n 2 - Fazer as unhas = R$ 80,00'
                '\n 3 - Fazer o cabelo = R$ 320,00'
                '\n Escolha o número do produto que deseja: '))
if produto == 1:
    print('A limpeza de pele estará pelo preço de R$ {}.'.format(200*0.95))

elif produto == 2:
    print('Para fazer as unhas terá um desconto, e o preço será de R$ {}'.format(80*0.95))

else: print(' Infelizmente não terá desconto hoje para este produto. Terá que pagar o valor padrão!')