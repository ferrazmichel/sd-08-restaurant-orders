from os import path
import csv


def favorite_dish(name, orders):
    favorite_dish = ""
    for row in orders:
        if row[0] == name:
            favorite_dish = row[1]
            break
    return favorite_dish


def repeated_dishes(name, dish, orders):
    client_order = set()
    for row in orders:
        if row[0] == name and row[1] == dish:
            client_order.add(row[1])
    return len(client_order)


def dishes_never_ordered(name, orders):
    client_order = set()
    all_orders = set()
    for order_row in orders:
        all_orders.add(order_row[1])
    for client_row in orders:
        if client_row[0] == name:
            client_order.add(client_row[1])
    return all_orders.difference(client_order)


def days_never_gone(name, days):
    days_never_gone = set()
    all_days = set()
    for day_row in days:
        all_days.add(day_row[2])
    for day_row in days:
        if day_row[0] == name:
            days_never_gone.add(day_row[2])
    return all_days.difference(days_never_gone)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        orders = list(csv_reader)
    clients_array = ["maria", "joao", "arnaldo", "hamburguer"]
    with open("data/mkt_campaign.txt", "w") as save_file:
        save_file.write(f"{favorite_dish(clients_array[0], orders)}\n")
        save_file.write(
            f"{repeated_dishes(clients_array[2], clients_array[3], orders)}\n"
        )
        save_file.write(f"{dishes_never_ordered(clients_array[1], orders)}\n")
        save_file.write(f"{days_never_gone(clients_array[1], orders)}\n")
