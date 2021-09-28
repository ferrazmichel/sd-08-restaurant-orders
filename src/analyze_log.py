import csv
from collections import Counter


class Order_Analyzer:
    def __init__(self, path_to_file):
        self.field_names = ['client_name', 'dish_name', 'week_day']
        with open(path_to_file) as file:
            reader = csv.DictReader(file, self.field_names)
            data = []
            for row in reader:
                data.append(row)
        self.data = data

    def _orders_by_client_name(self, name):
        return [
            {key: order[key] for key in order if key != 'client_name'}
            # dict(list(order.items())[1:])
            for order in self.data
            if order['client_name'] == name
        ]

    def _dishes_counter_by_client_name(self, name):
        client_orders = self._orders_by_client_name(name)
        return Counter([order['dish_name'] for order in client_orders])

    def most_ordered_by_client_name(self, name):
        dishes_counter = self._dishes_counter_by_client_name(name)
        return max(dishes_counter.items(), key=lambda tup: tup[1])[0]

    def quantity_of_dish_by_client_name(self, name, dish):
        dishes_counter = self._dishes_counter_by_client_name(name)
        return dishes_counter.get(dish, 0)

    def never_occurred_data_by_client_name(self, name, field_name):
        all = {order[field_name] for order in self.data}
        client_orders = self._orders_by_client_name(name)
        client_occurrences = {order[field_name] for order in client_orders}
        return all - client_occurrences


def analyze_log(path_to_file):
    analyzer = Order_Analyzer(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(analyzer.most_ordered_by_client_name('maria') + '\n')
        file.write(str(
            analyzer.quantity_of_dish_by_client_name('arnaldo', 'hamburguer'))
            + '\n')
        file.write(str(
            analyzer.never_occurred_data_by_client_name('joao', 'dish_name'))
            + '\n')
        file.write(str(
            analyzer.never_occurred_data_by_client_name('joao', 'week_day'))
            + '\n')
