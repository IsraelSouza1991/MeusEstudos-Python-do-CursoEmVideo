# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Informe a frase: ')).strip()
frasealt = frase.upper().replace(' ', '')\
    .replace('À', 'A').replace('Á', 'A').replace('Ã', 'A')\
    .replace('É', 'E').replace('Ê', 'E').replace('È', 'E')\
    .replace('Í', 'I').replace('Ì', 'I')\
    .replace('Ó', 'O').replace('Ô', 'O').replace('Ò', 'O').replace('Õ', 'O')\
    .replace('Ú', 'U').replace('Ù', 'U')
contrario = ''
for c in range(len(frasealt)-1, -1, -1):
    contrario += frasealt[c]
# é possível inverter por fatiamento de string
if frasealt == contrario:
    print('A frase \033[4m{}\033[m é Palíndromo.'.format(frase))
else:
    print('A frase \033[4m{}\033[m não é palindromo.'.format(frase))
