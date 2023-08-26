# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
from modulos import moeda

s = float(input('Informe o seu salário: R$ '))
print(f'Seu salário é R$ {s}, com o aumento ficará: {moeda.aumentar(s)}.'
      f'\nConsiderando a subtração o salário será: R${moeda.diminuir(s)}.'
      f'\nA metade do salário é R${moeda.metade(s)} e o dobro é R$ {moeda.dobro(s)}.')
