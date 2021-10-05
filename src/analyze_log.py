import csv


def read_csv_file(path):
    data = []
    with open(path) as file:
        read = csv.reader(file, delimiter=',', quotechar='"')
        for row in read:
            costumer, order, day = row
            data.append(
                {'costumer': costumer, 'order': order, 'day': day}
            )

    return data


def most_popular(client, orders):
    food = {}

    for order in orders:
        if client == order['costumer']:
            if order['order'] not in food:
                food[order['order']] = 1
            else:
                food[order['order']] += 1
    return max(food, key=food.get)


def number_of_orders(client, orders):
    food = {}

    for order in orders:
        if client == order['costumer']:
            if order['order'] not in food:
                food[order['order']] = 1
            else:
                food[order['order']] += 1
    return food['hamburguer']


def never_ordered(client, orders):
    order_set = set()
    all_orders = set()
    for order in orders:
        all_orders.add(order['order'])
    for order in orders:
        if client == order['costumer']:
            order_set.add(order['order'])
    return all_orders - order_set


def never_have_been(client, orders):
    date = set()
    all_date = set()
    for order in orders:
        all_date.add(order['day'])
    for order in orders:
        if client == order['costumer']:
            date.add(order['day'])
    return all_date - date


def write_file(content):
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(content)


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)
    most_ordered = most_popular('maria', data)
    number_of_order = number_of_orders('arnaldo', data)
    never = never_ordered('joao', data)
    never_went = never_have_been('joao', data)
    content = f"{most_ordered}\n{number_of_order}\n{never}\n{never_went}\n"
    write_file(content)