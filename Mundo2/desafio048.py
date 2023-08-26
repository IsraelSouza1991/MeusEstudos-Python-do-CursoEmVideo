# Exercício Python 48:
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(3, 501, 2):
    if c % 3 == 0:  # se c for divisível por 3, se não fosse o resto da divisão seria outro valor, ex: 5/3 = 1,6 (% = 6)
        soma = soma + c
        cont = cont + 1
print('A soma entre todos os números ímpares entre 1 e 500 é {}. Foi somado {} números.'.format(soma, cont))

