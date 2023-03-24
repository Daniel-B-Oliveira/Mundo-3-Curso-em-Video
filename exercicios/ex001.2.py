# 079 - Crie um programa onde o usuário possa digitar vários valores numéricos
#       e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
#       será adicionado. No final, serão exibidos todos os valores únicos
#       digitados, em ordem crescente.
num = []
print('\033[36m!!!DIGITE VÁRIOS NÚMEROS SEM QUE ESTES SE REPITAM!!!\033[m\n')
while True:
    while True:
        dig = int(input('Digite um número: '))
        if dig not in num:
            num.append(dig)
            print('\033[32mValor adicioanado com sucesso.\033[m')
            break
        else:
            print('\033[31mValor repitido, tente outro!\033[m')
    while True:
        prg = str(input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m]')).strip().upper()
        if prg == '':
            prg = 'S'
        if prg in 'SN':
            break
        else:
            print('\033[31mDigite um carácter possível.\033[m')
    if prg == 'N':
        break

num.sort()
print(f'\n\033[1mVALORES:\033[m {num}')
