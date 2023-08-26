#  Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = float(str(input('Primeiro número: ')).replace(',', '.'))
n2 = float(str(input('Segundo número: ')).replace(',', '.'))
opcao = 0
while opcao != 5:
    print('''MENU:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção?\nR: '))
    if opcao == 1:
        print('A soma entre {:.2f} + {:.2f} é {:.2f}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado de {:.2f} x {:.2f} é {:.2f}'.format(n1, n2,n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {:.2f}'.format(n1))
        else:
            print(('O maior número é {:.2f}.'.format(n2)))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = float(str(input('Primeiro número: ')).replace(',', '.'))
        n2 = float(str(input('Segundo número: ')).replace(',', '.'))
    elif opcao == 5:
        print('Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=-' * 20)
    sleep(2)
