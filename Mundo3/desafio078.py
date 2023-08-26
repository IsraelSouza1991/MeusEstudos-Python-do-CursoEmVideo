# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
from time import sleep

while True:
    maior = menor = 0
    posmaior = posmenor = 0
    lista = list()
    for c in range(0, 5):
        lista.append(float(input('Digite um valor: ')))
        for m in range(0, 1):
            maior = menor = lista[0]
            #posmaior = posmenor = lista.index(menor)

    print(f'Foram digitado os seguintes valores: {lista}')

    for chave, valor in enumerate(lista):
        if valor >= maior:
            maior = valor
            posmaior = chave + 1
        if valor <= menor:
            menor = valor
            posmenor = chave + 1
    print(f'-=-' * 40)

    print(f'O {maior} na posição {posmaior} foi o maior valor digitado e o {menor} na posição {posmenor} foi o menor')

    opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    while opcao not in 'SN':
        print('Opção incorreto.\nVamos tentar novamente.', end='')
        opcao = str(input('Deseja continuar: ')).strip().upper()[0]
    if opcao == 'N':
        break
    elif opcao == 'S':
        for c in range(0, 3):
            print('.', end='')
            sleep(1)
print('-=-' * 30)
print('Foi um prazer.')
