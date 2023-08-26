# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
peso = 0
menorpeso = 0
maiorpeso = 0
for c in range(1, 6):
    peso = float(str(input('Informe o peso da {}ª pessoa (em Kg, apenas número): '.format(c)).replace(',', '.')))
    if menorpeso == 0:
        menorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso

print(menorpeso + maiorpeso)
print('O maior peso lido foi {}kg e o menor peso lido foi {}Kg.'.format(str(maiorpeso).replace('.', ','), str(menorpeso).replace('.', ',')))

#  Resolução diferente da apresentada pelo professor
