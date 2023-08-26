# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = c = s = 0
plural = ''
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    else:
        c += 1
        s += n
if c > 1:
    plural = 's'
print(f'A soma do{plural} {c} número{plural} digitado{plural} foi {s}.')
