# 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#       No final, mostre qual foi o maior e o menor valor digitado e as suas
#       respectivas posições na lista.

numeros = []
m = p = 0

# VALORES

for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c+1}º valor: ')))
    # MAIOR E MENOR
    if c == 0:
        m = p = int(numeros[0])
    if int(numeros[c]) >= m:
        m = numeros[c]
    if int(numeros[c]) <= p:
        p = numeros[c]

print(f'\nValores da lista: {numeros}')

# MAIOR

print(f'\nMaior valor da lista: \033[32m{m}\033[m\nPosição:', end=' ')

for a, b in enumerate(numeros):
    if numeros[a] == m:
        print(a+1, end='ª...')
    if a == len(numeros)-1:
        print('')

# MENOR

print(f'\nMenor valor da lista: \033[31m{p}\033[m\nPosição:', end=' ')

for a, b in enumerate(numeros):
    if numeros[a] == p:
        print(a+1, end='ª...')
    if a == len(numeros)-1:
        print('')
