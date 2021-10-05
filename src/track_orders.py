class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}

        most_ordered = ''
        count[most_ordered] = 0
        for order in self.orders:
            if costumer == order['costumer']:
                if order['order'] not in count:
                    count[order['order']] = 1
                else:
                    count[order['order']] += 1
                if count[order['order']] > count[most_ordered]:
                    most_ordered = order['order']

        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        all_recipes = set()
        recipe_client = set()

        for item in self.orders:
            all_recipes.add(item['order'])

            if item['costumer'] == costumer:
                recipe_client.add(item['order'])

        result = all_recipes - recipe_client

        return result

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_day = set()

        for item in self.orders:
            all_days.add(item['day'])

            if item['costumer'] == costumer:
                client_day.add(item['day'])

        result = all_days - client_day

        return result

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
