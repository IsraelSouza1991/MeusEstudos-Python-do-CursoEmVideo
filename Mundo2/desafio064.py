# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('Será solicitado vários números, e como condição de parada você deverá digitar 999')
n = Q = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro:\n>>R: '))
    if n != 999:
        soma += n
        q += 1
s = 's' if q > 1 else ''
foram = 'Foram' if q > 1 else 'Foi'
print('{3} digitado{0} {1} número{0}, e a soma entre ele{0} é {2}'.format(s, q, soma, foram))
