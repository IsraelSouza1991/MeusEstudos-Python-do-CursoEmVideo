#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o salário do funcionário: R$ '))
if salario >= 1250:
    salarioatual = salario * 1.1
else:
    salarioatual = salario * 1.15
print('O salário com o aumento passa a ser: R$ {:.2f}.'.format(salarioatual))
