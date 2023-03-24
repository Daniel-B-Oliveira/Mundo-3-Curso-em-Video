# 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#       em uma tupla. No final, mostre:
#           A) Quantas vezes apareceu o valor 9.
#           B) Em que posição foi digitado o primeiro valor 3.
#           C) Quais foram os números pares.

nt = (int(input('Digite um valor: ')),
      int(input('Digite outro valor: ')),
      int(input('Digite mais um valor: ')),
      int(input('Digite o último  valor: ')))

print(f'\nNúmeros: {nt}')
# espaços

m = 0
for c in range(0, len(nt)):
    if c == 0:
        m = nt[c]
    if nt[c] >= m:
        m = nt[c]

# Quantas vezes apareceu o valor 9.

print('\n'+'~'*(len(str(m)) + 25))  # espaço

print(f'Ocorrência(s) de [\033[36m9\033[m]: {nt.count(9)}')

# Em que posição foi digitado o primeiro valor 3.

if 3 in nt:
    print(f'1ª aparição de [\033[36m3\033[m]: {nt.index(3)+1}')
else:
    print(f'1ª aparição de [\033[36m3\033[m]: \033[31mnão houve a aparição de 3\033[m')

# C) Quais foram os números pares.

print('Números \033[1mpares\033[m: ', end='')
p = 0
for c in range(0, len(nt)):
    if nt[c] % 2 == 0:
        print(nt[c], end='  ')
        p += 1
    if p == 0 and c == len(nt)-1:
        print('\033[31mNão houve valores pares\033[m')

print('\n'+'~'*(len(str(m)) + 25))  # espaço
