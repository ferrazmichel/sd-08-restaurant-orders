class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes_counter = {}
        for order_row in self.orders:
            if order_row[0] == costumer:
                if order_row[1] == dishes_counter:
                    dishes_counter[order_row[1]] += 1
                else:
                    dishes_counter[order_row[1]] = 1
        return max(dishes_counter, key=dishes_counter.get)

    def get_never_ordered_per_costumer(self, costumer):
        client_order = set()
        all_orders = set()
        for order_row in self.orders:
            all_orders.add(order_row[1])
            if order_row[0] == costumer:
                client_order.add(order_row[1])
        return all_orders - client_order

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_visited = set()
        for order_row in self.orders:
            days.add(order_row[2])
            if order_row[0] == costumer:
                days_visited.add(order_row[2])
        return days - days_visited

    def get_busiest_day(self):
        busiest_day_counter = {}
        for order_row in self.orders:
            if order_row[2] in busiest_day_counter:
                busiest_day_counter[order_row[2]] += 1
            else:
                busiest_day_counter[order_row[2]] = 1
        return max(busiest_day_counter, key=busiest_day_counter.get)

    def get_least_busy_day(self):
        least_busy_day_counter = {}
        for order_row in self.orders:
            if order_row[2] in least_busy_day_counter:
                least_busy_day_counter[order_row[2]] += 1
            else:
                least_busy_day_counter[order_row[2]] = 1
        return min(least_busy_day_counter, key=least_busy_day_counter.get)
