# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    param n: obrigatório. Um número escolhido para sinalizar o inicial do fatorial.
    param show: para mostrar a fórmula.
    return: retorna o resultado para a função.
    """
    resultado = 1
    for f in range(n, 0, -1):
        n -= 1
        if show == True:
            print(f'{f}', end='')
            if n == 0:
                print(' = ', end='')
            else:
                print(' x ', end='')

        resultado = resultado * f
    return resultado


print(fatorial(5, 1))

test = 5 * fatorial(5)
print(test)
help(fatorial)