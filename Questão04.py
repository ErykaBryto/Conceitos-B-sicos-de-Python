'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''
combustivel = float(input ("Informe a quantidade de litros de combustível consumidos: "))
distancia = float (input('Informe a distâcia percorrida em quilômetros: '))

consumo = distancia/combustivel
print(f'o consumo medio é {consumo:.2f} por Km/l: ')