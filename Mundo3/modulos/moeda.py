def aumentar(n):
    acrescimo = float(input('Quanto deseja aumentar? '))
    return n + acrescimo


def diminuir(n):
    subtrair = float(input('Quanto deseja subtrair? '))
    return n - subtrair


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n, formmoeda=True):
    if formmoeda:
        ret = str(f'R$ {n:.2f}').replace('.', ',')
    else:
        ret = n
    return ret


def resumo(s, a, d):
    m = metade(s)
    do = dobro(s)
    print('-' * 40)
    print('          RESIMO DO VALOR')
    print('-' * 40)
    print(str(
        f'Seu salário é {moeda(s, True)}.'
        f'\nCom o aumento ficará: {moeda(a+s)};'
        f'\nConsiderando a subtração o salário será: {moeda(s-d)};'
        f'\nA metade do salário é {moeda(m)};'
        f'\ne o dobro é {moeda(do)}.'
    ))
