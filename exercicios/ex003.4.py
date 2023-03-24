# 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#       O programa vai ler o nome do jogador e quantas partidas ele jogou.
#       Depois vai ler a quantidade de gols feitos em cada partida.
#       No final, tudo isso será guardado em um dicionário,
#       incluindo o total de gols feitos durante o campeonato.

jogo = {'Jogador': str(input('Nome do Jogador: ')).title().strip()}
partida = list()
total = 0

for c in range(1, int(input(f'Quantas partidas {jogo["Jogador"]} joogu? '))+1):
    partida.append(int(input(f'{" "*3}Número de gols na partida {c}? ')))
jogo['gols'] = partida[:]
jogo['total'] = sum(partida)

print('\n'+'~'*35)

print(f'Jogador: \033[36m{jogo["Jogador"]}\033[m\n')

for k, v in enumerate(jogo['gols']):
    print(f'Na {k+1:2}ª partida, fez {v:2} gols')

print(f'\nTotalizando em \033[36m{jogo["total"]}\033[m gols.')
