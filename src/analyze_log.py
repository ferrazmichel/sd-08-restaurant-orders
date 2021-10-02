import csv
from collections import Counter


def analyze_log(path_to_file):
    if not (path_to_file.endswith(".csv")):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    summary, dishes, weekdays = summarize_orders(path_to_file)

    generate_log(summary, dishes, weekdays)


def summarize_orders(path_to_file):
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
    return [summary, dishes, weekdays]


def generate_log(summary, dishes, weekdays):
    maria_eats = Counter(summary["maria"]["dishes_ordered"]).most_common(1)[0][
        0
    ]
    arnaldo_ask_hamburguer = Counter(summary["arnaldo"]["dishes_ordered"])[
        "hamburguer"
    ]
    joao_never_ask = {
        dish
        for dish in dishes
        if dish not in summary["joao"]["dishes_ordered"]
    }
    joao_never_went = {
        day
        for day in weekdays
        if day not in summary["joao"]["weekdays_with_orders"]
    }

    print(joao_never_ask)
    print(joao_never_went)

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(
            f"{maria_eats}\n"
            + f"{arnaldo_ask_hamburguer}\n"
            + f"{joao_never_ask}\n"
            + f"{joao_never_went}"
        )
