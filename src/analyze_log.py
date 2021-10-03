import csv
from collections import Counter


def read_csv(path_to_file):
    # https://stackoverflow.com/questions/24662571/python-import-csv-to-list
    with open(path_to_file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        return data


def meal_most_ordered(name, orders):
    meals = []
    for item in orders:
        if item[0] == name:
            meals.append(item[1])
        # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
        occurence_count = Counter(meals)
        return occurence_count.most_common(1)[0][0]


def count_meal(name, meal_selected, orders):
    counter = 0
    for item in orders:
        if item[0] == name and item[1] == meal_selected:
            counter += 1
    return counter


def meals_not_ordered(name, orders):
    # https://pythonacademy.com.br/blog/sets-no-python
    all_meals = set()
    ordered_meals = set()
    for item in orders:
        all_meals.add(item[1])
    for item in orders:
        if item[0] == name:
            ordered_meals.add(item[1])
    return all_meals.difference(ordered_meals)


def days_without_client(name, orders):
    # https://pythonacademy.com.br/blog/sets-no-python
    days_of_week = set()
    days_without_person = set()
    for item in orders:
        days_of_week.add(item[2])
    for item in orders:
        if item[0] == name:
            days_without_person.add(item[2])
    return days_of_week.difference(days_without_person)


def analyze_log(path_to_file):
    result = ''
    data = read_csv(path_to_file)
    maria_meal_most_ordered = meal_most_ordered("maria", data)
    arnaldo_count_meal = count_meal("arnaldo", "hamburguer", data)
    joao_never_ordered = meals_not_ordered("joao", data)
    days_without_joao = days_without_client("joao", data)
    result = (
        f"{maria_meal_most_ordered}\n"
        f"{arnaldo_count_meal}\n"
        f"{joao_never_ordered}\n"
        f"{days_without_joao}"
    )
    with open("data/mkt_campaign.txt", "w") as f:
        f.write(result)
