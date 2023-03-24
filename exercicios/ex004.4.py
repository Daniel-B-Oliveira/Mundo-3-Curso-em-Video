# 099 - Faça um programa que tenha uma função chamada maior(),
#       que receba vários parâmetros com valores inteiros.
#       Seu programa tem que analisar todos os valores e
#       dizer qual deles é o maior.

def maior(*v):
    g = 0
    print('-='*20)
    print('Todos os valores:', end=' ')
    for n in range(0, len(v)):
        if n == 0:
            g = v[n]
        if v[n] >= g:
            g = v[n]
        if n < len(v)-1:
            print(f'{v[n]}', end=' - ')
        else:
            print(f'{v[n]}')
    print(f'Maior valor: {g}')


maior(5, 7, 9, 3)
maior(1, 2, 3, 4)
maior(1, 2)
maior(99, 323,32, 123 )
