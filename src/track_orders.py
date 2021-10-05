from statistics import mode
# https://www.geeksforgeeks.org/python-statistics-mode-function/


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals = []
        for order in self.orders:
            if order[0] == costumer:
                meals.append(order[1])

        return mode(meals)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        days_customer = set()
        costumer_frequency = set()

        for row in self.orders:
            if row["name"] == costumer:
                costumer_frequency.add(row["day"])
            days_customer.add(row["day"])
        return days_customer.difference(costumer_frequency)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
