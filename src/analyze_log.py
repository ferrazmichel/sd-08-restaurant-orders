import csv


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        restaurant_log = csv.reader(file, delimiter=",", quotechar='"')

        log_screening = screening(restaurant_log)
        dict_restaurant_log = log_screening[0]
        menu = log_screening[1]
        days_week = log_screening[2]

        most_dish_by_maria = count_dish_by_client(
            menu, dict_restaurant_log, "maria"
        )[0]

        count_hamburger_by_arnaldo = count_dish_by_client(
            menu, dict_restaurant_log, "arnaldo"
        )[1]["hamburguer"]

        dishes_by_joao = count_dish_by_client(
            menu, dict_restaurant_log, "joao"
        )

        dishes_joao_dont_order = set()

        for dish in dishes_by_joao[1]:
            if dishes_by_joao[1][dish] == 0:
                dishes_joao_dont_order.add(dish)

        joao_frequency = client_frequency_week(dict_restaurant_log, "joao")

        days_week_without_joao = days_week.difference(joao_frequency)

    data_file = open("data/mkt_campaign.txt", mode="w")
    data_file.writelines([
        most_dish_by_maria, '\n',
        str(count_hamburger_by_arnaldo), '\n',
        str(dishes_joao_dont_order), '\n',
        str(days_week_without_joao)
    ])


def count_dish_by_client(menu, log, name):
    count = menu.copy()
    most_frequent = log[name][0][0]

    for row in log[name]:
        if row[0] not in count:
            count[row[0]] = 1
        else:
            count[row[0]] += 1

        if count[row[0]] > count[most_frequent]:
            most_frequent = row[0]

    return most_frequent, count


def screening(logs):
    logs_by_clients = {}
    menu = {}
    open_week = set()

    for row in logs:
        if row[0] not in logs_by_clients:
            logs_by_clients[row[0]] = [[row[1], row[2]]]
        else:
            logs_by_clients[row[0]].append([row[1], row[2]])

        if row[1] not in menu:
            menu[row[1]] = 0

        if row[2] not in open_week:
            open_week.add(row[2])

    return [logs_by_clients, menu, open_week]


def client_frequency_week(log, name):
    client_frequency = set()

    for day in log[name]:
        client_frequency.add(day[1])

    return client_frequency
