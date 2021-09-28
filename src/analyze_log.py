import csv

# from collections import Counter
from statistics import mode

# https://docs.python.org/pt-br/3/library/csv.html#csv.DictReader


def get_results(data_csv):
    all_foods = set()
    all_days = set()
    maria_most_ordered = []
    count_arnaldo_ordered_hamburguer = 0
    joao_ordered = set()
    joao_dayin = set()

    for data in data_csv:
        # print(data)
        all_foods.add(data["Pedido"])
        all_days.add(data["Dia"])
        if data["Nome"] == "maria":
            maria_most_ordered.append(data["Pedido"])
        if (
            data["Nome"] == "arnaldo"
            and data["Pedido"] == "hamburguer"
        ):
            count_arnaldo_ordered_hamburguer += 1

        if data["Nome"] == "joao":
            joao_ordered.add(data["Pedido"])
            joao_dayin.add(data["Dia"])

    # https://docs.python.org/3/library/statistics.html
    result_maria_most_ordered = mode(maria_most_ordered)
    result_joao_never_ordered = all_foods - joao_ordered
    result_joao_dayouts = all_days - joao_dayin

    # print(count_arnaldo_ordered_hamburguer)
    # print(all_foods - joao_ordered)
    # print(all_days - joao_dayin)
    # print(result_maria_most_ordered)
    print_result = (
        f"{result_maria_most_ordered}\n"
        f"{count_arnaldo_ordered_hamburguer}\n"
        f"{result_joao_never_ordered}\n"
        f"{result_joao_dayouts}"
        )
    with open('data/mkt_campaign.txt', 'w') as file:
        return file.write(print_result)


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


# path_to_file = "data/orders_1.csv"
# print(analyze_log(path_to_file))
