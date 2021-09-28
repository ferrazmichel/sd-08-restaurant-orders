from collections import defaultdict


data = []


class TrackOrders:
    def __len__(self):
        length = 0
        length = len(data)
        return length

    def add_new_order(self, costumer, order, day):
        data.append([costumer, order, day])
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_requst = defaultdict(int)
        for item in data:
            if costumer == item[0]:
                most_requst[item[1]] += 1
        return max(most_requst, key=most_requst.get)

    def get_never_ordered_per_costumer(self, costumer):
        cosumer_asked = set()
        all_types_of_food = set()
        for item in data:
            all_types_of_food.add(item[1])
            if costumer == item[0]:
                cosumer_asked.add(item[1])
        return all_types_of_food - cosumer_asked

    def get_days_never_visited_per_costumer(self, costumer):
        cosumer_day = set()
        all_days = set()
        for item in data:
            if costumer == item[0]:
                all_days.add(item[2])
                cosumer_day.add(item[2])
        return all_days - cosumer_day

    def get_busiest_day(self):
        most_day = defaultdict(int)
        for item in data:
            most_day[item[2]] += 1
        return max(most_day, key=most_day.get)

    def get_least_busy_day(self):
        most_day = defaultdict(int)
        for item in data:
            most_day[item[2]] += 1
        return min(most_day, key=most_day.get)
