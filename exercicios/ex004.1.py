# 096 - Faça um programa que tenha uma função chamada área(),
#       que receba as dimensões de um terreno retangular
#       (largura e comprimento) e mostre a área do terreno.

def area(x, y):
    print(f'Área ({x:.1f} x {y:.1f}): \033[1m{x*y:.1f}\033[m m²')


def titulo(msg):
    print(f'\n\033[1m{msg.title().strip():^{len(msg.strip())*2}}\033[m')
    print('-'*len(msg.strip())*2)


titulo('Cálculo de Área')
area(int(input('Largura(m): ')), int(input('Comprimento(m): ')))
