import csv
from collections import Counter
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://docs.python.org/pt-br/3/library/collections.html#counter-objects


def get_most_ordered_dish_per_costumer(file, name):
    orders = []
    for item in file:
        if item[0] == name:
            orders.append(item[1])
    count = Counter(orders)
    count_max = max(count.values())
    for k, v in count.items():
        if v == count_max:
            dish = k
    return dish


def get_dish_per_costumer(file, name, food):
    orders = []
    count = 0
    for item in file:
        if item[0] == name:
            orders.append(item[1])
    for dish in orders:
        if dish == food:
            count += 1
    return count


def get_never_ordered_per_costumer(file, name):
    orders = []
    foods = {'hamburguer', 'pizza', 'coxinha', 'misto-quente'}
    for item in file:
        if item[0] == name:
            orders.append(item[1])
    orders = set(orders)
    foods = foods.difference(orders)
    return foods


def get_days_never_visited_per_costumer(file, name):
    orders = set()
    days = {"segunda-feira", "terça-feira", "sabado"}
    for item in file:
        if item[0] == name:
            orders.add(item[2])
    days = days.difference(orders)
    return days


def analyze_log(path_to_file):
    output_file = "data/mkt_campaign.txt"
    orders = []
    with open(path_to_file, mode='r') as read_file:
        result = csv.reader(read_file, delimiter=",")
        for row in result:
            orders.append(row)
    with open(output_file, mode='w') as write_file:
        print(
            get_most_ordered_dish_per_costumer(orders, "maria"),
            get_dish_per_costumer(orders, "arnaldo", "hamburguer"),
            get_never_ordered_per_costumer(orders, "joao"),
            get_days_never_visited_per_costumer(orders, "joao"),
            sep="\n", file=write_file
            )

# Plantão Gleison e Bux em 29/07 13:00
