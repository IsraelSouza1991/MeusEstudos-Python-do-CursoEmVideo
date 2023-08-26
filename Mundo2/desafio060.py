# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Informe um número inteiro qualquer.\nR: '))
f = 1
contador = num
while contador > 0:
    print('{} '.format(contador), end='')
    print('x ' if contador > 1 else '', end='')
    f *= contador
    contador -= 1
print('\n...portanto {}! é igual a {}'.format(num, f))
