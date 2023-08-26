#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input('Digite a quantos km/h o carro passou: '))
if v > 80:
    multa = float((v - 80) * 7)
    print('O motorista foi multado! \n O preço a ser pago é de R$ {:.2f}!'.format(multa))
else:
    print('O motorista estava dentro do limite de velocidade.')
