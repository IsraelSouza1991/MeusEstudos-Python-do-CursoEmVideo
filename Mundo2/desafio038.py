#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
if  n1 > n2:
    print('O primeiro valor escolhido é maior!')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
else:
    print('O segundo valor é maior!')