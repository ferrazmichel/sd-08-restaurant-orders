from src.analyze_log import (
    most_ordered_meal, food_never_ordered, never_went_to_diner
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_ordered_meal(costumer, self.orders)

    def get_never_ordered_per_costumer(self, costumer):
        return food_never_ordered(costumer, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return never_went_to_diner(costumer, self.orders)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
