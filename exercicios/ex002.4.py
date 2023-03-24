# 087 - Aprimore o desafio anterior, mostrando no final:
#           A) A soma de todos os valores pares digitados.
#           B) A soma dos valores da terceira coluna.
#           C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col3 = maior = matrizm = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor ({l+1},{c+1}): '))
        if matriz[l][c] % 2 == 0:  # Soma de pares
            par += matriz[l][c]
        if matriz[l][c] is matriz[l][2]:  # Soma da terceira coluna
            col3 += matriz[l][c]
        if matriz[l][c] is matriz[1][c]:  # maior valor da linha 1, 2ª linha.
            if c == 0:
                maior = matriz[l][c]
            if matriz[l][c] >= maior:
                maior = matriz[l][c]

for t in matriz:
    for m in t:
        if m == [0][0]:
            matrizm = int(m)
        if int(m) >= matrizm:
            matrizm=int(m)

print(f'\n{"~"*(len(str(matrizm))*3+8)}')

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:0>{len(str(matrizm))}}]', end=' ')
    if l < 2:
        print()
print(f'\n{"~"*(len(str(matrizm))*3+8)}')
print(f'\nSoma de todos os pares: {par}')
print(f'Soma da terceira coluna: {col3}')
print(f'Maior valor da 2ª linha: {maior}')