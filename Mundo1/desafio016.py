''''#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float (input('Informe um número real: '))
#n1 = math.ceil(num)
#n2 = math.floor(num)
n3 = trunc(num)
print('Aporção inteira é :',n3)
#print('O resto seria: ',)'''

num = float (input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format (num, int(num)))