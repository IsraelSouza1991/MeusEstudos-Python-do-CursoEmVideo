# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from modulos import moeda

s = float(input('Informe o seu salário: R$ '))
a = moeda.aumentar(s)
d = moeda.diminuir(s)
m = moeda.metade(s)
do = moeda.dobro(s)
print('-='*20)
print(f'Seu salário é {moeda.moeda(s)}.'
      f'\nCom o aumento ficará: {moeda.moeda(a)};'
      f'\nConsiderando a subtração o salário será: {moeda.moeda(d)};'
      f'\nA metade do salário é {moeda.moeda(m)};'
      f'\ne o dobro é {moeda.moeda(d)}.')
