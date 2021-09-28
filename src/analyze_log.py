import csv
from collections import defaultdict


def _read_file(path_to_file):
    table = []
    with open(path_to_file, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            table.append(row)
    return table


def _write_file(name, data):
    with open(name, "w") as file:
        for line in data:
            file.write(str(line))
            file.write("\n")
    pass


def analyze_log(path_to_file):
    most_requst_maria = defaultdict(int)
    arnaldo_hamburguer = 0
    joao_asked = set()
    all_days = set()
    all_types_of_food = set()
    joao_days = set()
    reader = _read_file(path_to_file)
    for row in reader:
        all_days.add(row[2])
        all_types_of_food.add(row[1])
        if row[0] == "maria":
            most_requst_maria[row[1]] += 1
        elif row[0] == "arnaldo" and row[1] == "hamburguer":
            arnaldo_hamburguer += 1
        elif row[0] == "joao":
            joao_asked.add(row[1])
            joao_days.add(row[2])
    data = [
        max(most_requst_maria, key=most_requst_maria.get),
        arnaldo_hamburguer,
        all_types_of_food - joao_asked,
        all_days - joao_days,
    ]
    _write_file("./data/mkt_campaign.txt", data)
    return None
