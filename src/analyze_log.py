import csv


def maria_most_ordered_dishes(item, dishes):
    if item[0] == "maria":
        dishes[item[1]] = dishes.get(item[1], 0) + 1


def arnaldo_hamburguer_quantity(item):
    return item[0] == "arnaldo" and item[1] == "hamburguer"

def joao_missing_dishes_and_days(item, joao_orders, joao_days):
    if item[0] == "joao":
        joao_orders.add(item[1])
        joao_days.add(item[2])

def analyze_log(path_to_file):
    try:
        file = open(path_to_file)
        reader = csv.reader(file, delimiter=",")

        maria_dishes = {}
        arnaldo_hamburguer = 0
        foods = set()
        days = set()
        joao_orders = set()
        joao_days = set()

        for item in reader:
            foods.add(item[1])
            days.add(item[2])
            maria_most_ordered_dishes(item, maria_dishes)
            if arnaldo_hamburguer_quantity(item):
                arnaldo_hamburguer += 1
            joao_missing_dishes_and_days(item, joao_orders, joao_days)

        # https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
        maria = max(maria_dishes, key=maria_dishes.get)
    
        joao = [(foods - joao_orders), (days - joao_days)]

        # https://www.pythontutorial.net/python-basics/python-write-text-file/
        with open('data/mkt_campaign.txt', 'w') as f:
            f.write(f'{maria}\n')
            f.write(f'{arnaldo_hamburguer}\n')
            f.write(f'{joao[0]}\n')
            f.write(f'{joao[1]}')
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: " "'{}'".format(path_to_file))
