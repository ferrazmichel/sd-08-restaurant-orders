import csv
from collections import Counter


def get_orders(path):
    array_of_orders = []
    with open(path) as data:
        orders = csv.reader(data, delimiter=",")
        for order in orders:
            array_of_orders.append(order)
    return array_of_orders


def write_in_file(all_data):
    path = "data/mkt_campaign.txt"
    with open(path, 'a') as mkt_campaign:
        for data in all_data:
            mkt_campaign.write(str(data) + "\n")


# ref: https://pythonguides.com/python-counter/
def get_most_requested_dish_by_maria(all_orders):
    """Retorna o prato mais pedido por maria"""
    dishes_ordered_by_maria = [order[1] for order in all_orders]
    dishes_counter = Counter(dishes_ordered_by_maria)
    ordered_dishes_list = list(dishes_counter.items())
    ordered_dishes_list = sorted(ordered_dishes_list, key=lambda dish: dish[1])
    return ordered_dishes_list[-1][0]


def count_arnaldos_hamburger_orders(all_orders):
    """Conta a quantidade de hambúgueres pedidos por arnaldo"""
    hamburgers_counter = 0
    for order in all_orders:
        if order[0] == "arnaldo" and order[1] == "hamburguer":
            hamburgers_counter += 1
    return hamburgers_counter


def get_dishes_that_joao_never_ate(all_orders):
    all_dishes = set()
    dishes_that_joao_ate = set()
    for order in all_orders:
        all_dishes.add(order[1])
        if order[0] == "joao":
            dishes_that_joao_ate.add(order[1])
    return all_dishes - dishes_that_joao_ate


def get_days_that_joao_didnt_go_to_the_cafeteria(all_orders):
    all_days = {
        "domingo",
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sabado"}
    days_that_joao_went_to_the_cafeteria = set()

    for order in all_orders:
        if order[0] == "joao":
            days_that_joao_went_to_the_cafeteria.add(order[2])
    return all_days - days_that_joao_went_to_the_cafeteria


def analyze_log(path_to_file):
    """Analiza os dados no log"""
    orders = get_orders(path_to_file)
    data = []

    data.append(get_most_requested_dish_by_maria(orders))
    data.append(count_arnaldos_hamburger_orders(orders))
    data.append(get_dishes_that_joao_never_ate(orders))
    data.append(get_days_that_joao_didnt_go_to_the_cafeteria(orders))

    write_in_file(data)

    # print(get_most_requested_dish_by_maria(orders))
    # print(count_arnaldos_hamburger_orders(orders))
    # print(get_dishes_that_joao_never_ate(orders))
    # print(get_days_that_joao_didnt_go_to_the_cafeteria(orders))
    # raise NotImplementedError
