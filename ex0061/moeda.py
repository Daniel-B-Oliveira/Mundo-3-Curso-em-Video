# 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas
#       aumentar(), diminuir(), dobro() e metade().
#       Faça também um programa que importe esse módulo
#       e use algumas dessas funções.

def aumenta(v=0, i=0):
    i = 1 + i/100
    m = v * i
    return m


def diminuir(v=0, i=0):
    i = 1 - i/100
    m = v * i
    return m


def dobro(v=0):
    r = v * 2
    return r


def metade(v=0):
    r = v / 2
    return r
