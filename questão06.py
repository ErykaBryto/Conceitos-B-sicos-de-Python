'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

distancia = float(input("Digite a distância da viagem em km: "))

tempo_onibus = (distancia/80)
tempo_carro = (distancia/100)
tempo_aviao = (distancia/600)
print(f'O tempo gasto de viagem de avião é {tempo_aviao:.2f} horas, o tempo gasto de carro é {tempo_carro:.2f} horas e o tempo gasto de ônibus é {tempo_onibus:.2f} horas')