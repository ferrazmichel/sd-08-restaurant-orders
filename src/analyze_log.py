import csv
from statistics import mode


def analyze_log(path_to_file):
    maria_orders = []
    joao_orders = set()
    joao_days = set()
    counter = 0
    days = set()
    meals = set()

    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')

        for order in data:
            meals.add(order[1])
            days.add(order[2])
            if order[0] == "maria":
                maria_orders.append(order[1])
            if order[0] == "joao":
                joao_orders.add(order[1])
                joao_days.add(order[2])
            if order[0] == "arnaldo" and order[1] == "hamburguer":
                counter += 1

    report = open('data'+'/'+'mkt_campaign.txt', 'w')
    report.write(f"{mode(maria_orders)}\n")
    report.write(f"{counter}\n")
    report.write(f"{meals - joao_orders}\n")
    report.write(f"{days - joao_days}\n")
