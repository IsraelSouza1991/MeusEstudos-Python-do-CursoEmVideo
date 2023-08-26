# Exercício Python 076:
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)
lista = ('Lapis', 1.3, 'Tesoura', 2, 'Bolsa', 150, 'Caderno', 5)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('_' * 40)
