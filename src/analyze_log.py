import csv
from collections import Counter


def analyze_log(path_to_file):
    # if not path_to_file.endswith(".csv") or
    # not path_to_file.endswith(".csv") or path_to_file == "":
    # raise FileNotFoundError

    # raise NotImplementedError
    # Qual o prato mais pedido por 'maria'?
    # maria está na primeira posição

    with open(path_to_file) as csv_file:
        csv_reader = tuple(csv.reader(csv_file, delimiter=","))
        # print(csv_reader[0][0])
    menu = set()
    joao_orders = set()
    joao_days = set()
    work_days = set()
    count_maria_food = []
    arnaldo_hamburguers = 0
    for item in csv_reader:
        work_days.add(item[2])
        menu.add(item[1])
        # menu = list(dict.fromkeys(menu))
        # https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        # Create a dictionary, using the List items as keys. This will
        # automatically remove any duplicates because dictionaries cannot
        # have duplicate keys.
        # work_days = list(dict.fromkeys(work_days))
        if item[0] == "maria":
            count_maria_food.append(item[1])
        elif item[0] == "arnaldo" and item[1] == "hamburguer":
            arnaldo_hamburguers += 1
        elif item[0] == "joao":
            joao_orders.add(item[1])
            joao_days.add(item[2])
        maria_dict = Counter(count_maria_food)

    # refazer usar Counter
    # https://www.ti-enxame.com/pt/python/encontrar-o-maior-valor-em-um-dicionario/1069289117/
    # print(f"Prato mais pedido por Maria
    # {max(maria_dict, key=maria_dict.get)}")
    # print(f"Arnaldo Burger {arnaldo_hamburguers}")
    # print(f"joao nunca pediu {set(menu) - set(joao_orders)}")
    # print(f"joao_orders {joao_orders}")
    # print(f"menu {menu}")
    # print(f"joao_days {joao_days}")
    # print(f"joao nao vai a lanchonete {set(work_days) - set(joao_days)}")
    maria_more_ordered = max(maria_dict, key=maria_dict.get)
    arnaldo_burguer = arnaldo_hamburguers
    joao_never_asked = set(menu) - set(joao_orders)
    joao_never_go = set(work_days) - set(joao_days)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f'{maria_more_ordered}\n')
        file.write(f'{arnaldo_burguer}\n')
        file.write(f'{joao_never_asked}\n')
        file.write(f'{joao_never_go}')
