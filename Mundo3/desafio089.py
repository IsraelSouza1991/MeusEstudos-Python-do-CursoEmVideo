# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
print(f'==' * 10,
      f'\033[4m{"SISTEMA DE REGISTRO DE ALUNOS"}\033[m',
      f'==' * 10, '\n')

notaaluno = list()
listaalunos = []
while True:
    notaaluno.append(str(input('Qual o nome do aluno(a)? ')))
    notaaluno.append(float(input('Informe a 1ª nota: ')))
    notaaluno.append(float(input('Informe a 2ª nota: ')))
    listaalunos.append(notaaluno[:])
    notaaluno.clear()
    print('-' * 30)
    opcao = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        print('\nFIM...')
        break
    print()
print('-=' * 30)

#  Escolher o tipo de registro:
loop = 'S'
l = 0
while True:
    while l == 0:
        resul = int(input(f'Qual tipo de registro deseja visualizar?'
                          f'\n[1] Individual?'
                          f'\n[2] completa?'
                          f'\nR: '))
        # verificar a escolha do usuário:
        print('-=' * 30)
        if resul == 1:
            print('LISTA DOS ALUNOS:\n')
            for i, a in enumerate(listaalunos):
                print(f'Registro {i + 1}...Nome: {a[0]}')
            print('-=' * 30)
            reg = int(input('\nQual registro deseja visualizar? '))
            d = listaalunos[reg - 1]
            print(f'Nome: {d[0]}...Média: {(d[1] + d[2]) / 2}'.replace('[', '').replace(']', ''))
            l = 1
        elif resul == 2:
            for i, a in enumerate(listaalunos):
                print(f'Registro {i + 1}...Nome: {a[0]}...Média: {(a[1]+a[2])/2}')
                sleep(1)
            print('--' * 30)
            l = 1
        else:
            print('\033[31mDado incorreto!\033[m\n')
            l = 0
    print('--' * 30)
    loop = str(input('\nDeseja ver outro tipo de registro[S/N]? ')).strip().upper()[0]
    if loop == 'N':
        print('\nFim do programa!')
        break
    else:
        l = 0
