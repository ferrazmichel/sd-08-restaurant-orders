class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        all_foods = set()
        costumer_orders = set()
        for order in self.orders:
            all_foods.add(order[1])
            if costumer == order[0]:
                costumer_orders.add(order[1])
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        return all_foods.difference(costumer_orders)

    def get_never_ordered_per_costumer(self, costumer):
        all_foods = set()
        costumer_orders = set()
        for order in self.orders:
            all_foods.add(order[1])
            if costumer == order[0]:
                costumer_orders.add(order[1])
        return all_foods.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()
        for order in self.orders:
            all_days.add(order[2])
            if costumer == order[0]:
                costumer_days.add(order[2])
        return all_days.difference(costumer_days)

    def get_busiest_day(self):
        days = {}
        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
            else:
                days[order[2]] = 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for order in self.orders:
            if order[2] in days:
                days[order[2]] += 1
            else:
                days[order[2]] = 1
        return min(days, key=days.get)
