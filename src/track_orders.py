class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = [order for order in self.orders if costumer in order]
        orders = [order[1] for order in costumer_orders]
        dict_orders = {i: orders.count(i) for i in orders}
        higher_order = max(dict_orders, key=dict_orders.get)
        return higher_order

    def get_never_ordered_per_costumer(self, costumer):
        costumer_orders = [order for order in self.orders if costumer in order]
        orders = [order[1] for order in costumer_orders]
        costumer_orders_dict = {i for i in orders}

        general_orders = [order[1] for order in self.orders]
        general_orders_dict = {i for i in general_orders}

        return general_orders_dict - costumer_orders_dict

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_day = [day for day in self.orders if costumer in day]
        days = [day[2] for day in costumer_day]
        costumer_days_dict = {i for i in days}

        general_days = [day[2] for day in self.orders]
        general_days_dict = {i for i in general_days}

        return general_days_dict - costumer_days_dict

    def get_busiest_day(self):
        general_days = [day[2] for day in self.orders]
        general_days_dict = {i: general_days.count(i) for i in general_days}
        max_key = max(general_days_dict, key=general_days_dict.get)
        return max_key

    def get_least_busy_day(self):
        general_days = [day[2] for day in self.orders]
        general_days_dict = {i: general_days.count(i) for i in general_days}
        min_key = min(general_days_dict, key=general_days_dict.get)
        return min_key
