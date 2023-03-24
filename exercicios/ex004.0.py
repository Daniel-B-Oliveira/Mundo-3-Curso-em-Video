'''
def lin():
    print('-='*15)


# Programa Principal

lin()
print('TESTE 1')
lin()
print('TESTE 2')
lin()
print('TESTE 3')
lin()
print('TESTE 5')
lin()
'''
#       /           /           /           /           /

'''
def mensagem(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


mensagem('SISTEMA DE ALUNOS')
'''

'''
def soma(a, b):  # a e b são parametros
    s = a+b
    print(s)


soma(b=3, a=5)
'''

'''
def contador(*num):
    print(num)  # Cria uma tupla
    print(len(num))


contador(1,2,3,4,5,6)
'''


def dobra(lst):
    for pos in range(len(lst)):
        lst[pos] *= 2


val = [1, 3, 5]

dobra(val)
print(val)
