import csv


def get_most_ordered_by_client(path_to_file, client):
    with open(path_to_file) as file:
        orders = csv.reader(file, delimiter=",", quotechar='"')
        clientCount = {}
        for order in orders:
            if (order[0] == client):
                if (order[1] not in clientCount):
                    clientCount[order[1]] = 1
                else:
                    clientCount[order[1]] += 1
        # https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python#get
        return max(clientCount, key=clientCount.get)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders = csv.reader(file, delimiter=",", quotechar='"')
        mariaMostOrdered = get_most_ordered_by_client(path_to_file, 'maria')
        arnaldoHamburguerOrders = 0
        menu = set()
        joaoOrders = set()
        joaoOrderDays = set()
        daysOfTheWeek = set()
        for order in orders:
            menu.add(order[1])
            daysOfTheWeek.add(order[2])
            if (order[0] == 'arnaldo' and order[1] == 'hamburguer'):
                arnaldoHamburguerOrders += 1
            if (order[0] == 'joao'):
                joaoOrders.add(order[1])
                joaoOrderDays.add(order[2])
        with open('data/mkt_campaign.txt', 'w') as output_file:
            output_file.write(f'{mariaMostOrdered}\n')
            output_file.write(f'{str(arnaldoHamburguerOrders)}\n')
            output_file.write(f'{str(menu.difference(joaoOrders))}\n')
            output_file.write(
                f'{str(daysOfTheWeek.difference(joaoOrderDays))}'
                )
