import csv


def mais_pedido_maria(lista):
    listamaria = [item["pedido"] for item in lista if item["nome"] == "maria"]
    quantidade = dict()
    for pedido in listamaria:
        if pedido in quantidade:
            quantidade[pedido] = quantidade[pedido] + 1
        else:
            quantidade[pedido] = 1
    maior_pedido = max(quantidade, key=quantidade.get)
    return maior_pedido


def pedidos_arnaldo(lista):
    listaarnaldo = [
        item["pedido"] for item in lista if item["nome"] == "arnaldo"
    ]
    return listaarnaldo.count("hamburguer")


def pedidos_joao(lista):
    listatotal = set([item["pedido"] for item in lista])
    listajoao = set(
        [item["pedido"] for item in lista if item["nome"] == "joao"]
    )
    return listatotal.difference(listajoao)


def dias_joao(lista):
    listatotal = set([item["dia"] for item in lista])
    lista_joao = set([item["dia"] for item in lista if item["nome"] == "joao"])
    return listatotal.difference(lista_joao)


def analyze_log(path_to_file):
    txt_file_path = "data/mkt_campaign.txt"
    with open(path_to_file) as file:
        campos = ["nome", "pedido", "dia"]
        reader = csv.DictReader(file, fieldnames=campos)
        csv_data = [data for data in reader]
        maria = mais_pedido_maria(csv_data)
        arnaldo = pedidos_arnaldo(csv_data)
        joao_pedidos = pedidos_joao(csv_data)
        joao_dias = dias_joao(csv_data)
        with open(txt_file_path, mode="w") as text:
            text.write(
                f"{maria}\n"
                + f"{arnaldo}\n"
                + f"{joao_pedidos}\n"
                + f"{joao_dias}"
            )
