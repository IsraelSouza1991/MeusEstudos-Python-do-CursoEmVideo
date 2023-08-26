#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
altura = float(input('Informe o seu tamanho em cm: ')) / 100
peso = float(input('Informe seu peso em Kg: '))
imc = peso / (altura ** 2)
print('Você está com um IMC de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc < 25:
    print('Parabéns, você está com Peso Ideal.')
elif 25 < imc < 30:
    print('Você está Sobrepeso.')
elif 30 < imc < 40:
    print('Cuidado! está na linha da Obesidade.')
else:
    print('ATENÇÃO! Você está com Obesidade Mórbida.')