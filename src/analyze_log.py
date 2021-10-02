import csv


def most_ordered_meal(client, orders):
    food = {}

    for requested_food in orders:
        # print(requested_food)
        if client == requested_food['client']:
            if requested_food['order'] not in food:
                food[requested_food['order']] = 1
            else:
                food[requested_food['order']] += 1
    return max(food, key=food.get)


def how_many_times_burguer_was_ordered(client, orders):
    food = {}

    for requested_food in orders:
        if client == requested_food['client']:
            if requested_food['order'] not in food:
                food[requested_food['order']] = 1
            else:
                food[requested_food['order']] += 1
    return food['hamburguer']


def food_never_ordered(client, orders):
    order = set()
    all_orders = set()
    for requested_food in orders:
        all_orders.add(requested_food['order'])
    for requested_food in orders:
        if client == requested_food['client']:
            order.add(requested_food['order'])
    return all_orders - order


def never_went_to_diner(client, orders):
    date = set()
    all_date = set()
    for requested_food in orders:
        all_date.add(requested_food['day'])
    for requested_food in orders:
        if client == requested_food['client']:
            date.add(requested_food['day'])
    return all_date - date


def read_csv_file(path):
    data = []
    with open(path) as file:
        read = csv.reader(file, delimiter=',', quotechar='"')
        for row in read:
            client, order, day = row
            data.append(
                {'client': client, 'order': order, 'day': day}
            )

    return data


def write_file(content):
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(content)


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)

    maria = most_ordered_meal('maria', data)
    arnaldo = how_many_times_burguer_was_ordered('arnaldo', data)
    joao = food_never_ordered('joao', data)
    joao_never_went = never_went_to_diner('joao', data)

    converted_str = f"{maria}\n{arnaldo}\n{joao}\n{joao_never_went}\n"

    write_file(converted_str)
