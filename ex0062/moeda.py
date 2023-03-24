# 108 - Adapte o código do desafio #107, criando uma função adicional
#       chamada moeda() que consiga mostrar os números como um
#       valor monetário formatado.

def aumenta(v=0, i=0, formato=False):
    i = 1 + i/100
    m = v * i
    return m if formato is False else moeda(m)


def diminuir(v=0, i=0, formato=False):
    i = 1 - i/100
    m = v * i
    return m if formato is False else moeda(m)


def dobro(v=0, formato=False):
    r = v * 2
    return r if formato is False else moeda(r)


def metade(v=0, formato=False):
    r = v / 2
    return r if formato is False else moeda(r)


def moeda(v=0.00, md='R$'):

    v = f'{float(v):.2f}'.replace('.', ',')
    d2 = list()
    cont = -6

    for c in range(-1, int(-len(v)-1), -1):
        d2.append(v[c][:])
        if c == cont:
            d2.append('.')
            cont += -3

    d2.reverse()

    for c in range(0, int(len(d2))):
        if d2[0] not in '123456789':
            d2.remove(d2[0])

    df = md+(''.join(d2))

    return df


def titulo(msg, crt='='):
    print(f'{crt}' * len(msg) * 2)
    print(f'{msg}'.center(len(msg)*2))
    print(f'{crt}' * len(msg) * 2)


def remumo(n=0, d=0, a=0, formato=True):
    func = [aumenta(n, a, formato), diminuir(n, d, formato),
            dobro(n, formato), metade(n, formato)]
    cab = [f'Aumento em {a}% de {moeda(n)}',
           f'Decrescimo em {d}% {moeda(n)}',
           f'Dobro de {moeda(n)}', f'Metade de {moeda(n)}']

    # soma do tamanho de n + d + a + (média de d + a)
    tm = (len(str(n) + str(d) + str(a)) + len(str(d)+str(a))//2) // 2
    for c in range(0, len(func or cab)):
        if c == 0:
            titulo(str(f'{" "*tm}RESUMO DO VALOR {" "*tm}'))
        print(f'{cab[c]:^{(tm+8)*2}}', end='')
        print(f'{func[c]:^{(tm+8)*2}}')
        print('-'*(tm+8)*4)


