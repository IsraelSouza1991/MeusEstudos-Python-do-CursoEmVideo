# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área deste terreno de {l} metros de largura x {c} metros de comprimento é de {a} metros')
    print()


larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)
