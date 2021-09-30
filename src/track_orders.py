import operator


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods = {}
        for order in self.orders:
            if order[0] == costumer:
                try:
                    foods[order[1]] += 1
                except KeyError:
                    foods[order[1]] = 1
        return max(foods.items(), key=operator.itemgetter(1))[0]

    def get_never_ordered_per_costumer(self, costumer):
        total_foods = set()
        costumer_foods = set()
        for order in self.orders:
            total_foods.add(order[1])
            if order[0] == costumer:
                costumer_foods.add(order[1])
        # Todos os pedido MENOS os pedidos feitos = pedidos nunca realizados
        return total_foods - costumer_foods

    def get_days_never_visited_per_costumer(self, costumer):
        total_days = set()
        costumer_days = set()
        for order in self.orders:
            total_days.add(order[2])
            if order[0] == costumer:
                costumer_days.add(order[2])
        # Todos os dias MENOS dias que o costumer visitou
        # = dias que nunca visitou
        return total_days - costumer_days

    def get_busiest_day(self):
        days = {}
        for order in self.orders:
            try:
                days[order[2]] += 1
            except KeyError:
                days[order[2]] = 1
        # dia que mais se repete
        return max(days.items(), key=operator.itemgetter(1))[0]

    def get_least_busy_day(self):
        days = {}
        for order in self.orders:
            try:
                days[order[2]] += 1
            except KeyError:
                days[order[2]] = 1
        # dia que menos se repete
        return min(days.items(), key=operator.itemgetter(1))[0]
