'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

# Recebe o salário bruto do usuário
salario_bruto = float(input("Digite o salário bruto: R$ "))

# Define as faixas e as alíquotas
faixa1 = 1903.98
faixa2 = 2826.65
faixa3 = 3751.05
faixa4 = 4664.68

aliquota1 = 0
aliquota2 = 0.075
aliquota3 = 0.15
aliquota4 = 0.225
aliquota5 = 0.275

# Calcula o desconto do imposto de renda usando operações matemáticas e min
desconto_ir = (salario_bruto > faixa1) * min(salario_bruto, faixa2) * aliquota2 + \
              (salario_bruto > faixa2) * min(salario_bruto - faixa2, faixa3 - faixa2) * aliquota3 + \
              (salario_bruto > faixa3) * min(salario_bruto - faixa3, faixa4 - faixa3) * aliquota4 + \
              (salario_bruto > faixa4) * (salario_bruto - faixa4) * aliquota5

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto_ir

# Exibe os resultados
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IR: R$ {desconto_ir:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
