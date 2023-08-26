def leiaInt(msg):
    """
        Função semelhante ao input(), mas este faz a validação para somente aceitar valores numéricos do tipo inteiro.
    """
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário interrompeu o programa!\033[m')
            return 0
        else:
            return n


def trocaparaponto(msg):
    valor = str(input(msg)).replace(',', '.').strip()
    return valor


def trocaparavirgula(msg):
    valor = str(msg).replace('.', ',')
    return valor


def leiaFloat(msg):

    while True:
        try:
            n = float(trocaparaponto(msg))
        except(ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário interroumpeu o programa.\033[m')
            return 0
        else:
            return n
