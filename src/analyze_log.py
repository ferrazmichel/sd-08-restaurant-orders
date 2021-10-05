import csv


def read_csv(path_to_file):
    data = []
    with open(path_to_file, "r") as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        for row in file_content:
            client, meal, date = row
            data.append(
                {'client': client, 'meal': meal, 'date': date}
            )
    return data


def most_ordered(customer, orders):
    count = {}
    most_ordered = ''
    count[most_ordered] = 0
    for order in orders:
        if customer == order['client']:
            if order['meal'] not in count:
                count[order['meal']] = 1
            else:
                count[order['meal']] += 1
            if count[order['meal']] > count[most_ordered]:
                most_ordered = order['meal']

    return most_ordered


def count_order(customer, meal_selected, orders):
    count = 0
    for order in orders:
        if customer == order['client'] and meal_selected == order['meal']:
            count += 1
    return count


def never_ordered(customer, orders):
    all_orders = set()
    for order in orders:
        all_orders.add(order['meal'])
    customer_order = set()
    for order in orders:
        if customer == order['client']:
            customer_order.add(order['meal'])
    return all_orders - customer_order


def days_without_client(customer, orders):
    days_of_week = set()
    for order in orders:
        days_of_week.add(order['date'])
    customer_set = set()
    for order in orders:
        if customer == order['client']:
            customer_set.add(order['date'])
    return days_of_week - customer_set


def analyze_log(path_to_file):
    result = ''
    data = read_csv(path_to_file)
    most_requested_by_Maria = most_ordered("maria", data)
    arnaldo_count = count_order("arnaldo", "hamburguer", data)
    joao_never_ordered = never_ordered("joao", data)
    days_without_joao = days_without_client("joao", data)
    result = (
        f"{most_requested_by_Maria}\n"
        f"{arnaldo_count}\n"
        f"{joao_never_ordered}\n"
        f"{days_without_joao}"
    )
    with open("data/mkt_campaign.txt", "w") as f:
        f.write(result)
