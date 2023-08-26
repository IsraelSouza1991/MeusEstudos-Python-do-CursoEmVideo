#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga um número qualquer:'))
n1 = n % 2 # define se é par (resultado 0) ou ímpar (resultado 1)
if  n1 == 0:
    print('O número escolhido é Par')
else:
    print('O número escolhido é Ímpar')

