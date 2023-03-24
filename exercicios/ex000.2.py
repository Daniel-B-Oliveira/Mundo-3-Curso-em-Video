# 073 - Crie uma tupla preenchida com os 20 primeiros colocados da
#       Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#       Depois mostre:
#        a) Os 5 primeiros times.
#        b) Os últimos 4 colocados.
#        c) Times em ordem alfabética.
#        d) Em que posição está o time da Chapecoense.

times = ('ZERO', 'Parlmeiras', 'Internacional', 'Flumninense', 'Conrinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
         'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'{" BRASILEIRÃO 2022 ":-^45}')

# times

cor = 31
print('\n- TIMES: ', end='')

for c in range(1, 21):
    if c == 20:
        print(f'\033[{cor}m{times[c]}\033[m', end='.')
    else:
        print(f'\033[{cor}m{times[c]}\033[m', end=', ')
    cor += 1
    if cor == 37:
        cor = 31

# 5 primeiros

cor = 31
print(f'\n\n- 5 primeiros colocados (\033[36m1º-5º\033[m): ', end='')

for c in range(1, 6):
    if c == 5:
        print(f'\033[{cor}m{times[c]}\033[m', end='.')
    else:
        print(f'\033[{cor}m{times[c]}\033[m', end=', ')
    cor += 1

# 4 últimos

cor = 34
print(f'\n\n- 4 último colocados (\033[36m17º-20º\033[m): ', end='')

for c in range(17, 21):
    if c == 20:
        print(f'\033[{cor}m{times[c]}\033[m', end='.')
    else:
        print(f'\033[{cor}m{times[c]}\033[m', end=', ')
    cor -= 1

# Ordem Alfabética

cor = 31
atime = sorted(times)
print('\n\n- Times em ordem alfabética: ', end=' ')

for c in range(0, 21):
    if c == 20:
        print(f'\033[{cor}m{atime[c]}\033[m', end='.\n')
    else:
        print(f'\033[{cor}m{atime[c]}\033[m', end=', ')
    cor += 1
    if cor == 37:
        cor = 31
