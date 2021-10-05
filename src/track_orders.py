class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = dict()

        for item in self.orders:
            if item['costumer'] == costumer and item['order'] not in ordered:
                ordered[item['order']] = 1

            if item['costumer'] == costumer:
                ordered[item['order']] += 1

        return max(ordered, key=ordered.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        count_frequency = 0

        for order in self.orders:
            if order['costumer'] == costumer and order['order'] == order:
                count_frequency += 1

        return count_frequency

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        client_dishes = set()

        for order in self.orders:
            dishes.add(order['order'])

            if order['costumer'] == costumer:
                client_dishes.add(order['order'])

        return dishes.difference(client_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        restaurant_open = set()
        client_frequency = set()

        for order in self.orders:
            restaurant_open.add(order['day'])

            if order['costumer'] == costumer:
                client_frequency.add(order['day'])

        return restaurant_open.difference(client_frequency)

    def get_busiest_day(self):
        clients_frequency = {}

        for order in self.orders:
            if order['day'] not in clients_frequency:
                clients_frequency[order['day']] = 1

            else:
                clients_frequency[order['day']] += 1

        return max(clients_frequency, key=clients_frequency.get)

    def get_least_busy_day(self):
        clients_frequency = {}

        for order in self.orders:
            if order['day'] not in clients_frequency:
                clients_frequency[order['day']] = 1

            else:
                clients_frequency[order['day']] += 1

        return min(clients_frequency, key=clients_frequency.get)