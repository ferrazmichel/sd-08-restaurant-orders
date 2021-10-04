import csv
from collections import Counter


def csv_reader(path_to_file):
    data = []

    with open(path_to_file) as file:
        result = csv.reader(file, delimiter=',')
        for index in result:
            data.append(index)

    return data


def most_ordered(client, data):
    meals = []

    for index in data:
        if client in index:
            meals.append(index[1])

    count = Counter(meals)
    return count.most_common()[0][0]


def repeated_orders(client, order, data):
    result = 0

    for index in data:
        if index[0] == client and index[1] == order:
            result += 1
    return result


def never_ordered(client, data):
    client_orders = set()
    all_orders = set()

    for index in data:
        all_orders.add(index[1])
    for index in data:
        if index[0] == client:
            client_orders.add(index[1])
    return all_orders.difference(client_orders)


def without_orders(client, orders):
    ordered_days = set()
    days = set()

    for index in orders:
        days.add(index[2])
    for index in orders:
        if index[0] == client:
            ordered_days.add(index[2])
    return days.difference(ordered_days)


def analyze_log(path_to_file):

    data = csv_reader(path_to_file)

    message = (
        f"{most_ordered('maria', data)}\n"
        f"{repeated_orders('arnaldo', 'hamburguer', data)}\n"
        f"{never_ordered('joao', data)}\n"
        f"{without_orders('joao', data)}\n"
    )

    with open('data/mkt_campaign.txt', mode='w') as file:
        file.writelines(message)
