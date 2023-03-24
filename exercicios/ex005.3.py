# 103 - Faça um programa que tenha uma função chamada ficha(),
#       que receba dois parâmetros opcionais: o nome de um jogador
#       e quantos gols ele marcou. O programa deverá ser capaz de
#       mostrar a ficha do jogador, mesmo que algum dado não tenha
#       sido informado corretamente.

def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = '<none>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print('~' * (24 + len(nome) + len(str(gols))))
    print(f'Jogador(a) {nome} fez {gols} gol(s)')
    print('~' * (24 + len(nome) + len(str(gols))))


nome0 = str(input('Digite o nome do jogador: ')).strip().title()
gols0 = str(input('Gols do jogador: '))

ficha(nome0, gols0)
