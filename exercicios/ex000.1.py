# 072 - Crie um programa que tenha uma dupla totalmente preenchida com uma
#       contagem por extenso , de zero até vinte. Seu programa deverá ler
#       um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesesis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    p = int(input('Digite um número entre 0 e 20: '))
    if p in range(0, 21):
        break
    else:
        print('\033[31m[ERRO]\033[m', end='')

print(f'\nVocê digitou o número \033[36m{num[p]}\033[m.')
