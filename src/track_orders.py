from statistics import mode
# https://www.geeksforgeeks.org/python-statistics-mode-function/
# https://www.geeksforgeeks.org/python-set-difference/#:~:text=The%20difference%20between%20the%20two,the%20difference%20between%20two%20sets.&text=We%20can%20also%20use%20%E2%80%93%20operator,the%20difference%20between%20two%20sets.
# https://www.w3schools.com/python/ref_set_difference.asp

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
        costumer_dishe = set()
        list_dishes = set()

        for value in self.orders:
            if value["name"] == costumer:
                costumer_dishe.add(value["order"])
            list_dishes.add(value["order"])
        return list_dishes.difference(costumer_dishe)

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
