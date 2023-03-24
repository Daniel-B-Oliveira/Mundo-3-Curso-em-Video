# 100 - Faça um programa que tenha uma lista chamada números
#       e duas funções chamadas sorteia() e somaPar().
#       A primeira função vai sortear 5 números e vai colocá-los
#       dentro da lista e a segunda função vai mostrar a soma entre
#       todos os valores pares sorteados pela função anterior.

def sorteio(lista, i, f, k):
    from random import randint
    if f - i == 0:
        lista.append(i or f)
    else:
        if k > len((range(i, f+1))):
            k = len((range(i, f+1)))
        while True:
            n = randint(i, f)
            if n not in lista:
                lista.append(n)
            if len(lista) == k:
                break


def somapar(lista):
    soma = 0
    print('Soma de:', end=' ')
    for c in lista:
        if c % 2 == 0:
            print(f'[{c}', end='] ')
            soma += c
    print(f'= {soma}')


numeros = []
sorteio(numeros, 1, 10, 11)
print(numeros)

somapar(numeros)
