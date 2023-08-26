    ## Aula 6 - Tipos Primitivos
    ## Link: https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=9


n_int = int(input('Escreva um número inteiro:'))
    #int para números inteiros.

n_float = float(input("Escreva um número com ponto:"))
    #float para número reais (com ponto flutuante), considera ponto no lugar de vírgula

    #n_bool = True or False('')
    #para verdadeiro ou falso

string = 'Olá'
    #para texto

    # Exemplo matemático:

s = n_int + n_float

print('A soma de {0} com {1} vale {2}'.format(n_int,n_float,s))

#######


# Ordem de precedência: entre (), depois potência ***, depois
# Multiplicação *
# Divisão /
# Divisão inteira//
# e resto da divisão%

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = pow(n1,n2)
print('A soma de {} com {} é {}!'.format(n1, n2, s))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
print('A divisão de {} por {} é igual a {:.3f}'.format(n1, n2, d)) # resultado com 3 casas decimais
print('A divisão inteira de {} por {} é {}'.format(n1, n2, di), end='')
print(' O resto da divisão é {}'.format(n1 % n2))
print('A potência de {} elevado a {} é {}'.format(n1, n2, e))

nome = input('Qual é seu nome?')
print('Olá {:=^20}!'.format(nome))

# Aula 08 - Utilizando módulos

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.3f}'.format(num, raiz))


# Aula 09 - String

'''#Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(),
junção com join().

Fatiamento:

    variável[1:2:3]

    ss = Shark
    print(ss[0:12:2])
    SmySak # pula de dois em dois

fruit = 'banana'
    fruit[:3]
        'ban'
    fruit[3:]
        'ana'

Análise:
    len(variável) - tamanho da frase
    variável.count('o') - conta quantas vezes exites 'o' na frase
    variável.find() - quantas vezes encontrou...

Transformação
    variável.replace() substituição


o in é um operador

'''

frase = input('Informe o seu nome: ')

fatfrase = frase[::]
lenfrase = len(frase)
countfrase = frase.count('I')
findfrase = frase.find('Israel')

replacefrase = frase.replace('Israel', 'Bonito')


print(fatfrase,lenfrase, countfrase, findfrase, replacefrase)

# Aula 10
#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

"""
Condições simples e compostas

if carro.esquerda():
    bloco true

else: bloco falso


"""
'''
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Israel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão é tão normal!')
print('Bom dia, {}!'.format(nome))
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}'.format(m))
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')

# Aula 11

#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades.
print('\033[7;30m Olá munto!\033[m')
