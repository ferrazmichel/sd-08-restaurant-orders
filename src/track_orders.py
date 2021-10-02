class TrackOrders:
    def __init__(self):
        self.orders = dict()
        self.restaurant_menu = set()
        self.restaurant_dates = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.restaurant_menu.add(order)
        self.restaurant_dates.add(day)

        if customer not in self.orders:
            self.orders[customer] = {"orders": [], "days": []}

        self.orders[customer]["orders"].append(order)
        self.orders[customer]["days"].append(day)

    def get_most_ordered_dish_per_costumer(self, customer):
        if customer not in self.orders:
            return []
        customer_orders = self.orders[customer]["orders"]
        return max(set(customer_orders), key=customer_orders.count)

    def get_never_ordered_per_costumer(self, customer):
        return self.restaurant_menu - set(self.orders[customer]["orders"])

    def get_days_never_visited_per_costumer(self, customer):
        return self.restaurant_dates - set(self.orders[customer]["days"])

    def get_busiest_day(self):
        visited_days = self.get_all_customers_visits()
        return max(set(visited_days), key=visited_days.count)

    def get_least_busy_day(self):
        visited_days = self.get_all_customers_visits()
        return min(set(visited_days), key=visited_days.count)

    def get_all_customers_visits(self):
        visited_days = []
        for customer in self.orders:
            visited_days.extend(self.orders[customer]["days"])
        return visited_days
