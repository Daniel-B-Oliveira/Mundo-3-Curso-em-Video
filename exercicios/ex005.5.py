# 105 - Faça um programa que tenha uma função notas() que pode receber
#       várias notas de alunos e vai retornar um dicionário com
#       as seguintes informações:
#           – Quantidade de notas
#           – A maior nota
#           – A menor nota
#           – A média da turma
#           – A situação (opcional)

def notas(*nt, sit=False):
    """
    :param nt: Nota dos alunos
    :param sit: (Opcional) Situação da média da classe média >= 7 boa, 5 >= média < 7 regular, média < 5 ruim
    :return: nota.dict()
    """
    nota = dict()
    ct = 1
    for c in nt:
        nota[f'Nota {ct}'] = c
        ct += 1
    nota['Total'] = len(nt)
    nota['Maior'] = max(nt)
    nota['Menor'] = min(nt)
    nota['Média'] = str(f'{sum(nt)/len(nt):.2f}')

    if sit:
        if float(nota['Média']) >= 7.0:
            nota['Situação'] = 'Boa'
        elif float(nota['Média']) < 5.0:
            nota['Situação'] = 'Ruim'
        else:
            nota['Situação'] = 'Regular'

    return nota

print(notas(1,2,33,2,2,1))
