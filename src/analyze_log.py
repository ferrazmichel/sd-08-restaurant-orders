import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    output_file = "data/mkt_campaign.txt"
    contents = []
    tracker = TrackOrders()
    with open(path_to_file, mode='r') as read_file:
        result = csv.reader(read_file, delimiter="\n")
        for row in result:
            contents.append(row)
    with open(output_file, mode='w') as write_file:
        print(
            tracker.get_most_ordered_dish_per_costumer("maria"),
            tracker.get_dish_per_costumer("arnaldo", "hamburguer"),
            tracker.get_never_ordered_per_costumer("joao"),
            tracker.get_days_never_visited_per_costumer("joao"),
            sep="\n", file=write_file
            )
