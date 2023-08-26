# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
pares = 0
soma3c = 0
maior2l = 0
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para linha {l}, coluna {c}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            maior2l = matriz[l][c] if matriz[l][c] >= maior2l else maior2l
for c in range(0, 3):
    print('{}'.format(matriz[c]).replace(',', ' ]['))
print(f'A soma dos números pares: {pares}.')
print(f'A soma da 3ª coluna é {soma3c}.')
print(f'O maior valor da segunda linha é o {maior2l}.')
