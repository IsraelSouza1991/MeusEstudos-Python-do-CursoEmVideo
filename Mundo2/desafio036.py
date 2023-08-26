#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('/===/'*5)
nome = str(input('Olá, qual é o seu nome? ')).strip().capitalize()
valoremprestimo = float(input('Informe o valor do empréstimo que deseja para compra da Casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
tempo = int(input('Em quantos anos deseja pagar este empréstimo ? '))
parcelas = int(valoremprestimo / (12 * tempo))
if parcelas >= salario * 0.3:
    print('O empréstimo foi negado!')
else:
    print('{}, seu empréstimo foi aprovado!'.format(nome))
    print('A prestação será de R$ {:.2f}!'.format(valoremprestimo/(12*tempo)))
print('/===/'*5)
