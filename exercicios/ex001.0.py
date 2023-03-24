'''num = [1, 2, 3, 4, 5]
print(num)
del num[0]  # Posição.
num.remove(3)  # Valor.
num.pop()  # Caso valor não informado removo o último elemento na lista
print(num)

#       /           /           /           /           /

v = list(range(0, 11, 2))
v.sort()
v.sort(reverse=True)  # Inverte a ordem da listagem
v.append(91)  # Adiciona números
v.insert(2, 3)  # Posição e Valor
v.remove(2)  # Elimina a primeira aparição do elemento
if 97 in v:
    v.remove(97)
else:
    print('Valor 97 não encontrado')
print(v)'''

#       /           /           /           /           /

''''h = list()

for cont in range(1, 11):
    h.append(int(input(f'Digite o {cont}º valor:')))

h = sorted(h)
print(h)

for c, p in enumerate(h):
    print(f'{c+1}ªPosição, Valor {p}.')'''''

#       /           /           /           /           /

a = [1, 2, 3, 4, 5, 6]
# b = a
# b[5] = 99  # As listas se conctan, logo, b[5] = 99 e a[5] = 99

b = a[:]  # Cria uma cópia da lista
b[5] = 99

print(a)
print(b)

