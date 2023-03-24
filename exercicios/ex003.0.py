'''filme0 = {'titulo': 'Star Wars',
          'ano': 1997,
          'diretor': 'George Lucas'}

print(filme0.values()) # dict_values(['Star Wars', 1997, 'George Lucas'])
print(filme0.keys())  # dict_keys(['titulo', 'ano', 'diretor'])
print(filme0.items())  # dict_items([('titulo', 'Star Wars'), ('ano', 1997), ('diretor', 'George Lucas')])

for k, v in filme0.items():  # K: keys, V: Values
    print(f'O {k} é {v}')'''

#       /           /           /           /           /           /           /
'''
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'singla': 'SP'}

brasil.append(estado1)

brasil.append(estado2)

for c in range(0, len(brasil)):
    print(brasil[c]['UF'])
'''

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Silga do Estado: '))
    brasil.append(estado.copy())  # copy para copiar em vez de [:]

for e in brasil:  # for para  a lista
    for v in e.values():  # Para dicionário
        print(v, end=' ')
    print()


print(brasil)