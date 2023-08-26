# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# minha solução
'''
from time import sleep
from random import randint

jogadores = dict()
ganhadores = []
ranking = dict

quantjog = int(input('Deseja jogar com quantos jogadores? '))

for j in range(0, quantjog):
    jogadores['Nome'] = str(input(f'Infome o nome do {j+1}º jogador: '))
    print('lançando o dado', end='')
    for t in range(0, 3):
        print('.', end='')
        sleep(0.5)
    jogadores['Resultado Dado'] = randint(1, 6)
    print('Resutado:', end='')
    print(jogadores['Resultado Dado'])
    print('=-' * 20)
    sleep(1)
    ganhadores.append(jogadores.copy())
print(ganhadores)
'''

# solução do professor

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)