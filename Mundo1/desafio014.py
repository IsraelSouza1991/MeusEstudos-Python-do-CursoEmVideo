#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Informe uma temperatura em graus celsius: '))
print('A conversão da temperatura {:.2f}ºC em graus Fahrenheit seria {:.2f}ºF'.format(temperatura, temperatura * (9/5)+32))
