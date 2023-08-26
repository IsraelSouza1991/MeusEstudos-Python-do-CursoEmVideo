# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listainpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Deseja continuar?\n[S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
    elif escolha in 'S':
        print()
    else:
        print('Escolha inválida!\n')
lista.sort()
print(f'Os números selecionados: {lista}')
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listainpar.append(v)
listapar.sort()
listainpar.sort()
print(f'Somente os números pares: {listapar}')
print(f'Somente os números ímpares: {listainpar}')
