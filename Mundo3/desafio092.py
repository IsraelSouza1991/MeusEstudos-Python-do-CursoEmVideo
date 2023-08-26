# Exercício Python 092: Crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
anoatual = datetime.now().year
dados['idade'] = anoatual - nasc
dados['ctps'] = int(input('Número carteira de trabalho(digite 0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - anoatual) + dados['idade']
print('-=' * 30)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')