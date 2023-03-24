# 098 - Faça um programa que tenha uma função chamada contador(),
#       que receba três parâmetros: início, fim e passo. Seu programa
#       tem que realizar três contagens através da função criada:
#           a) de 1 até 10, de 1 em 1
#           b) de 10 até 0, de 2 em 2
#           c) uma contagem personalizada

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:  # Valor negatino não pode ser aceitado.
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        tm = len(str(cont)) + 3  # +3 por conta da palavra FIM
        while cont <= f:
            print(f'{cont}', end=' - ')
            cont += p
            tm += len(str(cont)) + 3  # Número + ' - '
        print('FIM!')
        print('=' * tm, '\n')
    else:
        cont = i
        tm = len(str(cont)) + 3
        while cont >= f:
            print(f'{cont}', end=' - ')
            cont -= p
            tm += len(str(cont)) + 3
        print('FIM!')
        print('=' * tm, '\n')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de persolaziar sua contagem: ')

contador(int(input('Inico: ')), int(input('Fim: ')), int(input('Razão: ')))
