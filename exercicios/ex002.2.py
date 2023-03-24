# 085 - Crie um programa onde o usuário possa digitar sete valores numéricos
#       e cadastre-os em uma lista única que mantenha separados os valores
#       pares e ímpares. No final, mostre os valores pares e
#       ímpares em ordem crescente.

'''num = ['#', '#']
p = 0

for c in range(1, 8):
    v = int(input(f'{c}º Valor: '))
    if v % 2 == 0:
        num.insert(0, v)
        p = p+1
    else:
        num.insert(-1, v)

for c in num:
    if '#' in num:
        num.remove('#')


print(f'Valores \033[32mPares\033[m: {sorted(num[0:p])}')
print(f'Valores \033[31mImpares\033[m: {sorted(num[p:len(num)])}')'''

#       /           /           /           /           /           /

# Solução Curso em Video:

num = [[], []]

for c in range(1,8):
    n = int(input(f'{c}º Valor:'))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f'\nValores \033[32mPares\033[m: {num[0]}')
print(f'Valores \033[31mImpares\033[m: {num[1]}')
