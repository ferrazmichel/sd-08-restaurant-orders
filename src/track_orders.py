class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        clients = {}
        for elem in self.orders:
            food = elem[1]
            if elem[0] == costumer:
                if elem[1] in clients:
                    clients[food] += 1
                else:
                    clients[food] = 1
        return max(clients, key=clients.get)

    def get_never_ordered_per_costumer(self, costumer):
        clients = set()
        foods = set()
        for elem in self.orders:
            name = elem[0]
            food = elem[1]
            foods.add(food)
            if name == costumer:
                clients.add(food)
        return foods - clients

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()
        for elem in self.orders:
            name = elem[0]
            day = elem[2]
            all_days.add(day)
            if name == costumer:
                costumer_days.add(day)
        return all_days - costumer_days

    def get_busiest_day(self):
        days = {}
        for elem in self.orders:
            day = elem[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for elem in self.orders:
            day = elem[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return min(days, key=days.get)
