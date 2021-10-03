import csv
from collections import Counter


def analyze_log(path_to_file):
    summary = {}
    dishes = set()
    weekdays = set()

    with open(path_to_file) as file:
        orders = csv.reader(file, delimiter=",")
        for name, dish, weekday in orders:
            dishes.add(dish)
            weekdays.add(weekday)
            if name not in summary:
                summary[name] = {
                    "dishes_ordered": [dish],
                    "weekdays_with_orders": {weekday},
                }
            else:
                summary[name]["dishes_ordered"].append(dish)
                summary[name]["weekdays_with_orders"].add(weekday)

    create_log(summary, dishes, weekdays)


def create_log(summary, dishes, weekdays):
    maria_most_request = Counter(
        summary["maria"]["dishes_ordered"]
    ).most_common(1)[0][0]
    arnaldo_count_hamburguer = Counter(summary["arnaldo"]["dishes_ordered"])[
        "hamburguer"
    ]
    joao_never_request = {
        dish
        for dish in dishes
        if dish not in summary["joao"]["dishes_ordered"]
    }
    joao_never_go = {
        day
        for day in weekdays
        if day not in summary["joao"]["weekdays_with_orders"]
    }

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(
            f"{maria_most_request}\n"
            + f"{arnaldo_count_hamburguer}\n"
            + f"{joao_never_request}\n"
            + f"{joao_never_go}"
        )
