import csv
from statistics import mode


def analyze_log(path_to_file):
    nome, pedido, dia = get_dados(path_to_file)

    maria = []
    for valor in nome["maria"]:
        maria.append(valor[0])
    maria_maior = mode(maria)

    arnaldo = 0
    for valor in nome["arnaldo"]:
        if valor[0] == "hamburguer":
            arnaldo += 1

    joao_pediu = set()
    joao_dia = set()
    for valor in nome["joao"]:
        joao_pediu.add(valor[0])
        joao_dia.add(valor[1])

    string = (f"{maria_maior}\n{arnaldo}\n"
              f"{joao_pediu.symmetric_difference(pedido)}\n"
              f"{joao_dia.symmetric_difference(dia)}")

    file = open("data/mkt_campaign.txt", mode="w")
    file.write(string)
    file.close


def get_dados(path_to_file):
    nome = {}
    pedido = set()
    dia = set()

    with open(path_to_file, "r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        for valor in data:
            pedido.add(valor[1])
            dia.add(valor[2])
            if valor[0] not in nome:
                nome[valor[0]] = [(valor[1], valor[2])]
            else:
                nome[valor[0]].append((valor[1], valor[2]))

    return (nome, pedido, dia)
