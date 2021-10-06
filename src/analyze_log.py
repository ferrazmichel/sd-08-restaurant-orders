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
    meals_count = {}
    the_most = ""

    orders_by_custumer = filter(lambda o: o['client'] == customer, orders)

    for order in orders_by_custumer:
        actual_meal = order['meal']
        if actual_meal not in meals_count:
            meals_count[actual_meal] = 1
        else:
            meals_count[actual_meal] += 1
        if the_most == "" or meals_count[actual_meal] > meals_count[the_most]:
            the_most = actual_meal

    return the_most


def count_order(customer, meal, orders):
    orders_filtered = list(filter(lambda o: o['client'] == customer
                                  and o['meal'] == meal, orders))
    return len(orders_filtered)


def food_never_ordered(customer, orders):
    meals_unique = set()
    for order in orders:
        meals_unique.add(order['meal'])

    meals_unique_by_customer = set()
    orders_by_custumer = filter(lambda o: o['client'] == customer, orders)
    for order in orders_by_custumer:
        meals_unique_by_customer.add(order['meal'])

    return meals_unique - meals_unique_by_customer


def write_file(content):
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines(content)


def never_date(customer, orders):
    dates_set = set()
    for order in orders:
        dates_set.add(order['date'])

    customer_set = set()
    orders_by_custumer = filter(lambda o: o['client'] == customer, orders)
    for order in orders_by_custumer:
        customer_set.add(order['date'])

    return dates_set - customer_set


def analyze_log(path_to_file):
    orders_history = read_file_csv(path_to_file)
    most_order = most_ordered_meal('maria', orders_history)
    count_ordered = count_order('arnaldo', 'hamburguer', orders_history)
    meal_not_ordered = food_never_ordered('joao', orders_history)
    no_order_day = never_date('joao', orders_history)
    file = f"{most_order}\n{count_ordered}\n{meal_not_ordered}\n{no_order_day}"
    write_file(file)
