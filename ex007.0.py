try:
    a = int(input('Digite um número'))
    b = int(input('Digite o divisor'))

    r = a / b

except (ValueError, TypeError):
    print('Obtivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível divisão por zero')

except KeyboardInterrupt:
    print('Valor vazio')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Obrigado pela atenção, volte sempre.')
