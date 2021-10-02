import csv
from collections import Counter


def analyze_log(path_to_file):

    with open(path_to_file) as csv_file:
        csv_reader = tuple(csv.reader(csv_file, delimiter=","))
    menu = set()
    dias = set()
    arnaldo_hamburguers = 0
    pratos_maria = []
    dias_joao = set()
    pedidos_joao = set()

    for item in csv_reader:
        dias.add(item[2])
        menu.add(item[1])
        if item[0] == "maria":
            pratos_maria.append(item[1])
        elif item[0] == "arnaldo" and item[1] == "hamburguer":
            arnaldo_hamburguers += 1
        elif item[0] == "joao":
            pedidos_joao.add(item[1])
            dias_joao.add(item[2])

    maria_dict = Counter(pratos_maria)

    maria_mais_pedido = max(maria_dict, key=maria_dict.get)
    vezes_arnaldo_pediu_hamb = arnaldo_hamburguers
    pratos_joao_nunca_pediu = set(menu) - set(pedidos_joao)
    dias_joao_nunca_foi = set(dias) - set(dias_joao)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f'{maria_mais_pedido}\n')
        file.write(f'{vezes_arnaldo_pediu_hamb}\n')
        file.write(f'{pratos_joao_nunca_pediu}\n')
        file.write(f'{dias_joao_nunca_foi}')
