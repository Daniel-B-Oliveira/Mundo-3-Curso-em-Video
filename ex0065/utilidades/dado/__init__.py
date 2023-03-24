def leiadinheiro(msg=''):
    while True:
        txt = str(input(msg)).replace(',', '.')
        if txt.isalpha() or txt.strip() == '':
            print('\033[31mValor inválido, tente novamente.\033[m')
        else:
            break
    return float(txt)
