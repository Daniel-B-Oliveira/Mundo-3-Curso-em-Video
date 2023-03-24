# 092 - Crie um programa que leia nome, ano de nascimento e carteira
#       de trabalho e cadastre-o (com idade) em um dicionário. Se por
#       acaso a CTPS for diferente de ZERO, o dicionário receberá também
#       o ano de contratação e o salário. Calcule e acrescente, além da idade,
#       com quantos anos a pessoa vai se aposentar.

from datetime import date

prg = ['Nome: ', 'Ano de nascimento: ', 'Carteira de trabalho: ',
       'Ano de contratação: ', 'Salário:R$ ']
user = dict()

for c in range(0, 3):
    if c == 1:
        user[f'{prg[c]}'] = int(input(prg[c]))
        user[f'Idade: '] = date.today().year - user[f'{prg[c]}']
    else:
        user[f'{prg[c]}'] = str(input(prg[c])).strip().title()

if user['Carteira de trabalho: '] != '0':
    for c in range(3, 5):
        user[f'{prg[c]}'] = int(input(prg[c]))
    user['Aposentadoria: '] = user[f'Idade: '] + user['Ano de contratação: '] + 35 - date.today().year

print('\n'+'-='*25)
print(f'{"CADASTRO":^50}')
print('-='*25+'\n')

for k, v in user.items():
    print(f'{k:<25}{v:>25}')
    print('--' * 25)
