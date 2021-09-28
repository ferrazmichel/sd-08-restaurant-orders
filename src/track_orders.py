class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        my_dict = dict()
        value = 0
        for x in self.orders:
            if x[0] == costumer:
                if x[0] not in my_dict:
                    my_dict[x[0]] = 1
                else:
                    my_dict[x[0]] += 1
                if my_dict[x[0]] > value:
                    value = my_dict[x[0]]
                    dish = x[1]
        return dish

        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
