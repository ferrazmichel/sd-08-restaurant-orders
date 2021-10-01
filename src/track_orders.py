from collections import Counter
from statistics import mode


class TrackOrders:
    def __init__(self):
        self.order_data = []

    def __len__(self):
        return len(self.order_data)

    def add_new_order(self, costumer, order, day):
        one_order = {"Nome": costumer, "Pedido": order, "Dia": day}
        return self.order_data.append(one_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_order = []
        for each_order in self.order_data:
            if each_order["Nome"] == costumer:
                most_order.append(each_order["Pedido"])
        result_most_order = mode(most_order)
        return result_most_order

    def get_never_ordered_per_costumer(self, costumer):
        all_foods = set()
        order_costumer = set()
        for each_order in self.order_data:
            all_foods.add(each_order["Pedido"])
            if each_order["Nome"] == costumer:
                order_costumer.add(each_order["Pedido"])
        result_never_costumer = all_foods.difference(order_costumer)
        return result_never_costumer

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days_in = set()
        for each_day in self.order_data:
            all_days.add(each_day["Dia"])
            if each_day["Nome"] == costumer:
                days_in.add(each_day["Dia"])
        result_never_visited = all_days.difference(days_in)
        return result_never_visited

    def get_busiest_day(self):
        busiest_day = []
        for each_order in self.order_data:
            busiest_day.append(each_order["Dia"])
        result_most_order = mode(busiest_day)
        return result_most_order

    def get_least_busy_day(self):
        busiest_day = []
        for each_order in self.order_data:
            busiest_day.append(each_order["Dia"])
        counter_busiest_day = Counter(busiest_day)
        result_most_order = min(
            counter_busiest_day, key=lambda key: counter_busiest_day[key]
        )
        return result_most_order
