# 082 - Crie um programa que vai ler vários números e colocar em uma lista.
#       Depois disso, crie duas listas extras que vão conter apenas os valores
#       pares e os valores ímpares digitados, respectivamente.
#       Ao final, mostre o conteúdo das três listas geradas.

num = []
par = []
impar = []

while True:
    num.append(int(input('Diigte um número')))

    prg = str(input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m] ? ')).strip().upper()
    if prg == '':
        prg = ' '
    if prg[0] == 'N':
        break

num.sort()  # Orderna os números da lista

for c in num:

    if c % 2 == 0:  # PAR
        par.append(c)

    else:           # IMPAR
        impar.append(c)

# Mostragem

print('\n'+'~'*35)
print(f'Valores da lista: {num}')
print(f'Valores \033[34mpares\033[m: {par}')
print(f'Valores \033[35mimpares\033[m: {impar}')
print('~'*35)
