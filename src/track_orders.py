class TrackOrders:

    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = {}
        for order in self.orders:
            if order["costumer"] == costumer:
                if order["order"] not in data:
                    data[order["order"]] = 1
                else:
                    data[order["order"]] += 1
        return max(data, key=data.get)

    def get_never_ordered_per_costumer(self, costumer):
        data = set()
        costumer_data = set()
        for order in self.orders:
            data.add(order["order"])
            if order["costumer"] == costumer:
                costumer_data.add(order["order"])
        return data - costumer_data

    def get_days_never_visited_per_costumer(self, costumer):
        data = set()
        costumer_data = set()
        for order in self.orders:
            data.add(order["day"])
            if(order['costumer']) == costumer:
                costumer_data.add(order["day"])
        return data - costumer_data

    def orders_by_day(self):
        data = {}
        for order in self.orders:
            if order["day"] not in data:
                data[order["day"]] = 1
            else:
                data[order["day"]] += 1
        return data

    def get_busiest_day(self):
        data = self.orders_by_day()
        return max(data, key=data.get)

    def get_least_busy_day(self):
        data = self.orders_by_day()
        return min(data, key=data.get)
