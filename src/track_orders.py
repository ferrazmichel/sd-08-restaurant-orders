from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_ordered_dishes = [
            order[1] for order in self.orders if costumer in order
        ]
        counter = Counter(costumer_ordered_dishes)
        return max(counter, key=counter.get)

    def get_never_ordered_per_costumer(self, costumer):
        dishes = {order[1] for order in self.orders}
        costumer_ordered_dishes = {
            order[1] for order in self.orders if costumer in order
        }
        return dishes.difference(costumer_ordered_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        open_days = {order[2] for order in self.orders}
        costumer_visited_days = {
            order[2] for order in self.orders if costumer in order
        }
        return open_days.difference(costumer_visited_days)

    def get_busiest_day(self):
        visited_days = [order[2] for order in self.orders]
        counter = Counter(visited_days)
        return max(counter, key=counter.get)

    def get_least_busy_day(self):
        visited_days = [order[2] for order in self.orders]
        counter = Counter(visited_days)
        return min(counter, key=counter.get)
