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
        # source: https://www.kite.com/python/answers/how-to-find-the-max-
        # value-in-a-dictionary-in-python#:~:text=values()%20to%20find%20the
        # ,max%20value%20of%20the%20dictionary.
        return max(foods, key=foods.get)

    def get_never_ordered_per_costumer(self, costumer):
        all_foods = set()
        costumer_foods = set()
        # por ser um set nunca adiciona repetidos e ao
        # fazer a diferença entre os dois conjuntos terá os nunca pedidos
        for order in self.orders:
            all_foods.add(order[1])
            if order[0] == costumer:
                costumer_foods.add(order[1])
        return all_foods - costumer_foods

    def get_days_never_visited_per_costumer(self, costumer):
        days_of_week = set()
        costumer_days = set()
        for order in self.orders:
            days_of_week.add(order[2])
            if order[0] == costumer:
                costumer_days.add(order[2])
        return days_of_week - costumer_days

    def get_busiest_day(self):
        days = {}
        for order in self.orders:
            try:
                days[order[2]] += 1
            except KeyError:
                days[order[2]] = 1
        # source: https://www.kite.com/python/answers/how-to-find-the-max-
        # value-in-a-dictionary-in-python#:~:text=values()%20to%20find%20the
        # ,max%20value%20of%20the%20dictionary.
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for order in self.orders:
            try:
                days[order[2]] += 1
            except KeyError:
                days[order[2]] = 1
        # source: https://www.kite.com/python/answers/how-to-find-the-max-
        # value-in-a-dictionary-in-python#:~:text=values()%20to%20find%20the
        # ,max%20value%20of%20the%20dictionary.
        return min(days, key=days.get)
        pass

    def get_how_many_times_dish_was_ordered(self, customer, dish):
        times = 0
        for order in self.orders:
            if order[0] == customer and order[1] == dish:
                times += 1
        return times
