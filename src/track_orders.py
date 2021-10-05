class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        food_amount = {}
        for order in self.orders:
            [name, order_prod, _] = order
            if costumer == name:
                try:
                    food_amount[order_prod] += 1
                except KeyError:
                    food_amount[order_prod] = 1

        return max(food_amount, key=food_amount.get)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def orders_count(self):
        days_orders = {}
        for [_, _, day] in self.orders:
            try:
                days_orders[day] += 1
            except KeyError:
                days_orders[day] = 1
        return days_orders

    def get_busiest_day(self):
        orders_amount = self.orders_count()
        return max(orders_amount, key=orders_amount.get)

    def get_least_busy_day(self):
        orders_amount = self.orders_count()
        return min(orders_amount, key=orders_amount.get)
