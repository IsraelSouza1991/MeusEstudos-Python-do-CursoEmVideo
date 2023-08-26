# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('=-='*40)
print(f'{"Minha solução: ":^40}')

p_aberto = p_fechado = 0
posicao = 0
express = list((input('Digite a expressão que deseja inserir: ')).replace(' ', ''))
for elemento in express:
    if elemento == '(':
        p_aberto += 1
    if elemento == ')':
        p_fechado += 1
# print(f'Quantidade de parênteses aberto: {p_aberto}.\n'
#      f'Quantidade de parênteses fechados: {p_fechado}.')
if p_aberto == p_fechado:
    print('Sua expessão está válida!')
else:
    print('Sua expressão não está válida!')

print('=-='*40)
print(f'{"Solução do professor: ":^40}')
"Solução do professor: "
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
