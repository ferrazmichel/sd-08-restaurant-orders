from collections import Counter


def without_keys(dct, keys):
    dct = dct.copy()
    for key in keys:
        dct.pop(key)
    return dct


class TrackOrders:
    def __init__(self, data=[]):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def _orders_by_customer(self, customer):
        return [
            without_keys(order, ['customer'])
            for order in self.data
            if order['customer'] == customer
        ]

    def _field_counter(self, field_name):
        return Counter([order[field_name] for order in self.data])

    def _field_counter_by_customer(self, customer, field_name):
        customer_orders = self._orders_by_customer(customer)
        return Counter([order[field_name] for order in customer_orders])

    def _never_occurred_data_by_customer(self, customer, field_name):
        all = {order[field_name] for order in self.data}
        customer_orders = self._orders_by_customer(customer)
        customer_occurrences = {order[field_name] for order in customer_orders}
        return all - customer_occurrences

    def add_new_order(self, customer, dish, week_day):
        self.data.append({
            'customer': customer,
            'dish': dish,
            'week_day': week_day,
        })

    def get_most_ordered_dish_per_costumer(self, customer):
        dishes_counter = self._field_counter_by_customer(customer, 'dish')
        return max(dishes_counter.items(), key=lambda tup: tup[1])[0]

    def get_quantity_of_dish_per_customer(self, customer, dish):
        dishes_counter = self._field_counter_by_customer(customer, 'dish')
        return dishes_counter.get(dish, 0)

    def get_never_ordered_per_costumer(self, customer):
        return self._never_occurred_data_by_customer(customer, 'dish')

    def get_days_never_visited_per_costumer(self, customer):
        return self._never_occurred_data_by_customer(customer, 'week_day')

    def get_busiest_day(self):
        day_counter = self._field_counter('week_day')
        return max(day_counter.items(), key=lambda tup: tup[1])[0]

    def get_least_busy_day(self):
        day_counter = self._field_counter('week_day')
        return min(day_counter.items(), key=lambda tup: tup[1])[0]
