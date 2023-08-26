#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input('Qual a distância em Km da viagem escolhida?'))
if d > 200:
    calc = d * 0.45
    print('O preço da passagem será de R$ {:.2f}.'.format(calc))
else:
    print('O preço da passagem será de R$ {:.2f}.'.format(d * 0.5))
