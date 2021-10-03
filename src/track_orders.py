from src.Analyzer import Analyzer


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.analyzer = Analyzer(self.orders)

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"client": costumer, "item": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.analyzer.get_most_ordered_item(costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return self.analyzer.get_not_tried_items(costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return self.analyzer.get_client_not_show_up_days(costumer)

    def get_busiest_day(self):
        return self.analyzer.get_busiest_day()

    def get_least_busy_day(self):
        return self.analyzer.get_least_busy_day()

    def get_order_frequency_per_costumer(self, customer_name, item_name):
        return self.analyzer.get_client_item_count(customer_name, item_name)
