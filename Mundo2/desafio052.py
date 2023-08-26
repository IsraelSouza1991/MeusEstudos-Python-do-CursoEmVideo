# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from time import sleep
print('~//'*20+'\n')
valor = int(input('Informe um valor que confirmaremos se ele é número primo: '))
total = 0
for c in range(1, valor+1):
    sleep(0.01)
    if valor % c == 0:
        print('\33[33m', end='')
        total += 1
    else:
        print('\33[30m', end='')
    print('{}'.format(c), end=' ')
print('\n \33[mO número {} foi divisível {} vezes.'.format(valor, total), end=' ')
if total == 2:
    print('Portanto é um número primo!')
else:
    print('Portanto não é um número primo!')
print('\n'+'~//'*20)
