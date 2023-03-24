from ex0065.utilidades import moeda
from ex0065.utilidades import dado

valor = dado.leiadinheiro('Digite um valor: ')
taxa = float(input('Digite a porcentagem do aumento: '))

moeda.remumo(valor, taxa, taxa)
