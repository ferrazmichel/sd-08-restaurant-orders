# from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = {}

    def __len__(self):
        return len(self.orders)

    def get_dish_per_costumer(self, costumer):
        pass

    def add_new_order(self, costumer, order, day):
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = max(self.orders[costumer]["dishes"])  # interação - lista de lista
        return result.key

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        alldays = ([
                "segunda-feira",
                "terça-feira",
                "sabado",
            ])
        result = self.orders[costumer]["days"]  # fazer uma iteração
        return alldays.difference(result.key)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
