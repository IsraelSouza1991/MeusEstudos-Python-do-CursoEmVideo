#  Exercício Python 098:
#  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#  início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada

from time import sleep as s


def contador():

    i = 1
    f = 11
    p = 1

    print('-=' * 20)
    for c in range(i, f, p):
        print(c, end=' ')
        c += 1
        s(0.5)
    print()

    print('-=' * 20)

    for c in range(f-1, i-1, -p):
        print(c, end=' ')
        c += 1
        s(0.5)
    print()
    print('-=' * 20)

    i = int(input('Digite o início: '))
    f = int(input('Digite o fim: '))
    p = int(input('Digite o passo: '))

    print('-=' * 20)
    if f < i:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            c += 1
            s(0.5)
        print()
    else:
        for c in range(i, f+1, p):
            print(c, end=' ')
            c += 1
            s(0.5)
        print()


contador()
