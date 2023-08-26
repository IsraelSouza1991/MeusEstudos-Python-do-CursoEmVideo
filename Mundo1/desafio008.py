# Escreva um programa que liea um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input('Informe um valor em metros: '))
print('Este é igual a {:.0f} centímetros e {:.0f} milímetros'.format(n1*100, n1*1000))
