# 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar
#       de forma semelhante á função input() do Python, só que fazendo
#       a validação para aceitar apenas um valor numérico.
#       Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric() is False:
            print('\033[31mDigite um valor válido.\033[m')
        else:
            val = num
            break
    return val


numero = leiaint('Digite um número: ')
print(f'Voce acabou de digitar {numero}.')
