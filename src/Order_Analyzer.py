import csv
from collections import Counter


def without_keys(dct, keys):
    '''
    Receives a dictionary and returns a new one without the
    specified keys.
    '''
    dct = dct.copy()
    for key in keys:
        dct.pop(key)
    return dct


class OrderAnalyzer:
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
            without_keys(order, ['client_name'])
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
