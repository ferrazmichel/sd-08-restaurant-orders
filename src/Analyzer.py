from collections import Counter


class Analyzer:
    def __init__(self, data):
        self.data = data

    def get_orders_by_name(self, name):
        return filter(lambda order: order["client"] == name, self.data)

    def get_menu_items(self):
        return {order["item"] for order in self.data}

    def get_work_days(self):
        return {order["day"] for order in self.data}

    def get_most_ordered_item(self, name):
        items = [order["item"] for order in self.get_orders_by_name(name)]
        counter = Counter(items)
        return counter.most_common(1).pop()[0]

    def get_client_ordered_items(self, name):
        return [order["item"] for order in self.get_orders_by_name(name)]

    def get_client_item_count(self, name, item_name):
        return sum(
            order["item"] == item_name
            for order in self.get_orders_by_name(name)
        )

    def get_not_tried_items(self, name):
        menu = self.get_menu_items()
        client_ordered_items = set(self.get_client_ordered_items(name))
        return menu - client_ordered_items

    def get_client_not_show_up_days(self, name):
        show_up_days = {
            order["day"] for order in self.get_orders_by_name(name)
        }
        return self.get_work_days() - show_up_days

    def get_busiest_day(self):
        return (
            Counter([order["day"] for order in self.data])
            .most_common(1)
            .pop()[0]
        )

    def get_less_busy_day(self):
        return (
            Counter([order["day"] for order in self.data])
            .most_common()
            .pop()[0]
        )

    def analyze(self, output_path):
        with open(output_path, "w") as file:
            for action in (
                lambda: self.get_most_ordered_item("maria"),
                lambda: self.get_client_item_count("arnaldo", "hamburguer"),
                lambda: self.get_not_tried_items("joao"),
                lambda: self.get_client_not_show_up_days("joao"),
            ):
                print(action(), file=file)
