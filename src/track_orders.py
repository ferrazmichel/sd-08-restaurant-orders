from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = []
        self.menu = set()
        self.week = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_customer = {}
        for person, dish, day in self.orders:
            if person not in orders_by_customer:
                orders_by_customer[person] = []
            else:
                orders_by_customer[person].append(dish)
        return Counter(orders_by_customer[costumer]).most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
