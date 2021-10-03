from collections import Counter


class TrackOrders:
    def __len__(self):
        pass
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        pass
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass
        count = Counter(
            [order[1] for order in self.orders if costumer in order]
        )
        return max(count, key=count.get)

    def get_never_ordered_per_costumer(self, costumer):
        pass
        dishes = {order[1] for order in self.orders}
        return dishes.difference(
            {order[1] for order in self.orders if costumer in order}
        )

    def get_days_never_visited_per_costumer(self, costumer):
        pass
        open_days = {order[2] for order in self.orders}
        return open_days.difference(
            {order[2] for order in self.orders if costumer in order}
        )

    def get_busiest_day(self):
        pass
        count = Counter([order[2] for order in self.orders])
        return max(count, key=count.get)

    def get_least_busy_day(self):
        pass
        count = Counter([order[2] for order in self.orders])
        return min(count, key=count.get)
