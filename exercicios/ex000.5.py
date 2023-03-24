# 076 - Crie um programa que tenha uma tupla única com nomes de produtos e seus
#       respectivos preços, na sequência. No final, mostre uma listagem de preços,
#       organizando os dados em forma tabular.

pdt = ('Mixer', 345,
       'Liquidificador', 650,
       'Sanduicheira', 189,
       'Forninho Elétrico', 789,
       'Máquina de lavar louça', 1550,
       'Geladeira', 1755,
       'Fogão', 1349,
       'Cafeteira', 689,
       'Adega Climatizada', 1350,
       'Aspirados de pó', 899,
       'Ferro á vapor vertical', 1199)

for c in range(0, len(pdt)):
    if c == 0:
        print('-' * 55)
        print(f'{"LISTAGEM DE PREÇOS":^55}')
        print('-'*55)
    if c % 2 == 0:
        print(f'{pdt[c]:.<40}', end='')
    elif c % 2 != 0:
        print('R$', f'{pdt[c]:>10.2f}')
    if c == len(pdt)-1:
        print('-' * 55)
        