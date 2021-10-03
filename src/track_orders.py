class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods = {}
        for item in self.orders:
            if item[0] == costumer:
                foods[item[1]] = foods.get(item[1], 0) + 1
        return max(foods, key=foods.get)

    def get_never_ordered_per_costumer(self, costumer):
        foods = set()
        customer_orders = set()
        for item in self.orders:
            foods.add(item[1])
            if item[0] == costumer:
                customer_orders.add(item[1])
        return foods - customer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        customer_days = set()
        for item in self.orders:
            days.add(item[2])
            if item[0] == costumer:
                customer_days.add(item[2])
        return days - customer_days

    def get_busiest_day(self):
        days = {}
        for item in self.orders:
            days[item[2]] = days.get(item[2], 0) + 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for item in self.orders:
            days[item[2]] = days.get(item[2], 0) + 1
        return min(days, key=days.get)
