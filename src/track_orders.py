class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"Nome": costumer, "Comida": order, "Dia": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_frequent = self.orders[0]["Comida"]

        for order in self.orders:
            name, food = (order["Nome"], order["Comida"])
            if name == costumer:
                if food not in count:
                    count[food] = 1
                else:
                    count[food] += 1
                    if count[food] > count[most_frequent]:
                        most_frequent = food
        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        set_foods = {order["Comida"] for order in self.orders}
        set_Joao_requests = {order["Comida"]
                             for order in self.orders
                             if order["Nome"] == costumer}
        return set_foods - set_Joao_requests

    def get_days_never_visited_per_costumer(self, costumer):
        set_days = {order["Dia"] for order in self.orders}
        set_Joao_days = {order["Dia"]
                         for order in self.orders
                         if order["Nome"] == costumer}
        return set_days - set_Joao_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
