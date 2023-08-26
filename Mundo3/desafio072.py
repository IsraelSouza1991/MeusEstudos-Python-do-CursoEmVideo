# Exercício Python 72: crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. O seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

escolha = int(input('Informe qual número, de zero ao vinte, deseja ver por extenso: '))
while True:
    if escolha < 0 or escolha > 20:
        escolha = int(input(f'O número escolhido está incorreto. Digite novamente: '))
    else:
        break
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze'
         , 'Catorze', 'Quinze', 'Dezeseis', 'Dezessete', 'Dezeoito', 'Dezenove', 'Vinte')
print(f'Este número por extenso é {tupla[escolha]}.')
print(f'Nossa tupla tem {len(tupla)} itens.')
