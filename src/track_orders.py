from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals = []
        for order in self.orders:
            if order[0] == costumer:
                meals.append(order[1])

        return mode(meals)

    def get_never_ordered_per_costumer(self, costumer):
        costumer_orders = set()
        meals = set()

        for order in self.orders:
            meals.add(order[1])
            if order[0] == costumer:
                costumer_orders.add(order[1])

        return meals - costumer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_days = set()
        days = set()

        for order in self.orders:
            days.add(order[2])
            if order[0] == costumer:
                costumer_days.add(order[2])

        return days - costumer_days

    def get_busiest_day(self):
        days = []

        for order in self.orders:
            days.append(order[2])

        return mode(days)

    def get_least_busy_day(self):
        days = []

        for order in self.orders:
            days.append(order[2])

        least_busy = Counter(days).most_common()[-1]
        return least_busy[0]
