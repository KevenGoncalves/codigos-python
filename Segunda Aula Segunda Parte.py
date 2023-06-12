valor = 0

# for passo in range(5):
#     if (passo == 2):
#         break
#     print(f"{passo} Olá Keven")
#     valor += 2

# print(valor)

# TODO: Mostrar motivo da diferença de for e while

# range(10) => range(0,10,1)
# range(2,20) => range(2,10,1)
# range(2,20,4)

# valorA = 0
# contador = 0

# while contador > 10:
#     print(f"{contador+1} Olá Keven")
#     # valorA += 2
#     contador += 1
# else:
#     print("Fim de Tudo")

# continue
# break

# while True:
#     x = input()

#     if x == "Sim":
#         break


# lista = ["Keven", "Luis", "Vanessa", 19, 32, True, 102, 23, "Keven"]
# print(lista)
# lista[2] = "Gonçalves"

# # print(len(lista))
# for valor in range(len(lista)):
#     print(lista[valor])

# for valorDentro in lista:
#     print(valorDentro)

for i in range(10):
    for j in range(5):
        print(f"{i}=> {j}:Olá")

lista = [
        ["Keven", 19, "Estudante"],
        ["Luis", 18, "Estudante"]
]

for i in range(len(lista)):
    for j in range(len(lista[1])):
        print(f"{i}=> {j}:Olá")

for cadalista in lista:
    for j in cadalista:
        print(f"{j}:Olá")
