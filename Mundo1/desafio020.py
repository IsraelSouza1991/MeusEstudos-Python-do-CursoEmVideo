# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro: ')
lista = [n1, n2, n3]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)