import csv

def most_requested_plate(customer, orders):
    meals = {}
    for order in orders:
        if customer in order:
            if order[1] not in meals:
                meals[order[1]] = 1
            else:
                meals[order[1]] += 1

    return max(meals, key=meals.get)


def repeated_plates(customer, plate, orders):
    client_order = set()
    for order in orders:
        if order[0] == customer and order[1] == plate:
            client_order.add(order[1])
    return len(client_order)


def never_ordered_plate(customer, orders):
    order_client = set()
    all_orders = set()
    for order in orders:
        all_orders.add(order[1])
    for order in orders:
        if order[0] == customer:
            order_client.add(order[1])
    return all_orders.difference(order_client)


def days_without_orders(customer, orders):
    days_with_orders = set()
    days = set()
    for order in orders:
        days.add(order[2])
    for order in orders:
        if order[0] == customer:
            days_with_orders.add(order[2])
    return days.difference(days_with_orders)


def open_csv(path):
    fileData = []

    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            fileData.append(row)

    return fileData


def write_file(str):
    with open('data/mkt_campaign.txt', mode='w') as file:
        file.writelines(str)
        

def analyze_log(path):
    fileData = []

    fileData = open_csv(path)

    str = "{0}\n{1}\n{2}\n{3}".format(
        most_requested_plate('maria', fileData),
        repeated_plates('arnaldo', 'hamburguer', fileData),
        never_ordered_plate('joao', fileData),
        days_without_orders('joao', fileData)
    )

    write_file(str)
    
