class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_ordered = ''
        count[most_ordered] = 0
        for order in self.orders:
            if costumer == order['costumer']:
                if order['order'] not in count:
                    count[order['order']] = 1
                else:
                    count[order['order']] += 1
                if count[order['order']] > count[most_ordered]:
                    most_ordered = order['order']

        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        for order in self.orders:
            all_orders.add(order['order'])
        customer_order = set()
        for order in self.orders:
            if costumer == order['costumer']:
                customer_order.add(order['order'])
        return all_orders - customer_order

    def get_days_never_visited_per_costumer(self, costumer):
        days_of_week = set()
        for order in self.orders:
            days_of_week.add(order['day'])
        customer_set = set()
        for order in self.orders:
            if costumer == order['costumer']:
                customer_set.add(order['day'])
        return days_of_week - customer_set

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
