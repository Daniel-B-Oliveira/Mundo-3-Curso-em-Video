# 089 - Crie um programa que leia nome e duas notas de vários alunos
#       e guarde tudo em uma lista composta. No final, mostre um boletim
#       contendo a média de cada um e permita que o usuário possa mostrar
#       as notas de cada aluno individualmente.

boletins = []

# Cadastras notas e nomes

while True:
    nm = str(input('NOME: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    md = (n1+n2)/2
    op = [nm, [n1, n2], md]
    boletins.append(op[:])
    prg = str(input('Continuar [\033[32mS\033[m/\033[31mN\033[m] ? ')).strip().upper()
    if prg == 'N':
        break

boletins.sort()  # Coloca os nomes em ordem alfabética

cont = 1

# Mostrar as notas mais as médias, ou somente as médias

while True:
    prg = str(input('Mostrar somente as médias [\033[32mS\033[m/\033[31mN\033[m] ? ')).strip().upper()
    if prg == '':
        prg = 'S'
    if prg == 'N':  # Mostra notas e médias
        print('~' * 66)
        print(f'{"BOLETIM ESCOLAR":^66}')
        print('~' * 66)
        for c in boletins:  # [0] = aluna,  [1] [0] = nota 1, [1] [1] = nota 2, [2] = media
            print(f'{cont:03} - {c[0]:<15} '
                  f'Nota1: {c[1][0]:>4.1f}{" "*5}'
                  f'Nota2: {c[1][1]:>4.1f}{" "*5}'
                  f'Média: {c[2]:>4.1f}{" "*5}')
            cont += 1
        print('~' * 66)
        break

    elif prg == 'S':  # Mostrar apenas notas
        print('~' * 33)
        print(f'{"BOLETIM ESCOLAR":^33}')
        print('~' * 33)
        for c in boletins:  # [0] = aluna,  [1] [0] = nota 1, [1] [1] = nota 2, [2] = media
            print(f'{cont:03} - {c[0]:<15}'
                  f'Média: {c[2]:>4.1f}{" "*5}')
            cont += 1
        print('~' * 33)
        pos = 0  # Usado para parar quando o usário digitar 999
        while True: # Pesquisar Notas Separadamente
            med = str(input('Pesquisar notas por aluno individualmente [\033[32mS/\033[31mN\033[m] ? ')).strip().upper()
            if med == '':
                med = 'S'

            if med == 'S':
                print('\nDigite o número do aluno para saber sua nota [\033[31m999 FINALIZA\033[m]:\n')
                while True:
                    pos = int(input('NÚMERO: '))
                    if pos == 999:
                        break
                    else:
                        if len(boletins) > 1:  # Mais que um aluno
                            if pos < len(boletins)+1 and pos != 0:
                                print(f'{pos:03} - {boletins[pos-1][0]:<15} '
                                      f'Nota1: {boletins[pos-1][1][0]:>4.1f}{" " * 5}'
                                      f'Nota2: {boletins[pos-1][1][1]:>4.1f}{" " * 5}'
                                      f'Média: {boletins[pos-1][2]:>4.1f}{" "*5}')
                            else:
                                print('\033[31mValor Ipossível, tente outro\033[m')
                        else:
                            if pos == len(boletins):  # Apenas um aluno
                                print(f'{pos:03} - {boletins[pos-1][0]:<15} '
                                      f'Nota1: {boletins[pos-1][1][0]:>4.1f}{" " * 5}'
                                      f'Nota2: {boletins[pos-1][1][1]:>4.1f}{" " * 5}'
                                      f'Média: {boletins[pos-1][2]:>4.1f}{" "*5}')
                            else:
                                print('\033[31mValor Ipossível, tente outro\033[m')
            elif med == 'N':
                break
            else:
                print('\033[31mValor Ipossível, tente outro\033[m')
            if pos == 999:
                break
        break
    else:
        print('\033[31mValor Ipossível, tente outro\033[m')
