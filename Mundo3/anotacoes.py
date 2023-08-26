# #                                            VARIÁVEIS COMPOSTAS
# ======================================================================================================
# #                                          Aula 15 Tuplas: Variáveis compostas: "As tuplas são imutáveis"

# Representado por (). Não sendo obrigatório
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#
# for cont in range(0, len(lanche)):
#   print(f'Eu vou comer {lanche[cont]}')
# print('Comi pra caramba!')

# ======================================================================================================

# for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer{comida} na posição {pos}')
# print('Comi pra caramba!')

# ======================================================================================================

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c)
# print(c.index(5, 1))  # retorna o índice a partir da primeira posição.

# ======================================================================================================
# ======================================================================================================

# #                                              AULA 16 - Lista[]:
#
# # Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# # As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# # acessíveis por chaves individuais.
# # lista pode começar assim: lista = [] ou assim: list()

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True) # organiza a lista
# num.insert(2, 0) # insere 2 na posição 0
# num.pop(2) # retira item

# ======================================================================================================

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
#
# for chave, v in enumerate(valores):
#     print(f'Na posição {chave} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')
# print(valores)

# ======================================================================================================

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for chave, v in enumerate(valores):
#     print(f'Na posição {chave} encontrei o valor {v}!')
# print('Cheguei ao final da lista.')

# ======================================================================================================

# # para fazer uma cópia de lista faça assim:

# a = [2, 3, 4, 7]
# # b = a # neste caso as listas teriam ligação entre elas. Alterando uma se altera a outra.
# b = a[:]
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
# ======================================================================================================
# ======================================================================================================

#                                                   Aula 18 – Listas (Parte 2)

# galera = list()
# dado = list()
# totmai = totmen = 0
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])  # [:] criar cópia de dados
#     dado.clear()
#
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade.')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade.')
#         totmen +=1
# print(f'Temos {totmai} maiores e {totmen} menores de idade.')

# ======================================================================================================
# ======================================================================================================

#                                                   Aula 19 – Dicionários
# '''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves literais.

# ======================================================================================================

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# ======================================================================================================

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()

# ======================================================================================================
# ======================================================================================================

#                                                   Aula 20 - Funções
#

# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

def mostralinha():
    print('-=' * 30)
#
# mostralinha()

# ======================================================================================================

def mensagem(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)
#
#
# mensagem('   Sistema de alunos   ')

# ======================================================================================================

def soma(a, b):
    print('-' * 30)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print('-' * 30)
#
#
# # programa principal
# soma(a=4, b=5)
# soma(8, 9)
# soma(2, 1)

# ======================================================================================================

def contador(* núm):
    print(núm)  # retorna tupla
    tam = len(núm)  # retorna quantidade de números
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
#
#
# contador(2, 1, 7)

# ======================================================================================================

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
#
#
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

# ======================================================================================================

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
#
#
# soma(5, 2)
# soma(2, 9, 4)

# ======================================================================================================
# #                                                   Aula 21 - Funções
# ======================================================================================================

# # Nessa aula, vamos continuar os nossos estudos de funções em Python,
# # aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções,
# # argumentos opcionais para dar mais dinamismo em funções Python,
# # escopo de variáveis e retorno de resultados.

# ======================================================================================================
def contador(i, f, p):
    """
        Aqui escreto os detalhes da minha função
    """
    c = i
    while c<= f:
        print(f'{c}',end='')
    print('FIM!')
#
#
# help(contador)

# ======================================================================================================

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *=c
    return f
#
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2}, {f3}')

# ======================================================================================================
# #                                                   Aula 22 - Módulos e Pacotes
# ======================================================================================================
# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python
# e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote,
# ampliando ainda mais a modularização em grandes projetos em Python.


# import uteis as u
#
# num = int(input('Digite um valor '))
# fat = u.fatorial(num)
# print(f'O fatorial de {num} é {fat}')
# print(f'O dobro de {num} é {u.dobro(num)}')
#
# from uteis import numeros
#
# num = int(input('Digite um valor '))
# fat = numeros.fatorial(num)
# print(f'O fatorial de {num} é {fat}')
# print(f'O dobro de {num} é {numeros.dobro(num)}')

"""
Neste Módulo apredemos a organizar os módulos e criar pacotes para determinados assuntos.
Não segui algumas das últimas aulas fazendo o arquivo pois a forma que estruturei foi diferente da apresentadada pelo
professor. Porém aprendi e aplicarei para projetos externos ao deste curso para otimizar o tempo e aprender o assunto da
próxima aula.
"""

# ======================================================================================================
# #                                                   Aula 23 - Tratamento de Erros e Exceções
# ======================================================================================================
# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
# Aprenda como usar a estrutura try except no Python de uma forma simples
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')

    # pode ter mais de um except
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')