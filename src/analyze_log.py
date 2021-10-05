import csv
from collections import Counter


def analyze_log(path_to_file):
    with open(path_to_file) as orders:
        order_dict = list(
            csv.DictReader(orders, fieldnames=["client", "food", "day"])
        )

        maria_favorite = get_marias_fav(order_dict)
        arnaldo_burgers = get_arnaldo_burgers(order_dict)
        joao_not_ordered = get_joao_not_ordered(order_dict)
        joao_not_visited_dates = get_joao_not_visited_days(order_dict)

        with open("data/mkt_campaign.txt", "w+") as destination:
            destination.writelines(
                "\n".join(
                    [
                        maria_favorite,
                        arnaldo_burgers,
                        joao_not_ordered,
                        joao_not_visited_dates,
                    ]
                )
            )


def get_marias_fav(order_dict):
    maria_orders = Counter(
        order["food"] for order in order_dict if order["client"] == "maria"
    )

    return max(maria_orders, key=maria_orders.get)


def get_arnaldo_burgers(order_dict):
    arnaldo_foods = Counter(
        order["food"] for order in order_dict if order["client"] == "arnaldo"
    )

    return str(arnaldo_foods["hamburguer"])


def get_joao_not_ordered(order_dict):
    all_foods = set([order["food"] for order in order_dict])
    joao_foods = set(
        [order["food"] for order in order_dict if order["client"] == "joao"]
    )

    return str(all_foods - joao_foods)


def get_joao_not_visited_days(order_dict):
    all_days = set([order["day"] for order in order_dict])
    joao_days = set(
        [order["day"] for order in order_dict if order["client"] == "joao"]
    )

    return str(all_days - joao_days)


analyze_log("data/orders_1.csv")
