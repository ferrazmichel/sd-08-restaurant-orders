class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered = dict()
        for custom, order, day in self.orders:
            if custom == costumer:
                if order in most_ordered:
                    most_ordered[order] = most_ordered[order] + 1
                else:
                    most_ordered[order] = 1
        return max(most_ordered, key=most_ordered.get)

    def get_never_ordered_per_costumer(self, costumer):
        total_plates = set([item[1] for item in self.orders])
        total_customer = set(
            [item[1] for item in self.orders if item[0] == costumer]
        )
        return total_plates.difference(total_customer)

    def get_days_never_visited_per_costumer(self, costumer):
        total_days = set([item[2] for item in self.orders])
        total_customer_days = set(
            [item[2] for item in self.orders if item[0] == costumer]
        )
        return total_days.difference(total_customer_days)

    def get_busiest_day(self):
        most_busy_day = dict()
        for customer, order, d in self.orders:
            if d in most_busy_day:
                most_busy_day[d] = most_busy_day[d] + 1
            else:
                most_busy_day[d] = 1
        return max(most_busy_day, key=most_busy_day.get)

    def get_least_busy_day(self):
        least_busy_day = dict()
        for customer, order, d in self.orders:
            if d in least_busy_day:
                least_busy_day[d] = least_busy_day[d] + 1
            else:
                least_busy_day[d] = 1
        return min(least_busy_day, key=least_busy_day.get)
