# 088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#       O programa vai perguntar quantos jogos serão gerados e vai sortear
#       6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
#       lista composta.

from random import choice
# from time import sleep
num0 = []
sort = []

for c in range(0, 61):
    num0.append(c)

prt = int(input('Quantos jogos serão feitos: '))

for c in range(1, prt+1):
    num = num0[:]  # Sempre reseta a lista num
    for p in range(0, 6):
        n = choice(num)
        sort.append(f'{n:02}')
        num.remove(n)
    if len(sort) == 6:
        # sleep(0.3)
        print(f'Jogo {c:{len(str(prt))}}º: {sort}')
    sort.clear()
