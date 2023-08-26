# Exercício Python 63:
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Informe quantos termos deseja que seja exibido na tela: \n'))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    c += 1
    t1 = t2
    t2 = t3
print('-> FIM')
print('~' * 30)
