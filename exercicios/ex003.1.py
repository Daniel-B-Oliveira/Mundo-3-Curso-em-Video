# 090 - Faça um programa que leia nome e média de um aluno,
#       guardando também a situação em um dicionário.
#       No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Digite seu nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:  # Aluno aprovado
    aluno['situação'] = 'APROVADO(A)'

elif aluno['media'] < 5:  # Aluno reprovado
    aluno['situação'] = 'REPROVADO(A)'

else:                     # Aluno em recuperação
    aluno['situação'] = 'EM RECUPERAÇÃO'

for k, v in aluno.items():
    print(f'{k} é ingual a {v}.')
