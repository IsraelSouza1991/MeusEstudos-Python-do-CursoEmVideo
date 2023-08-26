# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


from time import sleep
print('MINI-SISTEMA UTILIZANDO INTERACTIVE HELP DO Python\nDigite SAIR ou EXIT caso queira sair.\n')
while True:
    print('\033[m\033[42m' + '~'*30 + '\n    SISTEMA DE AJUDA PyHELP\n' + '~'*30 + '\n\033[m')
    resp = str(input('Função ou Biblioteca > ')).lower().strip()
    if resp == 'sair' or resp == 'exit':
        print('\033[m\033[41m' + '~'*30 + '\n    ATÉ LOGO\n' + '~'*30 + '\n\033[m')
        break
    print('\n\033[0:30:44m' + '~'*50 + '\n' + f"\n    Acessando o manual do comando'{resp}'\n ", end='\n' +
          '~'*50 + '\n\033[m\033[7m')
    sleep(2)
    print(help(resp))
    sleep(2)
