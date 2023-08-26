# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input('Agora informe a segunda nota: '))
media = (nota1+nota2) / 2
print('A média entre {} e {} é {}.'.format(nota1, nota2, media))

