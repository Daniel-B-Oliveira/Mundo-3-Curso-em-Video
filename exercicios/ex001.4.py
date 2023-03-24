# 081 - Crie um programa que vai ler vários números e colocar em uma lista.
#       Depois disso, mostre:
#           A) Quantos números foram digitados.
#           B) A lista de valores, ordenada de forma decrescente.
#           C) Se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        prg = str(input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m] ? ')).strip().upper()
        if prg == '':
            prg = 'S'
        if prg in 'NS':
            break
        else:
            print('\033[31mValor Impossível, tente outro.\033[m')
    if prg == 'N':
        break

# Valores em Ordem Crescente

print('\n'+'~'*45+'\n')
lista.sort(reverse=True)
print(f'Os {len(lista)} valores da lista são: {lista}\n')

# Ausência de 5 ou Presença e Posição de 5

print('Posição Valor(\033[36m5\033[m): ', end='')
if 5 in lista:
    for p, c in enumerate(lista):
        if lista[p] == 5:
            print(f'{p+1}', end='ª...')
else:
    print('\033[31mNão se encontra na lista.\033[m', end='')
print('\n\n'+'~'*45+'\n')
