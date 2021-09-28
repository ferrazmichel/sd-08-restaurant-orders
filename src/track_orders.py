from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = []
        self.menu = set()
        self.week = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))
        self.menu.add(order)
        self.week.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_customer = {}
        for person, dish, day in self.orders:
            if person not in orders_by_customer:
                orders_by_customer[person] = []
            else:
                orders_by_customer[person].append(dish)
        return Counter(orders_by_customer[costumer]).most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        customer_order_set = set()
        for person, dish, day in self.orders:
            if person == costumer:
                customer_order_set.add(dish)
        return self.menu.difference(customer_order_set)

    def get_days_never_visited_per_costumer(self, costumer):
        days_visited = set()
        for person, dish, day in self.orders:
            if person == costumer:
                days_visited.add(day)
        return self.week.difference(days_visited)

    def get_busiest_day(self):
        day_frequency = {}
        for person, dish, day in self.orders:
            if day not in day_frequency:
                day_frequency[day] = 1
            else:
                day_frequency[day] += 1
        return max(day_frequency, key=lambda key: day_frequency[key])

    def get_least_busy_day(self):
        pass
