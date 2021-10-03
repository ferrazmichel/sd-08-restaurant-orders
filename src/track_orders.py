# from typing import Dict, List


class TrackOrders:

    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = [order for order in self.orders if costumer in order]
        orders = [order[1] for order in costumer_orders]
        dict_orders = {i: orders.count(i) for i in orders}
        higher_order = max(dict_orders, key=dict_orders.get)
        return higher_order

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
