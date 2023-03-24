# 102 - Crie um programa que tenha uma função fatorial() que receba
#       dois parâmetros: o primeiro que indique o número a calcular
#       e outro chamado show, que será um valor lógico (opcional)
#       indicando se será mostrado ou não na tela o processo de
#       cálculo do fatorial.

def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: numero utilizado
    :param show: Mostrar ou não as operações
    :return: fatorial de numero
    """

    mult = 1
    if numero == 0:
        numero = 1  # Fatorial de 0 é 1
    for c in range(numero, 0, -1):
        mult *= c
        if show is True:
            if c == numero:
                print(f'{numero}! = {c}', end=' * ')
            elif c == 1:
                print(c, end=f' = {mult}')
            else:
                print(c, end=' * ')
    if show is False:
        print(f'{numero}! = {mult}')


fatorial(5, show=False)
