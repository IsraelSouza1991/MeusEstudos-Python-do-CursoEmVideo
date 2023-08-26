# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
from time import sleep

f_s = '\033[31m'
f_e = '\033[m'
print(f'{f_s}Olá, vamos realizar o preenchimento de ficha cadastral!{f_e}')

for i in range(0, 50):
    print('I', end='')
    i += 1
    sleep(0.05)
quantpessoas = maioridade = quantmulher20 = quanthomem = 0
print('\n')
while True:
    quantpessoas += 1
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = str(input(f'Agora querecemos saber seu sexo.'
                     f'\n Masculino{f_s}[M]{f_e} ou Feminino{f_s}[F]{f_e}? ')).strip().upper()[0]
    quanthomem += 1 if sexo == 'M' else 0
    quantmulher20 += 1 if sexo == 'F' and idade < 20 else 0
    while sexo not in 'FM':
        if sexo == 'M':
            quanthomem += 1
        elif sexo == 'F' and idade < 20:
            quantmulher20 += 1
        else:
            sexo = str(input(f'ERRO! Digite novamente!'
                             f'\n Masculino{f_s}[M]{f_e} ou Feminino{f_s}[F]{f_e}? ')).strip().upper()[0]
    opcao = str(input(f'Deseja continuar? {f_s}SIM{f_e} ou {f_s}NÃO{f_e}? ')).strip().upper()[0]

    while opcao not in 'SN':
        if opcao == 'S':
            print('Ok, vamos preencher mais uma ficha!')
            sleep(2)
        elif opcao == 'N':
            print('Ok, Obrigado pelos registros!')
            break
        else:
            opcao = str(input(f'!!! Opção inválida!!! '
                              f'\n Deseja continuar? {f_s}SIM{f_e} ou {f_s}NÃO{f_e}? ')).strip().upper()[0]
    print('=-=' * 20)
    if opcao == 'N':
        print('Ok, Obrigado pelos registros!')
        break


print(f'Foram cadastradas {quantpessoas} pessoas. Sendo {maioridade} maiores de 18, {quanthomem} se declaram homens,'
      f' {quantpessoas - quanthomem} são mulheres '
      f'e {quantmulher20} mulheres tem menos que 20 anos')