#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print('O(A) aluno(a) escolhido(a) foi: {}'.format(escolhido))