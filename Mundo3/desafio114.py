# Exercício Python 114:
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib as u
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')

except:
    print('O site dupim não está acessível no momento!')
else:
    print('Consegui acessar o site!')