'''def soma(a=0, b=0, c=0):
    """
    -> Faz a soma entre três valores e mostra o resultado.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Curso em Video, aula 21 funções(2)
    """
    global d  # Variável Global
    s = a + b + c
    print(f'A soma vale {s}')

d = 1
'''


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(1, 2, 3)
r3 = soma(5, 5, 5)

print(f'Meus calculos foram: {r1}, {r2}, {r3}')


