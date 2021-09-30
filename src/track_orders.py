# from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = {}

    def __len__(self):
        return len(self.orders)

    def get_dish_per_costumer(self, costumer):
        dishes = {}
        print(self.orders)
        for index in range(len(self.orders)):
            if self.orders[index]["customer"] == costumer:
                dishes.add(self.order[2])
            else:
                index += 1
        return dishes

    def add_new_order(self, costumer, order, day):
        print(self.orders)
# interação - lista de lista

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = max(self.orders[costumer]["dishes"])
        return result.key

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        for item in self.orders:
            if item[0] == costumer:
                dishes.add(item[1])
        return dishes

    def get_days_never_visited_per_costumer(self, costumer):
        alldays = ([
                "segunda-feira",
                "terça-feira",
                "sabado",
            ])
        result = self.orders[costumer]["days"]  # fazer uma iteração
        return alldays.difference(result.key)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
