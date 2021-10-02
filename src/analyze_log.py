import csv


def more_request_by_Maria(orders_list):
    count = {}
    most_frequent = orders_list[0]["Comida"]

    for order in orders_list:
        name, food = (order["Nome"], order["Comida"])
        if name == "maria":
            if food not in count:
                count[food] = 1
            else:
                count[food] += 1
                if count[food] > count[most_frequent]:
                    most_frequent = food
    return most_frequent


def count_hamburger_for_arnaldo(orders_list):
    count = {'Hanburger': 0}
    for order in orders_list:
        name, food = (order["Nome"], order["Comida"])
        if name == 'arnaldo' and food == 'hamburguer':
            count['Hanburger'] += 1
    return count['Hanburger']


def Joao_never_request(orders_list):
    set_foods = {order["Comida"] for order in orders_list}
    set_Joao_requests = {order["Comida"]
                         for order in orders_list
                         if order["Nome"] == "joao"}
    return set_foods - set_Joao_requests


def days_of_absent_Joao(orders_list):
    set_days = {order["Dia"] for order in orders_list}
    set_Joao_days = {order["Dia"]
                     for order in orders_list
                     if order["Nome"] == "joao"}
    return set_days - set_Joao_days


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders_reader = csv.reader(file, delimiter=",")
        orders_list = [{"Nome": row[0], "Comida": row[1], "Dia": row[2]}
                       for row in orders_reader]
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f'{more_request_by_Maria(orders_list)}\n'
                   f'{count_hamburger_for_arnaldo(orders_list)}\n'
                   f'{Joao_never_request(orders_list)}\n'
                   f'{days_of_absent_Joao(orders_list)}')
