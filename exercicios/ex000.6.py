# 077 - Crie um programa que tenha uma tupla com várias palavras
#       (não usar acentos). Depois disso, você deve mostrar,
#       para cada palavra, quais são as suas vogais.

from random import randint

plv0 = ('imprescindível', 'condescendente', 'idiossincrasia',
        'característica', 'concupiscência', 'extraordinário',
        'demasiadamente', 'intercorrência', 'irrepreensível',
        'consubstanciar', 'pronta-entrega', 'incomensurável',
        'preponderância', 'arbitrariedade', 'discricionário',
        'especificidade', 'posteriormente', 'imprescritível',
        'intransponível', 'contextualizar', 'empreendimento',
        'ancestralidade', 'entretenimento', 'transcendental',
        'infraestrutura', 'paulatinamente', 'revolucionário',
        'relacionamento', 'superveniência', 'arrependimento',
        'bem-aventurado', 'atenciosamente', 'imparcialidade',
        'periodicamente', 'ponto de vista', 'transcendência',
        'reconhecimento', 'democratização', 'insignificante',
        'diligentemente', 'inconsistência', 'personificação',
        'despretensioso', 'impessoalidade', 'socioambiental',
        'espontaneidade', 'cônjuge virago', 'intransigência',
        'aplicabilidade', 'funcionalidade', 'desprendimento',
        'trazer à baila', 'procrastinador', 'potencialidade',
        'principalmente', 'procrastinação', 'estratificação',
        'licenciosidade', 'excentricidade', 'prestatividade',
        'estelionatário', 'congratulações', 'inconveniência',
        'pusilanimidade', 'extraordinária', 'dissolutamente',
        'exequibilidade', 'insubstituível', 'epistemológico',
        'individualismo', 'resplandecente', 'biodiversidade',
        'coercitividade', 'abundantemente', 'jurisprudência',
        'plausibilidade', 'credenciamento', 'disponibilizar',
        'internalização', 'acessibilidade', 'constantemente',
        'exclusivamente', 'multiplicidade', 'aleatoriamente',
        'perfeccionista', 'implicitamente', 'impressionante',
        'questionamento', 'menção honrosa', 'papibaquígrafo',
        'grandiloquente', 'esclarecimento', 'minuciosamente',
        'intermunicipal', 'indiscriminado', 'frequentemente',
        'permissividade', 'sobrecarregado', 'concessionária')

vga = ('a', 'á', 'à', 'â', 'ã',
       'e', 'é', 'ê', 'i', 'í',
       'o', 'ô', 'õ', 'u', 'ú')

# título
ini = str('APRENDENDO ')
tit = str('VOGAIS')
cor = 31
p = ''

for let in tit:
        p += f'\033[{cor}m{let}\033[m'
        cor += 1
        if cor == 37:
                cor = 31
ini += p

print('-' * 41)
print(f'{" " * 12}{ini}')
print('-' * 41)

# vogais

for palavra in plv0:
        if palavra == plv0[0]:
                print(f'\nVogais em \033[1m{palavra.upper()}\033[m: ', end='')
        else:
                print(f'\nVogais em \033[1m{palavra.upper()}\033[m: ', end='')
        cor = randint(31, 36)
        for letra in palavra:
                if letra.lower() in vga:
                        print(f'\033[{cor}m{letra}\033[m', end=' ')
                        cor += 1
                        if cor == 37:
                                cor = 31
