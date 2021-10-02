import src.order_filters as f


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {'client': costumer, 'order': order, 'day': day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = f.filter_by_client(self.orders, costumer)
        most_ordered = f.find_most_repeated_value(client_orders, 'order')
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        client_orders = f.filter_by_client(self.orders, costumer)
        client_dishes = f.get_values_from_field(client_orders, 'order')
        all_dishes = f.get_values_from_field(self.orders, 'order')
        client_didnt_order = set(all_dishes).difference(
            set(client_dishes)
        )  # 1
        print('CLIENT_DISHES', client_dishes)
        print('ALL_DISHES', all_dishes)
        return client_didnt_order

    def get_days_never_visited_per_costumer(self, costumer):
        client_orders = f.filter_by_client(self.orders, costumer)
        days_client_did_go = f.get_values_from_field(client_orders, 'day')
        week_days = f.get_values_from_field(self.orders, 'day')
        days_client_didnt_go = set(week_days).difference(
            set(days_client_did_go)
        )  # 1
        return days_client_didnt_go

    def get_busiest_day(self):
        busiest = f.find_most_repeated_value(self.orders, 'day')
        return busiest

    def get_least_busy_day(self):
        return f.find_less_repeated_value(self.orders, 'day')
