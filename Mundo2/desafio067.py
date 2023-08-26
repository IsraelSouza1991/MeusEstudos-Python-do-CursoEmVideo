# Exercício Python 67:
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('-=-'*20)
nome = str(input(f'Olá, sou um programa que informa a tabuada conforme os números que for me informando.\n'
                 f'{"-=-"*20}\nPara iniciar informe seu nome: ')).strip()
print('-=-'*20)
print(f'É um prazer conversar contigo {nome}.\nPara sair da tabuada é somente digitar o número 0.')

num = result = 0
while True:
    print('~' * 40)
    num = int(input('Informe a tabuada de qual número deseja: '))
    if num == 0:
        break
    for c in range(1, 11):
        result = num * c
        print(f'{c} x {num} = {result}')
print(f'{nome}, volte sempre!')
