# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto():
    from datetime import date
    y = date.today().year
    print('-' * 20)
    ano_nascimento = int(input('Informe o Ano de nascimento: '))
    idade = y - ano_nascimento

    # voto negado para menor de 16.
    if idade < 16:
        return f'Você tem apenas {idade} anos.\nO voto foi negado!'

    # voto opcional entre 16 e 17, e acioma de 65.
    elif idade == 16 or idade < 18 or idade > 65:
        return f'Você tem {idade} anos.\nPortanto o voto é opcional!'

    # voto obrigatório para os maiores de 17, então a partir de 18 deve votar.
    else:
        return f'Você tem {idade} anos. É obrigatório que realize seu voto!'


resp = voto()
print(resp)
