# Exercício Python 70: crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o utilizador vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totgasto = quant1000 = preco = menorpreco = 0
prodbarato = ''
print('\n==== LOJA DA FAMÍLIA IFOSTEKAIO ====\n')
print('=-=' * 20)
while True:
    produto = str(input('\nProduto: '))
    preco = float(str(input('Preço: R$ ')).replace(',', '.'))
    for c in range(0, 1):   # entrada para receber o primeiro registro.
        prodbarato = produto
        menorpreco = preco
        c += 1
    if preco < menorpreco:
        prodbarato = produto
        menorpreco = preco
    if preco > 1000:
        quant1000 += 1
    totgasto += preco
    continue_ = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    print('-=-' * 20)
    if continue_ == 'N':
        break
print('Total gasto: R$ {:.2f}'.format(totgasto))
print(f'{quant1000} produtos custam mais que R$ 1.000,00')
print(f'O Produto mais barato foi {prodbarato} pelo preço de R$ {menorpreco:.2f}')
