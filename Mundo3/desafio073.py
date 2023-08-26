# Exercício Python 73:
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

cbf = ('Atlético Mineiro - MG', 'Flamengo - RJ', 'Palmeiras - SP', 'Fortaleza - CE', 'Corinthians - SP',
       'Bull Bragantino - SP', 'Fluminense - RJ', 'America - MG', 'Atlético - GO', 'Santos - SP', 'Ceará - CE',
       'Internacional - RS', 'São Paulo - SP', 'Athletico Paranaense - PR', 'Cuiabá - MT', 'Juventude - RS',
       'GrÊmio - RS', 'Bahia - BA', 'Sport - PE', 'Chapecoense - SC')
print(f'Os 5 primeiros: {cbf[0:5]}\n')
c = len(cbf)
print(f'Os últimos 4 colocados: {cbf[c - 4:c]}\n')
print(f'Times em ordem alfabética: {sorted(cbf)}\n')
pos = cbf.index('Chapecoense - SC')
print(f'Chapecoense está na {pos + 1}ª posição\n')
print(f'Times de São Paulo: ')
sp = ' - SP'
for c in range(0, len(cbf)):
    time = cbf[c]
    if time.find(sp) > -1:
           print(time)
    c += 1
