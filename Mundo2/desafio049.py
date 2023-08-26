# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada:

from time import sleep
n1 = int(input('Informe um número inteiro para mostrar sua tabuada: '))
n2 = 0

for t in range(0, 3):
    print('.', end='')
    sleep(0.5)
print(' ')

for c in range(-1, 10):
    print('{} x {} = {}'.format(n1, n2, n1 * n2))
    n2 = n2 + 1
    sleep(0.25)
print('{}FIM{}'.format(n1 * '=', n1 * '='))
