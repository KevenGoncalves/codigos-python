# Resolução de Exercicios
# 1-
media = 15

if media > 9:
    print(f" { '%.4f' % media } Passou")
elif media > 14:
    print("Dispensou")
else:
    print("Excluido")

# Qual seria o output (saida): Passou

# 2 -


def eBissesto(a: int):
    if (((a % 4 == 0) and (a % 100 != 0)) or a % 400 == 0):
        return True
    return False

# def eBissesto(a: int):
#     return (((a % 4 == 0) and (a % 100 != 0)) or a % 400 == 0)


# ano = int(input('digita o ano'))
# print(f'{ano} é bissesto? { eBissesto(ano)}')

# \n => newline ( novalinha)
# \t => tab (tabelação) 4 espaços
# \s => space (space)
# valor = input("Digite o numero\n")
# resultado = 0
# numero1 = 0
# numero2 = 0

# if valor == "+":
#     resultado = numero1 + numero2
# elif valor == "/":
#     resultado = numero1 * numero2
# elif valor == "*":
#     resultado = numero1 / numero2

# print(resultado)
