# Fala um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n1 = int(input('Me informe um número inteiro para mostrar sua tabuada: '))
txt = str('{} x {} = {}')
print('-'*12)
print(txt.format(n1, 0, n1*0))
print(txt.format(n1, 1, n1*1))
print(txt.format(n1, 2, n1*2))
print(txt.format(n1, 3, n1*3))
print(txt.format(n1, 4, n1*4))
print(txt.format(n1, 5, n1*5))
print(txt.format(n1, 6, n1*6))
print(txt.format(n1, 7, n1*7))
print(txt.format(n1, 8, n1*8))
print(txt.format(n1, 9, n1*9))
print(txt.format(n1, 10, n1*10))
print('-'*12)