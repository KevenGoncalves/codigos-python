print("\n Leia atentamente \n")

valorTotal = 0
pergunta1 = False
pergunta2 = False
pergunta3 = False
pergunta4 = False
pergunta5 = False

opcao1 = input("""
Qual é a resposta correta a, b ou c
a) maça
b) banana
c) alface
d) tomate
""")

if opcao1 == 'C':
    pergunta1 = True
    valorTotal += 4


opcao2 = input("Qual é a resposta correta a, b ou c")

if opcao2 == 'D':
    pergunta2 = True
    valorTotal += 4


if not pergunta1:
    print('A pergunta 1 está Errada Correto seria C')

if not pergunta2:
    print('A pergunta 2 está Errada Correto seria D')

print(f'O valor é {valorTotal}')
