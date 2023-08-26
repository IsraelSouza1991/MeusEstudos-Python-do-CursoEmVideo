# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('\033[31mJOGO DO PAR OU ÍMPAR\033[m')
from random import randint
n_vitorias = 0
escolha = 'S'
while escolha == 'S':
    while True:
        print('=-=' * 20)
        jogador = str(input('{0}P{1}AR ou {0}Í{1}MPAR? '.format('\033[4m', '\033[m')).upper().strip()[0].replace('Í', 'I'))
        if jogador == 'P' or jogador == 'I':
            n = int(input('Qual número (inteiro) entre 0 e 10 você escolhe? '))
            computador = randint(0, 10)
            print(f'Computador escolheu {computador}')
            soma = n + computador
            if soma % 2 == 0:
                resultado = 'P'
                print('Deu Par')
                if jogador == resultado:
                    print('O jogador ganhou 🥳!')
                    n_vitorias += 1
                else:
                    print('O computador ganhou!\n\033[mFIM DE JOGO!')
                    break

            else:
                resultado = 'I'
                print('Deu ímpar')
                if jogador == resultado:
                    print('O jogador ganhou 🥳!')
                    n_vitorias += 1
                else:
                    print('O computador ganhou!\nFIM DE JOGO!')
                    break
        else:
            print('Escolha incorreta!')
    if n_vitorias != 0:
        print('~' * 20)
        print(f'O jogador ganhou {n_vitorias} partidas')
    escolha = str(input('Deseja continuar?\nR: ')).strip()[0].upper()
print('Foi um prazer jugar contigo!')
