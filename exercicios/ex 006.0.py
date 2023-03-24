# Teste de todos os módulos: ex006.1 - ex006.6

'''from ex0061 import moeda

valor = float(input('Digite um valor: R$'))
taxa = float(input('Digite a porcentagem do aumento: '))
print(f'Valor aumento({taxa}%): R${moeda.aumenta(valor, taxa)}')
print(f'Valor diminuido({taxa}%: R${moeda.diminuir(valor, taxa)}')
print(f'Valor dobrado: R${moeda.dobro(valor)}')
print(f'Valor pela metade: R${moeda.metade(valor)}')
'''

from ex0062 import moeda

valor = float(input('Digite um valor: R$'))
taxa = float(input('Digite a porcentagem do aumento: '))

print(f'{moeda.moeda(valor)} aumentado ({taxa}%): {moeda.aumenta(valor, taxa,formato=True)}')
print(f'{moeda.moeda(valor)} diminuido({taxa}%: {moeda.diminuir(valor, taxa,formato=True)}')
print(f'{moeda.moeda(valor)} dobrado: {moeda.dobro(valor,formato=True)}')
print(f'{moeda.moeda(valor)} pela metade: {moeda.metade(valor,formato=True)}')

moeda.remumo(valor, taxa, taxa)
