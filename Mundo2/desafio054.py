# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
datahoje = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    anonasc = int(input('Informe a data de nascimento da {}ª pessoa: '.format(c)))
    idade = datahoje - anonasc
    if idade < 21:
        totalmenor += 1
    else:
        totalmaior += 1
print('Total que atingiram a maioridade: {}'.format(totalmaior))
print('Total qua não atingiram a maioridade: {}'.format(totalmenor))
