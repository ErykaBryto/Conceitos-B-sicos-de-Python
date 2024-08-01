'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
Lembrando que para o retorno vamos usar print com as variáveis
criadas e este texto é somente um exemplo, utilizem a criatividade.'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
profissao = input("Digite sua profissão: ")

print(f'Olá, {nome}! É um prazer conhecê-la. Vejo que você tem {idade} anos, é de {cidade} e trabalha como {profissao}. Espero que você tenha um ótimo dia!')