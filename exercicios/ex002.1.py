# 084 - Faça um programa que leia nome e peso de várias pessoas,
#       guardando tudo em uma lista. No final, mostre:
#           A) Quantas pessoas foram cadastradas.
#           B) Uma listagem com as pessoas mais pesadas.
#           C) Uma listagem com as pessoas mais leves.

p = list()
g = list()
mai = men = 0
while True:
    p.append(str(input('NOME: ')).upper().strip())
    p.append(float(input('PESO: ')))
    # Maior e menor
    if len(g) == 0:
        mai = men = p[1]
    else:
        if p[1] > mai:
            mai = p[1]
        if p[1] < men:
            men = p[1]

    g.append(p[:])
    p.clear()
    prg = str(input('Deseja continuar [S/N] ? ')).strip().title()
    if prg == 'N':
        print('')
        break

print('~'*50)

# Pessoas cadastradas

print(f'\nPessoas cadastradas: {len(g)}')

# Média de peso.

c = 0

for m in g:
    c += int(m[1])

med = c/len(g)

# Pessoas com peso na média

print(f'\nPessoas com peso na média({med:.3f}Kg):', end=' ')
cont = 0
for k in g:
    if k[1] == med:
        print(f'\033[36m{k[0]}\033[m ({k[1]:.3f}Kg)', end='...')
        cont = 1
if cont == 0:
    print('\033[31mNão houve valor\033[m', end='')

# Pessoas com peso acima da média

cont = 0
print(f'\n\nPessoas com peso acima da média:', end=' ')
for k in g:
    if k[1] > med:
        print(f'\033[36m{k[0]}\033[m ({k[1]:.3f}Kg)', end='...')
        cont = 1
if cont == 0:
    print('\033[31mNão houve valor\033[m', end='')

    # Maior

print(f'\n\033[36mMaior peso ({mai:.3f}):\033[m', end=' ')

for k in g:
    if k[1] == mai:
        print(f'\033[36m{k[0]}\033[m', end='\033[36m...\033[m')

# Pessoas com peso abaixo da média

print(f'\n\nPessoas com peso abaixo da média:', end=' ')
cont = 0
for k in g:
    if k[1] < med:
        print(f'\033[36m{k[0]}\033[m ({k[1]:.3f}Kg)', end='...')
        cont = 1
if cont == 0:
    print('\033[31mNão houve valor\033[m', end='')

    # Menor

print(f'\n\033[36mMenor peso ({men:.3f}):\033[m', end=' ')

for k in g:
    if k[1] == men:
        print(f'\033[36m{k[0]}\033[m', end='\033[36m...\033[m')
print('\n\n'+'~'*50)
