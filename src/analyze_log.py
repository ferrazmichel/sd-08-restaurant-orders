import csv
from collections import Counter


def analyze_log(path_to_file):
    """Commit inicial do projeto"""
    customer_dict = {}
    menu = set()
    week = set()
    with open(path_to_file) as file:
        orders = csv.reader(file, delimiter=",", quotechar='"')
        for order in orders:
            menu.add(order[1])
            week.add(order[2])
            if order[0] not in customer_dict:
                customer_dict[order[0]] = [(order[1], order[2])]
            else:
                customer_dict[order[0]].append((order[1], order[2]))

    maria_orders = []
    for order in customer_dict["maria"]:
        maria_orders.append(order[0])
    maria_most_ordered = Counter(maria_orders).most_common()[0][0]

    arnaldo_hamburgers = 0
    for order in customer_dict["arnaldo"]:
        if order[0] == "hamburguer":
            arnaldo_hamburgers += 1

    joao_dishes = set()
    joao_frequency = set()
    for order in customer_dict["joao"]:
        joao_dishes.add(order[0])
        joao_frequency.add(order[1])

    never_ordered_by_joao = menu.difference(joao_dishes)
    joao_is_hungry_in = week.difference(joao_frequency)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(
            f"{str(maria_most_ordered)}\n{str(arnaldo_hamburgers)}\n"
            f"{str(never_ordered_by_joao)}\n{str(joao_is_hungry_in)}"
        )
