from src.analyze_log import (
    most_requested_plate, never_ordered_plate, days_without_orders
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_requested_plate(costumer, self.orders)

    def get_never_ordered_per_costumer(self, costumer):
        return never_ordered_plate(costumer, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return days_without_orders(costumer, self.orders)

    def orders_per_day(self):
        days = {}
        for order in self.orders:
            if order[2] not in days:
                days[order[2]] = 1
            else:
                days[order[2]] += 1
        return days

    def get_busiest_day(self):
        days = self.orders_per_day()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = self.orders_per_day()
        return min(days, key=days.get)
