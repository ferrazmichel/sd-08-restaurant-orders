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
        orders_costumer = set()
        for prato in self.orders:
            rangos.add(prato[1])
        for prato in self.orders:
            if prato[0] == costumer:
                orders_costumer.add(prato[1])
        return rangos.difference(orders_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
