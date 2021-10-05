from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order_list = []

    def __len__(self):
        return len(self.order_list)

    def add_new_order(self, costumer, order, day):
        self.order_list.append(
            {"costumer": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.get_stats_per_value_type("order", costumer, "max")

    def get_order_frequency_per_costumer(self, costumer, food):
        return self.get_stats_per_value_type("order", costumer), [food]

    def get_never_ordered_per_costumer(self, costumer):
        return self.customer_missing_values(costumer, "order")

    def get_days_never_visited_per_costumer(self, costumer):
        return self.customer_missing_values(costumer, "day")

    def get_busiest_day(self):
        return self.get_stats_per_value_type("day", result_type="max")

    def get_least_busy_day(self):
        return self.get_stats_per_value_type("day", result_type="min")

    def get_stats_per_value_type(
        self, value_type, customer=None, result_type="count"
    ):
        value_count = Counter(
            order[value_type]
            for order in self.order_list
            if order["costumer"] == customer or customer is None
        )

        return {
            "count": value_count,
            "max": max(value_count, key=value_count.get),
            "min": min(value_count, key=value_count.get),
        }[result_type]

    def customer_missing_values(self, customer, value_type):
        all_values = set([order[value_type] for order in self.order_list])
        customer_values = set(
            [
                order[value_type]
                for order in self.order_list
                if order["costumer"] == customer
            ]
        )

        return all_values - customer_values
