# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
pa = primeiro
decimo = 0
while decimo < 10:
    print(pa, end=' -> ')
    pa += razao
    decimo += 1
print('Acabou!')

"""
    # Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
    # No final, mostre os 10 primeiros termos dessa progressão.
    print('+=' * 20)
    print('A PROGRESSÃO ARITMÉTICA DE ACORDO COM O TERMO E RAZÃO A SEGUIR!\n')
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Informe a razão: '))
    decimo = primeiro + (10 - 1) * razao
    for c in range(primeiro, decimo, razao):
        print('{} '.format(c), end='-> ')
    print('ACABOU!')
"""