class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders) or 0

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_frequent = 'teste'
        count[most_frequent] = 0
        for order in self.orders:
            if costumer == order['costumer']:
                if order['order'] not in count:
                    count[order['order']] = 1
                else:
                    count[order['order']] += 1
                if count[order['order']] > count[most_frequent]:
                    most_frequent = order['order']

        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        meals_set = set()
        for order in self.orders:
            meals_set.add(order['order'])

        customer_set = set()
        for order in self.orders:
            if costumer == order['costumer']:
                customer_set.add(order['order'])

        return meals_set - customer_set

    def get_days_never_visited_per_costumer(self, costumer):
        dates_set = set()
        for order in self.orders:
            dates_set.add(order['day'])
        customer_set = set()
        for order in self.orders:
            if costumer == order['costumer']:
                customer_set.add(order['day'])
        return dates_set - customer_set

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
