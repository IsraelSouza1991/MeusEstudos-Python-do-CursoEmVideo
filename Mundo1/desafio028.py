# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('-=-' * 20)
print('Olá, estou pensando em um número inteiro entre 0 e 5...')
print('-=-' * 20)
# numal = random.randrange(0,6)
numal = random.randint(0, 5)
num = int(input('Qual número você acha que escolhi? \n Digite:'))
print('Processando...')
sleep(3)
print('-=-' * 20)
if num == numal:
    print('Você Acertou! \n O número escolhido realmente era o {}'.format(numal))
else:
    print('Infelizmente você errou. \n O número que escolhi foi o {}'.format(numal))
print('-=-' * 20)
