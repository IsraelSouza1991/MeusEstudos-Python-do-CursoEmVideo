#Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
hoje = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = hoje - ano
print('O atleta tem {} anos, portanto está na seguinte categoria: '.format(idade))
if idade <= 14:
    if idade <= 9:
        print('MIRIM')
    else:
        print('INFANTIL')
if idade < 25:
    if idade <= 19:
        print('JÚNIOR')
    else:
        print('SÊNIOR')
elif idade > 25:
    print('MASTER')