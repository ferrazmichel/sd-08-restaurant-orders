class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.menu = {}
        self.orders_by_custumer = {}
        self.open_week = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = [[order, day]]
        else:
            self.orders[costumer].append([order, day])
        if order not in self.menu:
            self.menu[order] = 0
        if day not in self.open_week:
            self.open_week[day] = 1
        else:
            self.open_week[day] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = self.menu.copy()
        most_frequent = self.orders[costumer][0][0]

        for row in self.orders[costumer]:
            if row[0] not in count:
                count[row[0]] = 1
            else:
                count[row[0]] += 1

            if count[row[0]] > count[most_frequent]:
                most_frequent = row[0]

        self.orders_by_custumer = count

        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        self.get_most_ordered_dish_per_costumer(costumer)

        dishes_costumer_dont_order = set()

        for dish in self.orders_by_custumer:
            if self.orders_by_custumer[dish] == 0:
                dishes_costumer_dont_order.add(dish)

        return dishes_costumer_dont_order

    def get_days_never_visited_per_costumer(self, costumer):
        client_frequency = set()

        for day in self.orders[costumer]:
            client_frequency.add(day[1])

        week = set()

        for day in self.open_week:
            week.add(day)

        return week.difference(client_frequency)

    def get_busiest_day(self):
        busiest_day = ''

        for day in self.open_week:
            if not busiest_day:
                busiest_day = day
            elif self.open_week[busiest_day] < self.open_week[day]:
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = ''

        for day in self.open_week:
            if not least_busy_day:
                least_busy_day = day
            elif self.open_week[least_busy_day] > self.open_week[day]:
                least_busy_day = day

        return least_busy_day

    def get_order_frequency_per_costumer(self, costumer, order):
        pass
