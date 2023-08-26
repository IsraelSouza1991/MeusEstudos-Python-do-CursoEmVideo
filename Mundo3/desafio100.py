# Exercício Python 100:
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

numeros = list()


def sorteio():

    for c in range(1, 6):
        num = randint(1, 100)
        numeros.append(num)
        c += 1
    print(f'Númeos sorteados: {numeros}'.replace('[', '').replace(']', ''))


def somapar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    if soma == 0:
        print('Não há valores pares na lista!')
    else:
        print(f'A soma entre os valores pares sorteados é {soma}')


sorteio()
somapar()
