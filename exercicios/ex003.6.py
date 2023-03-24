#  095 - Aprimore o desafio 93 para que ele funcione com vários jogadores,
#        incluindo um sistema de visualização de detalhes do aproveitamento
#        de cada jogador.

from time import sleep

num = 1
futebol = dict()

# INSERIR DADOS

while True:
    jogador = {'nome': str(input('\nDigite o nome do jogador: ')).strip().title()}
    partida = list()
    partida.clear()
    total = 0

    for c in range(1, int(input(f'  Quantas partidas {jogador["nome"]} jogou? '))+1):
        partida.append(int(input(f'     Número de gols na partida {c}? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)

    futebol[f'jogador {num}'] = jogador
    num += 1

    while True:
        prg = str(input('\nDeseja adicionar mais um jogador [S/N] ?')).strip().upper()
        if prg == '':
            prg = 'S'
        if prg == 'S' or prg == 'N':
            break
        else:
            print('\033[31mValor inválido, tente novamente.\033[m')
    if prg == 'N':
        print('\nFinalizando', end='')
        for c in range(0, 5):
            print('.', end='')
            sleep(0.5)
        print('.\n')
        break

# MOSTRAR DADOS

for posi, jogadores in futebol.items():  # Posição e Jogador
    print('='*30)
    print(f'{posi:<15} ', end='')
    cont = 0
    for k, v in jogadores.items():  # Jogador e informações
        if cont == 0:  # Nome Jogador
            print(f'{v:^15}')
            cont += 1
            print('~' * 30)
        elif cont == len(jogadores)-1:  # Total de gols
            print('~' * 30)
            print(f'Total de gols: {v:^15}')
            print()
        else:  # Lista de gols
            for c in range(0, len(v)):  # Gols por partida
                print(f'Gols prt {c+1}:    {v[c]:^15}')
            cont += 1

# PESQUISAR DADOS

while True:
    futebolspc = dict()
    while True:  # Escolher jogador
        jgd = int(input('Mostrar dados de qual jogador [999 finalzia] ? '))
        if jgd == 999:
            break
        elif f'jogador {jgd}' in futebol:
            futebolspc = futebol[f'jogador {jgd}'].copy()
            cont = 0
            for k, v in futebolspc.items():  # Jogador e informações
                if cont == 0:  # Nome
                    print('\n'+'=' * 30)
                    print(f'{v:^30}')
                    cont += 1
                    print('~' * 30)
                elif cont == len(futebolspc) - 1:  # Total de gols
                    print('~' * 30)
                    print(f'Total de gols: {v:^15}')
                    print()
                else:  # Lista de gols
                    for c in range(0, len(v)):  # Gols por partida
                        print(f'Gols prt {c + 1}:    {v[c]:^15}')
                    cont += 1
            break
        else:
            print('\033[31mValor inválido, tente novamente.\033[m')
    if jgd == 999:
        break
