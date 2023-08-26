# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior():
    # criar lista
    numeros = list()
    m = 0
    while True:
        n = int(input('Digite um número inteiro [para sair digite 999]: '))
        if n == 999:
            break
        else:
            numeros.append(n)
    # saber qual é o maior
            if n > m:
                m = n

    print(('%%' * len(numeros)) + ('%%' * 20))
    print(f'\nO maior número digitado da lista foi {m}.'
          f'\nVeja a lista com o números digitados: {numeros}')


maior()
