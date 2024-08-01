'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

horas_exercicio = float(input("Digite a quantidade de horas que se exercita por semana: "))

calorias_mes= ((horas_exercicio * 60)*4)*5

print(f"O total de calorias queimadas em um mês é: {calorias_mes:.2f} calorias")