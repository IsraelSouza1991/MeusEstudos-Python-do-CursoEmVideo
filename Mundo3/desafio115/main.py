from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    print('=='*50)
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo(arq)

    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[31mERRO, digite um a opção Válida\033[m')
    sleep(2)
