'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''

nome = str(input('Informe um nome: ')).strip()
print('Analisando seu nome...')
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras ao todo, sem considerar espaços:{}'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
format = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(format[0],len(format[0])))

