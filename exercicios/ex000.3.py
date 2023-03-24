# 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em
#       uma tupla.Depois disso, mostre a listagem de números gerados e
#       também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (randint(0, 9), randint(0, 9), randint(0, 9),
       randint(0, 9), randint(0, 9))

print('Números Gerados:', end=' ')

for c in range(0, len(num)):
    if c == len(num)-1:
        print(num[c])
    else:
        print(num[c], end=' - ')

print(f'Menor Valor: \033[31m{sorted(num)[0]}\033[m\n'
      f'Maior Valor: \033[32m{sorted(num)[len(num)-1]}\033[m')
