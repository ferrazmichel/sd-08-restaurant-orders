import csv
from statistics import mode


def get_results(data_csv):
    days = set()
    foods = set()
    maria_ordered = []
    count_arnaldo_hamburguer = 0
    joao_day = set()
    joao_ordered = set()

    for data in data_csv:
        foods.add(data["Pedido"])
        days.add(data["Dia"])
        if data["Nome"] == "maria":
            maria_ordered.append(data["Pedido"])
        elif (
            data["Nome"] == "arnaldo"
            and data["Pedido"] == "hamburguer"
        ):
            count_arnaldo_hamburguer += 1

        elif data["Nome"] == "joao":
            joao_ordered.add(data["Pedido"])
            joao_day.add(data["Dia"])

    result_maria_ordered = mode(maria_ordered)
    result_joao_never_ordered = foods - joao_ordered
    result_joao_dayouts = days - joao_day

    result = (
        f"{result_maria_ordered}\n"
        f"{count_arnaldo_hamburguer}\n"
        f"{result_joao_never_ordered}\n"
        f"{result_joao_dayouts}"
    )
    with open('data/mkt_campaign.txt', 'w') as file:
        return file.write(result)


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as job:
            data = csv.DictReader(
                job, delimiter=",", fieldnames=["Nome", "Pedido", "Dia"]
            )
            data_csv = []
            for row in data:
                data_csv.append(row)
        return get_results(data_csv)
    except ValueError:
        raise NotImplementedError


path_to_file = "data/orders_1.csv"
print(analyze_log(path_to_file))
