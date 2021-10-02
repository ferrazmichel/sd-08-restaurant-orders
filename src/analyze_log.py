import csv


def read_csv(path):
    content = []
    with open(path, "r") as file:
        file_content = csv.reader(file, delimiter=",", quotechar='"')
        for row in file_content:
            client, meal, date = row
            content.append(
                {'client': client, 'meal': meal, 'date': date}
            )

    return content


def common_order(customer, orders):
    count = {}
    most_frequent = 'teste'
    count[most_frequent] = 0
    for order in orders:
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


def never_ordered(customer, orders):
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
    content_file = read_csv(path_to_file)
    most_frequent = common_order('maria', content_file)
    number_of_order = count_order('arnaldo', 'hamburguer', content_file)
    unordered_meal = never_ordered('joao', content_file)
    date = never_date('joao', content_file)
    content = f'{most_frequent}\n{number_of_order}\n{unordered_meal}\n{date}'
    write_file(content)
    # raise NotImplementedError
