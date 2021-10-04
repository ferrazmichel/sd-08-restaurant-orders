class TrackOrders:
    def __init__(self):
        self.orders = []
        self.menu = set()
        self.daysOfWeek = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.menu.add(order)
        self.daysOfWeek.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumerOrders = {}
        for order in self.orders:
            if (order[0] == costumer):
                if (order[1] not in costumerOrders):
                    costumerOrders[order[1]] = 1
                else:
                    costumerOrders[order[1]] += 1
        # https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python#get
        return max(costumerOrders, key=costumerOrders.get)

    def get_never_ordered_per_costumer(self, costumer):
        costumerOrders = set()
        for order in self.orders:
            if (order[0] == costumer):
                costumerOrders.add(order[1])
        return self.menu.difference(costumerOrders)

    def get_days_never_visited_per_costumer(self, costumer):
        costumerOrderDays = set()
        for order in self.orders:
            if (order[0] == costumer):
                costumerOrderDays.add(order[2])
        return self.daysOfWeek.difference(costumerOrderDays)

    def get_busiest_day(self):
        ordersByDay = {}
        for order in self.orders:
            if (order[2] not in ordersByDay):
                ordersByDay[order[2]] = 1
            else:
                ordersByDay[order[2]] += 1
        return max(ordersByDay, key=ordersByDay.get)

    def get_least_busy_day(self):
        ordersByDay = {}
        for order in self.orders:
            if (order[2] not in ordersByDay):
                ordersByDay[order[2]] = 1
            else:
                ordersByDay[order[2]] += 1
        return min(ordersByDay, key=ordersByDay.get)
