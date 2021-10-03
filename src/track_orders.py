from collections import Counter


class TrackOrders:
    def __init__(self):
        self.ordered_dishes = []

    def __len__(self):
        return len(self.ordered_dishes)

    def add_new_order(self, costumer, order, day):
        return self.ordered_dishes.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_list = list(
            record[1] for record in self.ordered_dishes
            if record[0] == costumer
        )
        return Counter(order_list).most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set(record[1] for record in self.ordered_dishes)
        dishes_per_costumer = set(
            record[1] for record in self.ordered_dishes
            if record[0] == costumer)
        return dishes.difference(dishes_per_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        day_list = list(record[2] for record in self.ordered_dishes)
        return Counter(day_list).most_common()[0][0]

    def get_least_busy_day(self):
        day_list = list(record[2] for record in self.ordered_dishes)
        return Counter(day_list).most_common()[-1][0]
