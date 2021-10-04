import csv


def read_file(path):
    data = []
    with open(path) as file:
        files = csv.reader(file, delimiter=",")
        for row in files:
            customer, food, day = row
            data.append({"customer": customer, "food": food, "day": day})
    return data


def write_file(data):
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(data)


def most_requested_dish_by_maria(orders):
    dish = {}
    for order in orders:
        if order["customer"] == "maria":
            if order["food"] not in dish:
                dish[order["food"]] = 1
            else:
                dish[order["food"]] += 1
    return max(dish, key=dish.get)


def how_many_times_does_arnaldo_order_hamburger(orders):
    counter = 0
    for order in orders:
        if order["customer"] == "arnaldo" and order["food"] == "hamburguer":
            counter = +1
    return counter


def dishes_that_joao_never_ordered(orders):
    all_orders = set()
    joao_orders = set()
    for order in orders:
        all_orders.add(order["food"])
        if order["customer"] == "joao":
            joao_orders.add(order["food"])
    return all_orders.difference(joao_orders)


def joao_days_without_order(orders):
    days = set()
    joao_days_with_order = set()
    for order in orders:
        days.add(order["day"])
        if order["customer"] == "joao":
            joao_days_with_order.add(order["day"])
    return days.difference(joao_days_with_order)


def analyze_log(path_to_file):
    orders = read_file(path_to_file)

    maria = most_requested_dish_by_maria(orders)
    arnaldo = how_many_times_does_arnaldo_order_hamburger(orders)
    joao_never_order = dishes_that_joao_never_ordered(orders)
    joao_without_order = joao_days_without_order(orders)
    data = f"{maria}\n{arnaldo}\n{joao_never_order}\n{joao_without_order}"

    write_file(data)
