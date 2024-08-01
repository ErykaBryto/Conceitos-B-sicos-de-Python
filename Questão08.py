'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês.'''

ganho_hora = float(input('Quanto você ganha por hora trabalhada? '))
hora_mes = float(input('Quantas horas você trabalha por mês? '))

salario = ganho_hora * hora_mes

print(f'Seu salário nesse mes foi de: {salario:.2f}')