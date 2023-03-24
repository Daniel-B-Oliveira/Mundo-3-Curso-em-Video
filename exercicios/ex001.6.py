# 083 - Crie um programa onde o usuário digite uma expressão qualquer
#       que use parênteses. Seu aplicativo deverá analisar se a expressão
#       passada está com os parênteses abertos e fechados na ordem correta.

op = str(input('Digite a expreção:\n'))
print(f'\nEXPRESSÃO: {op}')

# Solução maior e menor

a = op.count('(')
b = op.count(')')

if a == b:
    print('\n\033[32mA operação está correta.\033[m')
elif a < b:
    print('\n\033[31mA operação está errada.Existem parenteses que não foram abertos.\033[m')
elif a > b:
    print('\n\033[31mA operação está errada.Existem parenteses que não foram fechados.\033[m')

# Solução Curso em Video, utilizando os conceitos da aula 17

print('')

pilha = list()

for simb in op:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32mExpreção Válida.\033[m')
else:
    print('\033[31mExpressão Inválida.\033[m')
