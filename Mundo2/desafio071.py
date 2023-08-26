# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

"""Solucução do Professor
while True:
    print('=' * 30)
    print('{:^30}'.format('BANCO OLIVEIRA SOARES'))
    print('=' * 30)
    valor = int(input('Que valor você quer sacar? R$ '))
    total = valor
    céd = 50
    totcéd = 0
    while True:
        if total >= céd:
            total -= céd
            totcéd += 1
        else:
            if totcéd > 0:
                print(f'Total de {totcéd} cédulas de R$ {céd}')
            if céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 1
            totcéd = 0
            if total == 0:
                break
    print('=' * 30)
    break
"""

"Minha Solução"

saque = int(input('Digite o valor que deseja sacar: R$ '))
montante_banco = saque
quant_cedulas = 0
while True:
    if montante_banco >= 50:
        quant_cedulas = montante_banco // 50
        montante_banco = montante_banco % 50
        print(f'{quant_cedulas} notas de 50')
    elif 50 > montante_banco > 20:
        quant_cedulas = montante_banco // 20
        montante_banco = montante_banco % 20
        print(f'{quant_cedulas} notas de 20')
    elif 20 > montante_banco > 10:
        quant_cedulas = montante_banco // 10
        montante_banco = montante_banco % 10
        print(f'{quant_cedulas} notas de 10')
    elif 10 > montante_banco > 1:
        quant_cedulas = montante_banco // 1
        montante_banco = montante_banco % 1
        print(f'{quant_cedulas} notas de 1')
    if montante_banco == 0:
        break
