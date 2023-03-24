# 101 - Crie um programa que tenha uma função chamada voto() que vai
#       receber como parâmetro o ano de nascimento de uma pessoa,
#       retornando um valor literal indicando se uma pessoa tem voto NEGADO,
#       OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nascimento):
    from datetime import date
    ano = date.today().year - nascimento
    if 16 <= ano < 18 or ano > 70:
        return f'Com {ano} anos: voto facultativo'
    elif ano < 16:
        return f'Com {ano} anos: ainda não possui idade'
    else:
        return f'Com {ano} anos: voto obrigatório'


print(voto(int(input('Ano de nascimento: '))))
