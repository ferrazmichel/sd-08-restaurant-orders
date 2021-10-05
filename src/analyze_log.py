import csv
from src.track_orders import TrackOrders


def get_orders_data(path_to_file):
    field_names = ['customer', 'dish', 'week_day']
    with open(path_to_file) as file:
        reader = csv.DictReader(file, field_names)
        data = []
        for row in reader:
            data.append(row)
    return data


def analyze_log(path_to_file):
    orders_data = get_orders_data(path_to_file)
    analyzer = TrackOrders(orders_data)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(analyzer.get_most_ordered_dish_per_costumer('maria') + '\n')
        file.write(str(
            analyzer.get_quantity_of_dish_per_customer('arnaldo', 'hamburguer')
            )
            + '\n')
        file.write(str(
            analyzer.get_never_ordered_per_costumer('joao'))
            + '\n')
        file.write(str(
            analyzer.get_days_never_visited_per_costumer('joao'))
            + '\n')
