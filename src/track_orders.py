from collections import Counter


class TrackOrders:
    # https://stackoverflow.com/questions/625083/what-init-and-self-do-in-python
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals = []
        for item in self.orders:
            if item[0] == costumer:
                meals.append(item[1])
        # https://note.nkmk.me/python-collections-counter/
        occurence_count = Counter(meals)
        return occurence_count.most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        # https://pythonacademy.com.br/blog/sets-no-python
        all_meals = set()
        ordered_meals = set()
        for item in self.orders:
            all_meals.add(item[1])
        for item in self.orders:
            if item[0] == costumer:
                ordered_meals.add(item[1])
        return all_meals.difference(ordered_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        # https://pythonacademy.com.br/blog/sets-no-python
        days_of_week = set()
        days_without_person = set()
        for item in self.orders:
            days_of_week.add(item[2])
        for item in self.orders:
            if item[0] == costumer:
                days_without_person.add(item[2])
        return days_of_week.difference(days_without_person)

    def get_busiest_day(self):
        days = []
        for item in self.orders:
            days.append(item[2])
        # https://note.nkmk.me/python-collections-counter/
        occurence_count = Counter(days)
        return occurence_count.most_common()[0][0]

    def get_least_busy_day(self):
        days = []
        for item in self.orders:
            days.append(item[2])
        # https://note.nkmk.me/python-collections-counter/
        occurence_count = Counter(days)
        return occurence_count.most_common()[-1][0]
