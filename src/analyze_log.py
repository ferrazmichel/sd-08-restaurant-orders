import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    if not path_to_file or not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    track_orders = TrackOrders()
    try:
        with open(path_to_file, "r") as csv_file:
            # ñ precisa ler com DictReader, reader retorna cada linha um array
            # csv_reader = csv.DictReader(csv_file, delimiter=",")
            csv_reader = csv.reader(csv_file, delimiter=",")
            for info in csv_reader:
                track_orders.add_new_order(info[0], info[1], info[2])
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    most_ordered_by_maria = track_orders.get_most_ordered_dish_per_costumer(
        "maria"
    )
    times_arnaldo_ordered_hamburguer = (
        track_orders.get_how_many_times_dish_was_ordered(
            "arnaldo", "hamburguer"
        )
    )
    how_many_dishes_joao_never_ordered = (
        track_orders.get_never_ordered_per_costumer("joao")
    )

    what_days_joao_never_went_to_restaurant = (
        track_orders.get_days_never_visited_per_costumer("joao")
    )

    a = most_ordered_by_maria
    b = times_arnaldo_ordered_hamburguer
    c = how_many_dishes_joao_never_ordered
    d = what_days_joao_never_went_to_restaurant

    result = f"{a}\n{b}\n{c}\n{d}"

    mkt_campaign = open("data/mkt_campaign.txt", "w")
    mkt_campaign.write(result)
    mkt_campaign.close()
