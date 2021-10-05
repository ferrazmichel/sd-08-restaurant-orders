class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for prato in self.orders:
            if prato[0] == costumer:
                orders.append(prato[1])
        return max(set(orders), key=orders.count)

    def get_never_ordered_per_costumer(self, costumer):
        rangos = set()
        order_costumer = set()
        for prato in self.orders:
            rangos.add(prato[1])
        for prato in self.orders:
            if prato[0] == costumer:
                order_costumer.add(prato[1])
        return rangos.difference(order_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        working_days = set()
        order_costumer = set()
        for prato in self.orders:
            working_days.add(prato[2])
        for prato in self.orders:
            if prato[0] == costumer:
                order_costumer.add(prato[2])
        return working_days.difference(order_costumer)

    def get_busiest_day(self):
        order_day = []
        for order in self.orders:
            order_day.append(order[2])
        return max(set(order_day), key=order_day.count)

    def get_least_busy_day(self):
        order_day = []
        for order in self.orders:
            order_day.append(order[2])
        return min(set(order_day), key=order_day.count)
