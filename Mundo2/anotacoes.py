# Aula 12 – Condições Aninhadas

"""
Teoria:

    Dentro de condições, outras condições.
    if carro.esquedar():
        carro.siga()

    elif carro.direita(): PODEMOS ADICIONAR VÁRIOS ELIF ABREIAÇÃO DE if else.

    else:

    Exemplo prático:

"""

nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Israel':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Stefane':
    print('Que belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

########################################################################################################################

# Aula 13 - Estrutura de repetição FOR

"""
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)

Teoria em portugues:

laço c no intervalo (1,10)
    passo
pega

Teoria na lingua:
for c in range(1,10):
    passo
pega

Exmplo prático:

"""
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

" considenando com soma: "

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor inteiro: '))
    s += n  # é o mesmo que s = s + n
print('O somatório de todos os valores foi {}'.format(s))


" É possível considerar aninhado com outras condições"

########################################################################################################################

#  AULA 14 - Estrutura de repetição while

'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. 
Por exemplo:

c=1 

while c != 10: 

    print(c)

    c += 1

print(‘Acabou’)

O while representar 'Enquanto' c for diferente de 10, vai dar print em c e somar 1 ao c.

'''

# Exemplo 1
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

# Exemplo 2
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

########################################################################################################################

# Aula 15 – Interrompendo repetições while

'''
Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. 
É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

'''
