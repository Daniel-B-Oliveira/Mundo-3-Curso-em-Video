# 094 - Crie um programa que leia nome, sexo e idade de várias pessoas,
#       guardando os dados de cada pessoa em um dicionário e todos os
#       dicionários em uma lista. No final, mostre:
#           A) Quantas pessoas foram cadastradas
#           B) A média de idade
#           C) Uma lista com as mulheres
#           D) Uma lista de pessoas com idade acima da média
pessoas = list()
pessoa = dict()
pergunta = ['NOME: ', 'SEXO[M/F]: ', 'IDADE: ']

# Formação da lista:

while True:
    for c in range(len(pergunta)):
        pessoa[f'{pergunta[c]}'] = str(input(f'{pergunta[c]}')).upper().strip()
    pessoas.append(pessoa.copy())

    cnt = str(input('Deseja continhar [S/N] ?')).upper().strip()

    if cnt == 'N':
        break

print('\n'+'-='*25)

# Total de cadastros:

print(f'Total de possoas cadastradas: {len(pessoas)}')

# Média da idade + lista apenas com mulheres:

soma = 0
mulheres = list()

print(f'\nLista apenas de \033[31mmulheres\033[m:', end=' ')

for c in range(0, len(pessoas)):
    soma += int(pessoas[c]['IDADE: '])
    if pessoas[c]['SEXO[M/F]: '] == 'F':
        mulheres.append(pessoas[c]['NOME: '])
        print(f'\033[31m{pessoas[c]["NOME: "]}', end='...\033[m')

print(f'\n\nMédia de idade: \033[36m{soma/len(pessoas):.2f}\033[m anos.')

# lista apenas com pessoas de idade acima da média:

idade = list()
print(f'\nPessoas com \033[33midade\033[m acima da média:', end=' ')
for c in range(0, len(pessoas)):
    if int(pessoas[c]['IDADE: ']) > (soma/len(pessoas)):
        idade.append(pessoas[c]['NOME: '])
        print(f'\033[33m{pessoas[c]["NOME: "]}', end='...\033[m')

print('\n'+'-='*25)
