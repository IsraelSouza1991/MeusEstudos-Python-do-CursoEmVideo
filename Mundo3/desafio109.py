# Exercício Python 109:
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from modulos import moeda

s = float(input('Informe o seu salário: R$ '))
a = moeda.aumentar(s)
d = moeda.diminuir(s)
m = moeda.metade(s)
do = moeda.dobro(s)
print('-='*20)
print(f'Seu salário é {moeda.moeda(s, False)}.'
      f'\nCom o aumento ficará: {moeda.moeda(a)};'
      f'\nConsiderando a subtração o salário será: {moeda.moeda(d)};'
      f'\nA metade do salário é {moeda.moeda(m)};'
      f'\ne o dobro é {moeda.moeda(d)}.')
