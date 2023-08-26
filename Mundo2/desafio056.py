# Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
name = ''
age = 0
mediaidade = 0
somaidade = 0
homemmaisvelho = 0
nomevelho = ''
totmulher20 = 0
from time import sleep
for person in range(1, 5):
    for t in range(1, 20):
        sleep(0.01)
        print('=', end='')
    print('\n\33[0:36mPerson {}.\033[m'.format(person))
    name = str(input('What{}s your name? \n R: '.format("'"))).strip()
    age = int(input('How old are you? \n R: '))
    sex = str(input('Are you male (M) or female (F)? \n R: ')).upper().strip()[0]
    while sex not in 'MF':
        sex = str(input('Dados inválidos, digite novamente seu sexo: ')).strip().upper()[0]
    if person == 1 and sex in 'M':
        homemmaisvelho = age
        nomevelho = name
    if sex in 'M' and age > homemmaisvelho:
        homemmaisvelho = age
        nomevelho = name
    if sex in 'F' and age < 20:
        totmulher20 = totmulher20 + 1
    somaidade += age
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(homemmaisvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
