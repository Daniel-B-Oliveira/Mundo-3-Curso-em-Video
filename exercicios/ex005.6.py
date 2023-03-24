# 106 - Faça um mini-sistema que utilize o Interactive Help do Python.
#       O usuário vai digitar o comando e o manual vai aparecer.
#       Quando o usuário digitar a palavra ‘FIM’, o programa
#       se encerrará. Importante: use cores.

def titulo(msg, cor='\033[m'):
    print(f'{cor}~'*int(len(msg))*2)
    print(f'{msg:^{int(len(msg))*2}}')
    print('~'*int(len(msg))*2)
    print('\033[m', end='')


def ajudac(arg):
    titulo(f'Acessando "{arg}"', '\033[46m')
    print('\033[7;40m', end='\n')
    print(f'{help(arg)}\n')
    print(f'\033[m', end='')


while True:
    titulo('Sistema de Ajuda PyHELP', '\033[1;44m')
    prg = str(input('Função ou bilioteca > ')).strip().lower()
    if prg == 'fim':
        titulo('Finalizando sistema de ajuda PyHELP', '\033[7;31m')
        break
    ajudac(prg)
