# 097 - Faça um programa que tenha uma função chamada escreva(),
#       que receba um texto qualquer como parâmetro e mostre uma
#       mensagem com tamanho adaptável.

def escreva(msg):
    txt = str(f'{msg}').strip().title()
    tam = len(txt)+4
    print('~'*tam)
    print(f'\033[1m{txt:^{tam}}\033[m')
    print('~' * tam)

escreva('Olá, mundo!')
escreva('Bom dia!!!')
escreva('BOA NOITE GALERA')
