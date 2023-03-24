# 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados
#       aleatórios. Guarde esses resultados em um dicionário em Python.
#       No final, coloque esse dicionário em ordem, sabendo que o vencedor
#       tirou o maior número no dado

from random import randint
from operator import itemgetter

jogo = {}
ranking = list()


for c in range(1,5):
    jogo[f'jogador {c}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'{k} - tirou {v} no dado')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # 0 utiliza as chaves # 1 utiliza os elementos

print('\n'+'='*25)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: \033[1m{v[0]}\033[m com \033[1m{v[1]}\033[m')

print('='*25)