'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite sua altura em metro: "))

imc = peso / (altura*altura)

print(f'Seu Índice de Massa Corporal (IMC) é de: {imc:.2f}')