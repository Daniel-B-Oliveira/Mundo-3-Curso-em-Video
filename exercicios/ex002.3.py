# 086 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha
#       com valores lidos pelo teclado. No final, mostre a matriz na tela,
#       com a formatação correta

mat = list()
linha = list()
numeros = list()
v = 3
vlinha = vmatriz = maiorlinha = maiormatriz = 0
zero = 0  # troque 0 por 1 para a lista começar com 0

# Crias lista de números:
for c in range(1-zero, v**2+1-zero):
    numeros.append(c)

for c0 in range(0, v):  # Forma a matriz linha por linha
    for c1 in range(0, v):  # Forma a linha
        vlinha = int(input(f'Valor ({c0+1},{c1+1})'))  # adicionar manualmente
        # vlinha = numeros[0]  # usar números em ordem crescente
        numeros.remove(numeros[0])
        linha.append(vlinha)
        # maior Valor da Linha
        if c1 == 0:
            maiorlinha = vlinha
        if vlinha >= maiorlinha:
            maiorlinha = vlinha
    # maior Valor da Matriz
    vmatriz = maiorlinha
    if c0 == 0:
        maiormatriz = vmatriz
    if vmatriz >= maiormatriz:
        maiormatriz = vmatriz

    mat.append(linha[:])
    linha.clear()

maior = len(str(maiormatriz))

for c2 in range(0, v):
    for c3 in range(0, v):
        sn = 0  # Verificar se este valor ja foi impresso.
        posi = str(mat[c2][c3])
        if len(posi) < maior:
            if maior % 2 == 0:  # LEN de Maior par; numero atual impar
                if len(posi) % 2 != 0:
                    print(f'[{"0"+posi:^{maior}}]', end=' ')
                    sn = 1
            else:               # LEN de Maior impar, número atual  par
                if len(posi) % 2 == 0:
                    print(f'[{"0"+posi:^{maior}}]', end=' ')
                    sn = 1
        if sn == 0:
            print(f'[{posi:^{maior}}]', end=' ')
    print('')
