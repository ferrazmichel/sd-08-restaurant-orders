import csv
from collections import Counter


def read_csv(filepath):
    with open(filepath) as file:
        fieldnames = ["name", "order", "week_day"]
        reader = csv.DictReader(file, fieldnames=fieldnames)
        return [data for data in reader]


def most_frequent_dish(orders, person):
    order_filter = [item["order"] for item in orders if item["name"] == person]
    dish_count = Counter(order_filter)
    return max(dish_count, key=dish_count.get)


def count_ordered_dish(orders, person, dish):
    order_filter = [item["order"] for item in orders if item["name"] == person]
    dish_count = Counter(order_filter)
    return dish_count[dish]


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)
    frequent_dish = most_frequent_dish(orders, "maria")
    count_dish = count_ordered_dish(orders, "arnaldo", "hamburguer")
    print(frequent_dish)
    print(count_dish)
