class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders) or 0

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals_count = {}
        most = ""
        orders_by_custumer = filter(lambda o: o['costumer']
                                    == costumer, self.orders)

        for order in orders_by_custumer:
            actual_meal = order['order']
            if actual_meal not in meals_count:
                meals_count[actual_meal] = 1
            else:
                meals_count[actual_meal] += 1
            if most == "" or meals_count[actual_meal] > meals_count[most]:
                most = actual_meal

        return most

    def get_never_ordered_per_costumer(self, costumer):
        meals_unique = set()
        for order in self.orders:
            meals_unique.add(order['order'])

        meals_unique_by_customer = set()
        cust_order = filter(lambda o: o['costumer'] == costumer, self.orders)
        for order in cust_order:
            meals_unique_by_customer.add(order['order'])

        return meals_unique - meals_unique_by_customer

    def get_days_never_visited_per_costumer(self, costumer):
        dates_set = set()
        for order in self.orders:
            dates_set.add(order['day'])

        customer_set = set()
        filter_order = filter(lambda o: o['costumer'] == costumer, self.orders)
        for order in filter_order:
            customer_set.add(order['day'])

        return dates_set - customer_set

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
