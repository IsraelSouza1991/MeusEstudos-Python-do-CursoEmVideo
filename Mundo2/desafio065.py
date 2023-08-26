# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = media = soma = cont = maior = menor = 0

continuar = 'S'
while continuar == 'S':
    num = int(input('Informe um número inteiro: '))
    if cont == 0:
        menor = num
    menor = num if num <= menor else menor
    maior = num if num >= maior else maior
    continuar = str(input('\033[0:31mDeseja continuar [S / N]?\n R:\033[m ')).strip().upper()[0]
    soma += num
    cont += 1
    print('=-=' * 20 + '\n')

media = soma / cont
print('A média entre todos os números digitados foi {:.2f} e {} foi o maior valor, enquando {} foi o menor'.format(media, maior, menor))



