# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    nome = str(input('Informe o nome do jogador: '))
    gols = str(input('Informe o número de gols: '))

    if not gols.isnumeric():
        gols = 0
    print(f'Jogador: {nome} ........ número de gols: {gols}')


ficha()