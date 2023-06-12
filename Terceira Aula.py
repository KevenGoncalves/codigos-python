# listas, tuplas e dicionarios

listas = ["Keven", "Luis"]
len(listas)


tupla = ("Keven", "Mais")
# tupla = "Portugues",


dictionarios = {
    "nome": "Keven",
    "idade": 19
}


# estudante = [
#         ("Keven", 19),
#         (19, "Luis")
# ]

estudantes = [
        {
            "nome": "Keven",
            "idade": 19
        },
        {
            "nome": "Luis",
            "idade": 20,
        }
]

# print(estudantes)

# for est in estudantes:
#     print(est['nome'].lower())


# print(listas[0])
# print(dictionarios.values())

# for i in dictionarios.values():
#     print(i)

perguntas = [
        {
            "pergunta": "qual é o animal",
            "resposta1": "A",
            "resposta2": "B",
            "resposta3": "C",
            "resposta4": "D",
            "resposta_certa": "A",
            "acertou": False
            },
        {
            "pergunta": "qual é o animal",
            "resposta1": "A",
            "resposta2": "B",
            "resposta3": "C",
            "resposta4": "D",
            "resposta_certa": "A",
            "acertou": False
            },
        ]

soma = 0
for pergunta in perguntas:
    print(f"""
{pergunta['pergunta']}
{pergunta['resposta1']}
{pergunta['resposta2']}
{pergunta['resposta3']}
{pergunta['resposta4']}
          """)

    valor = input()

    if valor == pergunta['resposta_certa']:
        pergunta['acertou'] = True
        soma += 4

print(soma)

for pergunta in perguntas:
    if not pergunta['acertou']:
        print(f"Respota errada a respota ceerta seria {pergunta['resposta_certa']}")
