# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade
# se ele ainda vai se alistar ao serviço militar
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from time import sleep
from datetime import datetime

anoatual = datetime.now().year  # Lê Ano atual do computador
name = str(input('Digite seu nome completo: ').strip())  # Recebe nome do usuário
namefat = name.split()  # Fatiamento do nome para pegar o primeiro nome

ano = int(input('Em que ano você nasceu? '))
if ano > anoatual or ano < 1900:
    print('--=--' * 3)
    print('Há algo errado no número digitado. é necessário ter 4 digitos!')
else:
    print('''Precisamos saber de qual sexo você é!
   
            Importante!!!
    ...escolha M para Masculino
    ou F para Feminino...
    
    ''')
    sexo = str(input('... Por favor, Digite: ')).upper().strip()
    print('Por favor, aguarde!. Estamos processando as informações...')
    sleep(3)
    idade = anoatual - ano

    # SE FOR MULHER

    if sexo == 'F':
        print('{}, não será necessário o alistamento! Por ser mulher não há obrigatoriedade.'.format(namefat[0]))

    # SE FOR HOMEM COM 18 ANOS

    elif sexo == 'M' and idade == 18:
        print('Sr. {}, Será necessário se alistar!'.format(namefat[0]))
        sleep(2)
        rg = input('Informe seu número de RG para iniciarmos o registro \n '
                   'ou verificarmos se já realizou o alistamento. (Apenas os números): ')

        # SE FOR HOMEM MAIOR DE 18

    elif sexo == 'M' and idade > 18:
        print('Sr. {}, você tem mais que 18 anos, é necessário verificar pois já se passou {} anos para realizar '
              'o alistamento.'.format(namefat[0], idade - 18))

        # SE FOR HOMEM MENOR DE 18

    elif sexo == 'M' and idade < 18:
        print('Sr. {}, não tem idade para se alistar. Deverá voltar daqui {} ano{}!'.format(namefat[0], 18 - idade, 's'
        if (18 - idade) > 1 else ''))
    else:
        print('Não foi digitado um númeto válido!')
print('--=--'*3)

#\033[7;30m