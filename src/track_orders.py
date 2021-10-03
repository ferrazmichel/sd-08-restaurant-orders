from collections import Counter


class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        self.data.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_food = []
        for order in self.data:
            if order[0] == costumer:
                order_food.append(order[1])

        # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/#:~:text=Copy%20key3-,Utilize%20max()%20e%20dict.,%C3%A9%20utilizado%20o%20m%C3%A9todo%20dict.
        # Obter a chave com o maior valor de um dicionario
        return str(max(Counter(order_food), key=Counter(order_food).get))

    def get_never_ordered_per_costumer(self, costumer):
        orders_costumer = set()
        all_food = set()
        for order in self.data:
            all_food.add(order[1])
            if order[0] == costumer:
                orders_costumer.add(order[1])

        return all_food - orders_costumer

    def get_days_never_visited_per_costumer(self, costumer):
        days_costumer = set()
        all_days = set()
        for order in self.data:
            all_days.add(order[2])
            if order[0] == costumer:
                days_costumer.add(order[2])

        return all_days - days_costumer

    def get_busiest_day(self):
        busiest_day = []
        for order in self.data:
            busiest_day.append(order[2])

        # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/#:~:text=Copy%20key3-,Utilize%20max()%20e%20dict.,%C3%A9%20utilizado%20o%20m%C3%A9todo%20dict.
        # Obter a chave com o maior valor de um dicionario
        return str(max(Counter(busiest_day), key=Counter(busiest_day).get))

    def get_least_busy_day(self):
        less_busy_day = []
        for order in self.data:
            less_busy_day.append(order[2])

        return str(min(Counter(less_busy_day), key=Counter(less_busy_day).get))
