import csv


def read_file(path):
    data = []
    with open(path) as arquivo:
        file = csv.reader(arquivo, delimiter=",")
        for row in file:
            customer, food, day = row
            data.append({"customer": customer, "food": food, "day": day})
    return data


def write_file(data):
    with open("data/mkt_campaign.txt", mode="w") as arquivo:
        arquivo.writelines(data)


def pedidos_maria(orders):
    data = {}
    for order in orders:
        if order["customer"] == "maria":
            if order["food"] not in data:
                data[order["food"]] = 1
            else:
                data[order["food"]] += 1
    return max(data, key = data.get)

def arnaldo_request(orders):
    contador = 0
    for order in orders:
        if order["customer"] == "arnaldo" and order["food"] == "hamburguer":
            contador += 1
    return contador


def joao_nunca_pediu(orders):
    pedidos = set()
    pedidos_joao = set()
    for order in orders:
        pedidos.add(order["food"])
        if order["customer"] == 'joao':
            pedidos_joao.add(order["food"])
    return pedidos - pedidos_joao

def dia_joao_nao_foi(orders):
    dias = set()
    dias_joao_foi = set()
    for order in orders:
        dias.add(order["day"])
        if order["customer"] == "joao":
            dias_joao_foi.add(order["day"])
    return dias - dias_joao_foi


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    maria_pedido = pedidos_maria(orders)
    arnaldo_pedido = arnaldo_request(orders)
    joao_nao_pediu = joao_nunca_pediu(orders)
    joao_nao_foi = dia_joao_nao_foi(orders)
    write_file(f"{maria_pedido}\n{arnaldo_pedido}\n{joao_nao_pediu}\n{joao_nao_foi}")
