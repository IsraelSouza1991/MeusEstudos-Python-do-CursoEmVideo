# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

p = int(input('Informe o primeiro número: '))   # primeiro
r = int(input('Informe a razão: '))     # razão (pulando de quanto em quanto)
t = int(input('Informe o termo: '))     # Termo (Quantas sequencias)
c = 0  # contador
total = 0
while t != 0:
    total += t
    while c < t:
        print(p, end=' -> ')
        p += r
        t -= 1
    print('PAUSA')
    t = int(input('Quantos termos a mais deseja que seja mostrado? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

"""
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