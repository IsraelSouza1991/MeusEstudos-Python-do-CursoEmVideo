#  Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
from time import sleep
quant = 0

num = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
menor = maior = num[0]
soma = sum(num)
print('Gerando 5 números aleatórios: ', end='')
for n in num:
    print(n, ' ', end='')
    sleep(0.5)
    if n <= menor:
        menor = n
    elif n >= maior:
        maior = n
print(f'\nO maior número gerado foi {maior} e o menor foi {menor}.')
print(f'A soma destes número é {soma}.')
