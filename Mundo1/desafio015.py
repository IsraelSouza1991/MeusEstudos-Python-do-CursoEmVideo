#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de km que o carro percorreu: '))
d = int(input('Informe a quantidade de diárias que foram utilizadas: '))
al = d * 60
kmt = km * 0.15
print('O custo total do aluguel do carro é de R${:.2f} e R${:.2f} por km rodado, totalizando R${}.'.format(al, kmt, al + kmt))