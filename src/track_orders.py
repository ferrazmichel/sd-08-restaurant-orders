from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for item in self.orders:
            if item[0] == costumer:
                orders.append(item[1])
        count = Counter(orders)
        count_max = max(count.values())
        for k, v in count.items():
            if v == count_max:
                dish = k
        return dish

    def get_never_ordered_per_costumer(self, costumer):
        foods = {'hamburguer', 'pizza', 'coxinha', 'misto-quente'}
        orders = []
        for item in self.orders:
            if item[0] == costumer:
                orders.append(item[1])
        orders = set(orders)
        foods = foods.difference(orders)
        return foods

    def get_days_never_visited_per_costumer(self, costumer):
        orders = set()
        days = {"segunda-feira", "terça-feira", "sabado"}
        for item in self.orders:
            if item[0] == costumer:
                orders.add(item[2])
        days = days.difference(orders)
        return days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
