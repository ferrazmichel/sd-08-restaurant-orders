from collections import defaultdict


class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        length = len(self.data) or 0
        return length

    def add_new_order(self, costumer, order, day):
        self.data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_request = defaultdict(int)
        for item in self.data:
            if costumer == item[0]:
                most_request[item[1]] += 1
        return max(most_request, key=most_request.get)

    def get_never_ordered_per_costumer(self, costumer):
        cosumer_asked = set()
        types_of_food = set()
        for item in self.data:
            types_of_food.add(item[1])
            if costumer == item[0]:
                cosumer_asked.add(item[1])
        return types_of_food - cosumer_asked

    def get_days_never_visited_per_costumer(self, costumer):
        cosumer_day = set()
        days = set()
        for item in self.data:
            days.add(item[2])
            if costumer == item[0]:
                cosumer_day.add(item[2])
        return days - cosumer_day

    def get_busiest_day(self):
        day = defaultdict(int)
        for item in self.data:
            day[item[2]] += 1
        return max(day, key=day.get)

    def get_least_busy_day(self):
        day = defaultdict(int)
        for item in self.data:
            day[item[2]] += 1
        return min(day, key=day.get)
