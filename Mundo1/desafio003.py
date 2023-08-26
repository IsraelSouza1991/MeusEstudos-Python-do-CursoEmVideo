nome = str(input('Olá, qual o seu nome? '))
print('Ok {}, vamos realizar algumas contas simples...'.format(nome))
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div = n1 / n2
print('A soma entre {0} e {1} é {2}'.format(n1, n2, soma))
print('{0} menos {1} é igual a {2}'.format(n1, n2, subt))
print('a multiplicação de {} com {} é igual a {}'.format(n1, n2, mult))
print(n1,' dividido por {0} é igual a {1}'.format(n2, div))
