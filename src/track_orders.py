class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        result = len(self.orders)
        return result

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        person_dict = {}
        for item in self.orders:
            if costumer == item[0]:
                if item[1] in person_dict:
                    person_dict[item[1]] += 1
                else:
                    person_dict[item[1]] = 1
        return max(person_dict, key=person_dict.get)

    def get_never_ordered_per_costumer(self, costumer):
        costumer_get = set()
        all_foods = set()
        for item in self.orders:
            all_foods.add(item[1])
            if costumer == item[0]:
                costumer_get.add(item[1])
        return all_foods.difference(costumer_get)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_day = set()
        all_days = set()
        for item in self.orders:
            all_days.add(item[2])
            if costumer == item[0]:
                costumer_day.add(item[2])
        return all_days.difference(costumer_day)

    def get_busiest_day(self):
        busy_day = {}
        for item in self.orders:
            if item[2] in busy_day:
                busy_day[item[2]] += 1
            else:
                busy_day[item[2]] = 1
        return max(busy_day, key=busy_day.get)

    def get_least_busy_day(self):
        busy_day = {}
        for item in self.orders:
            if item[2] in busy_day:
                busy_day[item[2]] += 1
            else:
                busy_day[item[2]] = 1
        return min(busy_day, key=busy_day.get)
