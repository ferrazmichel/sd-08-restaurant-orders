import csv
from statistics import mode


def get_all_orders(data_csv):
    foods = set()
    work_days = set()
    ordered_by_joao = set()
    joao_day = set()
    ordered_by_maria = []
    hamburguers_ordered_by_arnaldo = 0

    for data in data_csv:
        foods.add(data["Pedido"])
        work_days.add(data["Dia"])

        if data["Nome"] == "maria":
            ordered_by_maria.append(data["Pedido"])

        if (
            data["Nome"] == "arnaldo"
            and data["Pedido"] == "hamburguer"
        ):
            hamburguers_ordered_by_arnaldo += 1

        if data["Nome"] == "joao":
            ordered_by_joao.add(data["Pedido"])
            joao_day.add(data["Dia"])

    most_ordered_by_maria = mode(ordered_by_maria)
    never_ordered_by_joao = foods.difference(ordered_by_joao)
    result_joao_days = work_days.difference(joao_day)

    with open('data/mkt_campaign.txt', 'w') as file:
        return file.write(
            f"{most_ordered_by_maria}\n"
            f"{hamburguers_ordered_by_arnaldo}\n"
            f"{never_ordered_by_joao}\n"
            f"{result_joao_days}"
        )


def analyze_log(path_to_file):
    try:
        with open(path_to_file) as job:
            reader = csv.DictReader(
                job, delimiter=",", fieldnames=["Nome", "Pedido", "Dia"]
            )
            data_csv = []

            for row in reader:
                data_csv.append(row)
            return get_all_orders(data_csv)

    except ValueError:
        raise NotImplementedError

# Créditos à solução da colega Giovanna Betti
