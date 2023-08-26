# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
lcomp = []
njogo = int(input('Quantos jogos deseja gerar?\nR: '))
for j in range(0, njogo):
    jogo = list()
    for n in range(0, 6):
        while True:
            sort = randint(1, 60)
            if sort not in jogo:
                jogo.append(sort)
                break
    lcomp.append(jogo[:])
    # print(jogo) # para cada jogo separado
for i, l in enumerate(lcomp):
    print(f'Jogo {i+1}: {l}.')

"""
maisjogados = list()
for i, cada in enumerate(lcomp):
    while cada in lcomp:
        cada += 1
        lcomp.pop(i)
    maisjogados.append(i)
print(f'Os mais jogados fora: {maisjogados}')
"""