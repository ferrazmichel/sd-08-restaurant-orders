import csv


def read_file_csv(path):
    content = []
    with open(path, "r") as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        for row in file_content:
            client, meal, date = row
            content.append(
                {'client': client, 'meal': meal, 'date': date}
            )
    return content


def most_ordered_meal(customer, orders):
    count = {}
    most_frequent = 'teste'
    count[most_frequent] = 0
    for order in orders:
        print(order['meal'])
        if customer == order['client']:
            if order['meal'] not in count:
                count[order['meal']] = 1
            else:
                count[order['meal']] += 1
            if count[order['meal']] > count[most_frequent]:
                most_frequent = order['meal']

    return most_frequent


def count_order(customer, meal, orders):
    count = 0
    for order in orders:
        if customer == order['client'] and meal == order['meal']:
            count += 1
    return count


def food_never_ordered(customer, orders):
    meals_set = set()
    for order in orders:
        meals_set.add(order['meal'])

    customer_set = set()
    for order in orders:
        if customer == order['client']:
            customer_set.add(order['meal'])

    return meals_set - customer_set


def write_file(content):
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines(content)


def never_date(customer, orders):
    dates_set = set()
    for order in orders:
        dates_set.add(order['date'])
    customer_set = set()
    for order in orders:
        if customer == order['client']:
            customer_set.add(order['date'])
    return dates_set - customer_set


def analyze_log(path_to_file):
    file_content = read_file_csv(path_to_file)
    maria_order = most_ordered_meal('maria', file_content)
    arnaldo_order = count_order('arnaldo', 'hamburguer', file_content)
    joao_not_ordered = food_never_ordered('joao', file_content)
    joao_date = never_date('joao', file_content)
    file = f"{maria_order}\n{arnaldo_order}\n{joao_not_ordered}\n{joao_date}"
    write_file(file)
