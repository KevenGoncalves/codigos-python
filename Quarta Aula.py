# Listas => ["Nome",19,True] => list
# Tuplas => ("Nome",19,True) => tuple
# Sets => {"Nome",19,True} => set
# Dicionarios => {"id": "Nome", "idade": 19,"valor":True} => dict

# set1 = {"Nome", 19, "True", 19}

# str -> int
# cast variavel de um tipo => outro tipo
# entrada = bool(input(""))  # False

# lista = dict(set1)
# print(lista)

def ler_media(divisao=3, outro_parametro=""):
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())

    media = (valor1 + valor2 + valor3) / divisao

    return media


def verficar_media(media):
    if media >= 14:
        return "Dispensado"
    elif media >= 9.5:
        return "Admitido"
    else:
        return "Excluido"


media = ler_media(4)
estado = verficar_media(media)
print(estado)


# 1 => Tempo Escrita
# 2 => Tempo de Compilação / Interpretação
# 3 => Tempo Execução

# valor = int("9")
