# 113 - Reescreva a função leiaInt() que fizemos no desafio 104,
#       incluindo agora a possibilidade da digitação de um número
#       de tipo inválido. Aproveite e crie também uma função leiaFloat()
#       com a mesma funcionalidade.

def leiaint(msg='Digite um número'):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print(f'\033[31mErro: {erro.__class__}\033[m')
            continue
        else:
            return n


def leiafloat(msg='Digite um número Real'):
    while True:
        try:
            n = float(input(msg))
        except Exception as erro:
            print(f'\033[31mErro: {erro.__class__}\033[m')
            continue
        else:
            return n


leiaint()
leiafloat()
