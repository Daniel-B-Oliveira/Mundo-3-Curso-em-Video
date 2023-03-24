
'''Já consigo formar a matriz e rotaciona-la, ainda falta conseguir fazer as diagonais'''

from itertools import combinations, combinations_with_replacement
numeros = list()
nummin = list()
camadas = list()
linhas = list()
colunas = list()
t = 3

for c in range(0, t**3):  # Números para matrizes
    numeros.append(c)
for c in range(0, t):  # Números para cordenadas
    nummin.append(c)

# Cordenadas

a1 = combinations_with_replacement(nummin,t)
cordenadas = list(a1) # Todas as conbinações possivel de cordenadas

'''diagonias = []

cont = 0

for c1 in range(len(str(cordenadas))):  # Cordenada Especifica
    cont = 0
    for c2 in range(0, t): # Valor da cordenada
        if cordenadas[c1][cont] != cordenadas[c1][c2]:
            diagonias.insert(0,cordenadas[c1][cont])
            diagonias.index(0,cordenadas[c1][c2])
print(diagonias)'''

# Formação da Matriz

for c1 in range(0, t):
    for c2 in range(0, t):
        for c3 in range(0, t):
            colunas.append(numeros[0])
            numeros.remove(numeros[0])
        linhas.append(colunas[:])
        colunas.clear()
    camadas.append(linhas[:])
    linhas.clear()

matriz = list(camadas[:])

maior = len(str(matriz[-1][-1][-1]))

'''# Rotações do cubo

x = y = z = 0
print(camadas)
cam = [camadas[x][z][y],camadas[z][y][x],camadas[y][x][z],
       camadas[x][y][z],camadas[z][x][y],camadas[y][z][x]]'''

for z in range(0, t):  # CAMADAS
    for y in range(0, t):  # LINHAS
        for x in range(0, t):  # COLUNAS
            print(f'[{matriz[z][y][x]:>{maior}}]', end=' ')
        print()
    print()

# Diagonal principal e secundária:
dig_pri = []
dig_sec = []

for z in range(len(matriz)):
    for y in range(len(matriz)):
        for x in range(len(matriz)):
            if z == y == x:
                dig_pri.append(matriz[z][y][x])
            if z + y + x == len(matriz):
                dig_sec.append(matriz[z][y][x])

print(dig_pri)
print(dig_sec)