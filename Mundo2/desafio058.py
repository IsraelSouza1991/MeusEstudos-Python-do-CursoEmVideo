# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep

novojogo = 'S'
while novojogo == 'S':
    print('=' * 20)
    print('\033[0:33:40mOlá, estou pensando em um número inteiro entre 0 e 10 e quero que você adivinhe.\033[m')
    print('_'*20)
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    num = random.randint(0, 10)
    print('Escolhi o número {}'.format(num))
    escolha = int(input('Em qual número você acha que estou pensando?\n\033[7:30:41mDigite:\033[m '))
    quantpalpites = 1

    while escolha != num:

        if escolha < 0 or escolha > 10:

            escolha = int(input('Número inválido. Você digitou {} e ele está fora da lista.\n\033[7:30:41mTente novamente\033[m: '.format(escolha)))
            quantpalpites += 1
        else:
            escolha = int(input('Errou...\n\033[7:30:41mTente novamente:\033[m '))
            quantpalpites += 1
        print('='*20)
    print('Correto!\nVocê acertou, o número que escolhi foi {}.'.format(num))

    s = 's' if quantpalpites > 1 else ''  # if ternário

    print('Você deu {} palpite{}.'.format(quantpalpites, s))

    novojogo = str(input('Quer jogar novamente?\n\033[7:33:40m[SIM] ou [NÃO]:\033[m ')).strip().upper()[0]

print('Foi um prazer jogar com você!')
