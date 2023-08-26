# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

hitorico = dict()

situacao = ''
hitorico['Aluno'] = str(input('Informe o nome do aluno(a): '))
hitorico['Nota'] = float(input('Informe a nota dele(a): '))

if hitorico['Nota'] < 5:
    situacao = str('foi reprovado')
elif hitorico['Nota'] >= 7:
    situacao = str('foi aprovado(a)')
else:
    situacao = str('está de exame')

hitorico['Situação'] = situacao

for k, v in hitorico.items():
    print(f'{k}: {v}')
