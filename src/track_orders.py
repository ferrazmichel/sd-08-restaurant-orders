class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish = {}
        for order in self.orders:
            if order["costumer"] == costumer:
                if order["order"] not in dish:
                    dish[order["order"]] = 1
                else:
                    dish[order["order"]] += 1
        return max(dish, key=dish.get)

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        costumer_orders = set()
        for order in self.orders:
            all_orders.add(order["order"])
            if order["costumer"] == costumer:
                costumer_orders.add(order["order"])
        return all_orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        costumer_days_with_order = set()
        for order in self.orders:
            days.add(order["day"])
            if order["costumer"] == costumer:
                costumer_days_with_order.add(order["day"])
        return days.difference(costumer_days_with_order)

    def number_orders_per_day(self):
        days = {}
        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order["day"]] += 1
        return days

    def get_busiest_day(self):
        days = self.number_orders_per_day()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = self.number_orders_per_day()
        return min(days, key=days.get)
