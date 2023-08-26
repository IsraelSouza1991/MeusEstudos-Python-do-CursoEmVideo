# Exercício Python 105:
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas():
    quant_notas = maiornota = menornota = soma = 0

    while True:
        nota = float(input('Digite a nota do aluno [Digite 999 para finalizar]: '))
        if nota == 999:
            break
        while nota > 10 or nota < 0:
            nota = float(input('Erro!\nNota inválida. Digite notamente: '))
        quant_notas += 1
        maiornota = nota if nota > maiornota else maiornota
        if menornota != 0:
            menornota = nota if nota < menornota else menornota
        else:
            menornota = nota
        soma += nota
    media = float(f'{soma / quant_notas:.2f}')
    if media < 7:
        situacao = 'A média está ruim'
    elif media == 10:
        situacao = 'A média está ótima'
    else:
        situacao = 'A média está boa'
    turma = {'Quantidade de notas': quant_notas, 'Maior Nota': maiornota,
             'Menor Nota': menornota, 'Média da Turma': media, 'Situação': situacao}
    return turma


print(notas())
