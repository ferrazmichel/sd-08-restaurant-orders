class TrackOrders:
    def __init__(self) -> None:
        self.orders = {}
        self.type_order = set()
        self.days = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.type_order.add(order)
        self.days.add(day)

        if self.orders.get(costumer):
            self.orders[costumer].append({"prato": order, "dia": day})
        else:
            self.orders[costumer] = [{"prato": order, "dia": day}]

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requested_dish = dict()
        is_costumer = self.orders[costumer]
        for order in is_costumer:
            if most_requested_dish.get(order["prato"]):
                most_requested_dish[order["prato"]] += 1
            else:
                most_requested_dish[order["prato"]] = 1

        result = max(most_requested_dish.items(), key=lambda x: x[1])
        return result[0]

    def get_never_ordered_per_costumer(self, costumer):
        customer_dishes = set()
        for order in self.orders[costumer]:
            customer_dishes.add(order["prato"])

        return self.type_order - customer_dishes

    def get_days_never_visited_per_costumer(self, costumer):
        customer_day = set()
        for order in self.orders[costumer]:
            customer_day.add(order["dia"])

        return self.days - customer_day

    def get_busiest_day(self):
        busiest_day = dict()

        for order in self.orders.values():
            for x_order in order:
                if busiest_day.get(x_order["dia"]):
                    busiest_day[x_order["dia"]] += 1
                else:
                    busiest_day[x_order["dia"]] = 1

        result = max(busiest_day.items(), key=lambda x: x[1])
        return result[0]

    def get_least_busy_day(self):
        less_busy_day = dict()

        for order in self.orders.values():
            for x_order in order:
                if less_busy_day.get(x_order["dia"]):
                    less_busy_day[x_order["dia"]] += 1
                else:
                    less_busy_day[x_order["dia"]] = 1

        result = min(less_busy_day.items(), key=lambda x: x[1])
        return result[0]
