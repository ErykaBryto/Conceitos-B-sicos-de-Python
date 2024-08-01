'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

quilometro = int(input ("Informe a quantidade de quilometros: "))
metro = 1000 * quilometro
centimetro = 100000 * quilometro
milimetro = 1000000 * quilometro
print(f'Fazendo a conversão temos: {metro} metros, {centimetro} centímetros e {milimetro} milímetros')